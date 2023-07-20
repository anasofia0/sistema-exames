from app.forms import form_questao

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
from ..models import Exame, Questao, QuestaoExame, RespostaAluno, questao
from flask_login import current_user, login_required
from ..forms import CriaExameForm, form_resposta_aluno
from ..services.salvar_resposta_aluno import save_student_answer
from datetime import datetime

bp = Blueprint("criacao_exames", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    return 0


@bp.route("/exam/create", methods=["GET", "POST"])
@login_required
def cria_exame():
    form = CriaExameForm()
    matricula = current_user.get_id()
    questoes = Questao.query.filter_by(matricula_professor=matricula).all()
    form.questoes.choices = [(q.id, q.enunciado) for q in questoes]

    if form.validate_on_submit():

        data_abertura = form.data_abertura.data
        data_fechamento = form.data_fechamento.data

        checa_datas(data_abertura, data_fechamento)

        novo_exame = Exame(
            nome=request.form.get("nome"),
            professor=matricula,
            nota=request.form.get("nota"),
            data_abertura=data_abertura,
            data_fechamento=data_fechamento,
            duracao = datetime2int(form.duracao.data)
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

@bp.route('/exam/<int:id>', methods=['GET'])
def detalhes_exame(id):
    exam = Exame.query.get(id)
    if exam is None:
        abort(404, description="Exame não encontrado")
    return render_template('detalhesExame.html', exam=exam)




@bp.route("/exam/<int:id>/<int:question_index>", methods=["GET", "POST"])
def comeca_exame(id, question_index):
    # Procura o exame na base de dados
    exam = Exame.query.get(id)

    # Se não existe exame ou o index da questao é menor que 0 ou maior que o numero de questoes retorna 404
    if exam is None or question_index < 0 or question_index >= len(exam.questoes):
        abort(404)

    # Pega a questão atual do exame
    question = exam.questoes[question_index]

    # Cria o form apropriado para o tipo de questão
    if question.tipo_questao == questao.TipoQuestao.VERDADEIRO_FALSO:
        form = form_questao.RespostaVFForm()
    elif question.tipo_questao == questao.TipoQuestao.MULTIPLA_ESCOLHA:
        form =  form_questao.RespostaMultiplaEscolhaForm()
        form.resposta.choices = [
            (option.value, option.label) for option in question.opcoes
        ]
    elif question.tipo_questao ==  questao.TipoQuestao.ENTRADA_NUMERO:
        form =  form_questao.RespostaNumericoForm()
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
    return render_template("relizarExame.html", exam=exam, question=question, form=form)

@bp.route('/exam/review/<int:id>', methods=['GET'])
def revisao(id):
    exam = Exame.query.get(id)
    if exam is None:
        abort(404)

    # Procura pelas respostas do aluno
    answers = RespostaAluno.query.filter_by(id_exame=exam.id, id_aluno=current_user.id).all()
    
    #Renderiza a pagina de revisao
    return render_template('revisao.html', exam=exam, answers=answers)

def datetime2int(datetime):
    return 3600*datetime.hour + 60*datetime.minute + datetime.second

def checa_datas(data_abertura, data_fechamento):
    if (data_fechamento-data_abertura).total_seconds() < 0:
        raise ValueError('Data de abertura depois da data de fechamento')
    if (data_abertura-datetime.now()).total_seconds() < 60:
        raise ValueError('Data de abertura com mínimo de um minuto de diferença do momento atual')