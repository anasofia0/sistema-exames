from datetime import datetime

from ..app import db
from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    render_template,
    abort,
    redirect,
    url_for,
)
from ..models import Exame, Questao, QuestaoExame, RespostaAluno
from flask_login import current_user, login_required
from ..forms import CriaExameForm, form_resposta_aluno
from ..services.salvar_resposta_aluno import save_student_answer

bp = Blueprint("criacao_exames", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    return 0


# inserir questoes para testar
# tentar fazer inserir questao_exame
# tela simples -> criar/começar exame
# form criar exame
@bp.route("/exam/new", methods=["GET"])
@login_required
def cria_exame_form():
    return render_template("criacao_exame.html")


@bp.route("/exam/create", methods=["GET", "POST"])
@login_required
def cria_exame():
    form = CriaExameForm()
    matricula = current_user.get_id()
    questoes = Questao.query.filter_by(matricula_professor=matricula).all()
    form.questoes.choices = [(q.id, q.enunciado) for q in questoes]

    if form.validate_on_submit():
        novo_exame = Exame(
            nome=request.form.get("nome"),
            professor=matricula,
            nota=request.form.get("nota"),
            data_abertura=form.data_abertura.data,
            data_fechamento=form.data_fechamento.data,
        )
        db.session.add(novo_exame)
        db.session.flush()
        for questao in questoes:
            questao_exame = QuestaoExame(
                exame_id=novo_exame.id, questao_id=questao.id, nota=questao.id * 10
            )
            db.session.add(questao_exame)
        db.session.commit()

        return redirect("/logged/professor")
    print(form.errors)
    return render_template("criacao_exame.html", form=form)


@bp.route("/exam/list", methods=["GET"])
def lista_exames():
    # Mostra todos os escames disponíveis
    exams = Exame.query.all()

    # Renderiza a tela de exames
    return render_template("listaExames.html", exams=exams)


@bp.route("/exam/<int:id>/<int:question_index>", methods=["GET", "POST"])
def exame(id, question_index):
    # Procura o exame na base de dados
    exam = Exame.query.get(id)

    # Se não existe exame ou o index da questao é menor que 0 ou maior que o numero de questoes retorna 404
    if exam is None or question_index < 0 or question_index >= len(exam.questoes):
        abort(404)

    # Pega a questão atual do exame
    question = exam.questoes[question_index]

    # Creia o form apropriado para o tipo de questão
    if question.tipo_questao == form_resposta_aluno.TipoQuestao.VERDADEIRO_FALSO:
        form = form_resposta_aluno.RespostaVFForm()
    elif question.tipo_questao == form_resposta_aluno.TipoQuestao.MULTIPLA_ESCOLHA:
        form = form_resposta_aluno.RespostaMultiplaEscolhaForm()
        form.resposta.choices = [
            (option.value, option.label) for option in question.opcoes
        ]
    elif question.tipo_questao == form_resposta_aluno.TipoQuestao.ENTRADA_NUMERO:
        form = form_resposta_aluno.RespostaNumericoForm()
    else:
        abort(400)  # ERROR 400 BAD REQUEST

    # Se o form enviado for valido, salva a resposta do aluno
    if form.validate_on_submit():
        save_student_answer(exam.id, question.id, current_user.id, form.resposta.data)
        prox_questao = question_index + 1
        if prox_questao < len(exam.questoes):
            # Ir para proxima questavao
            return redirect(url_for("exame", id=id, question_index=prox_questao))
        else:
            # A prova acabou
            # Reduirecionar para a pagina de revisao
            return redirect(url_for('revisao', id=id))
    # Renderiza a pagina do exame, passando o exame, a questão e o form para o template
    return render_template("exam.html", exam=exam, question=question, form=form)

@bp.route('/exam/review/<int:id>', methods=['GET'])
def revisao(id):
    exam = Exame.query.get(id)
    if exam is None:
        abort(404)

    # Procura pelas respostas do aluno
    answers = RespostaAluno.query.filter_by(id_exame=exam.id, id_aluno=current_user.id).all()
    
    #Renderiza a pagina de revisao
    return render_template('revisao.html', exam=exam, answers=answers)


def insere_questao():
    pass
