from decimal import Decimal
from app.forms import form_questao
from app.services import calcular_nota
from app.services.professor_anotation import professor_required
from ..models.user import User
from ..models.exame import Nota, TempoExameAluno

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
    jsonify,
    flash
)
from ..models import Exame, Questao, QuestaoExame, RespostaAluno, questao
from flask_login import current_user, login_required
from ..forms import CriaExameForm
from ..services.salvar_resposta import salvar_resposta_estudante
from datetime import datetime
import time

bp = Blueprint("exames", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    return 0


@bp.route("/exam/create", methods=["GET", "POST"])
@login_required
@professor_required
def cria_exame():
    form = CriaExameForm()
    matricula = current_user.get_id()
    questoes = Questao.query.filter_by(matricula_professor=matricula).all()
    form.questoes.choices = [(q.id, q.enunciado) for q in questoes]

    if form.validate_on_submit():

        data_abertura = form.data_abertura.data
        data_fechamento = form.data_fechamento.data

        ok = checa_datas(data_abertura, data_fechamento)

        if ok:

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
            for questao in form.questoes.data:
                questao_exame = QuestaoExame(
                    exame_id=novo_exame.id, questao_id=questao, nota=10/len(form.questoes.data)
                )
                db.session.add(questao_exame)
            db.session.commit()

            return redirect("/logged/professor")
    print(form.errors)
    return render_template("criacao_exame.html", form=form)


@bp.route("/exam/list", methods=["GET"])
@login_required
def lista_exames():
    # Mostra todos os escames disponíveis
    exams = Exame.query.all()

    # Renderiza a tela de exames
    return render_template("listaExames.html", exams=exams)

@bp.route('/exam/<int:id>', methods=['GET'])
@login_required
def detalhes_exame(id):
    exam = Exame.query.get(id)
    if exam is None:
        abort(404, description="Exame não encontrado")
    return render_template('detalhesExame.html', exam=exam)


@bp.route("/exam/<int:id>/<int:question_index>", methods=["GET", "POST"])
@login_required
def comeca_exame(id, question_index):
    # Procura o exame na base de dados
    time.sleep(0.2)
    exam = Exame.query.get(id)
    tempo_aluno = TempoExameAluno.query.filter_by(exame_id=exam.id, matricula_aluno=current_user.matricula).first()
    tempo_total = exam.duracao
    tempo_restante = tempo_total - (datetime.now() - tempo_aluno.tempo_inicio).total_seconds()
    if tempo_aluno.terminou:
        flash("Já finalizou a prova")
        return redirect("/logged/aluno")
    if (exam.data_fechamento - datetime.now()).total_seconds() < 0:
        flash("Passou do prazo")
        return redirect(url_for('exames.revisao', id=id))
    elif tempo_restante < 0:
        flash("Tempo esgotado")
        return redirect(url_for('exames.revisao', id=id))
    # Se não existe exame ou o index da questao é menor que 0 ou maior que o numero de questoes retorna 404
    if exam is None or question_index < 0 or question_index >= len(exam.questoes):
        abort(404)

    # Pega a questão atual do exame
    question = exam.questoes[question_index]

    # Cria o form apropriado para o tipo de questão
    if question.tipo_questao == questao.TipoQuestao.VERDADEIRO_FALSO:
        print("VERDADEIRO_FALSO")
        form = form_questao.RespostaVFForm()
    elif question.tipo_questao == questao.TipoQuestao.MULTIPLA_ESCOLHA:
        print("MULTIPLA_ESCOLHA")
        form =  form_questao.RespostaMultiplaEscolhaForm()
        form.resposta.choices = [
            (option, option) for option in question.opcoes
        ]
    elif question.tipo_questao ==  questao.TipoQuestao.ENTRADA_NUMERO:
        print("ENTRADA_NUMERO")
        form =  form_questao.RespostaNumericoForm()
    else:
        abort(400)  # ERROR 400 BAD REQUEST
        
    if request.method == 'GET':
        previous_answer = RespostaAluno.query.filter_by(id_exame=exam.id, id_questao=question.id, id_aluno=current_user.matricula).first()
        if previous_answer:
            if question.tipo_questao == questao.TipoQuestao.VERDADEIRO_FALSO:
                form.resposta.data = previous_answer.resposta
            elif question.tipo_questao == questao.TipoQuestao.MULTIPLA_ESCOLHA:
                form.resposta.data = str(previous_answer.resposta)
            elif question.tipo_questao == questao.TipoQuestao.ENTRADA_NUMERO:
                form.resposta.data = Decimal(previous_answer.resposta)

    
    # Se o form enviado for valido, salva a resposta do aluno
    if form.validate_on_submit():
        print("VALIDO")
        salvar_resposta_estudante(exam.id, question.id, current_user.matricula, str(form.resposta.data))

        prox_questao = question_index + 1
        if prox_questao < len(exam.questoes):
            # Ir para proxima questavao
            return redirect(url_for("exames.comeca_exame", id=id, question_index=prox_questao))
        else:
            # A prova acabou
            # Redirecionar para a pagina de revisao
            return redirect(url_for('exames.revisao', id=id))
    # Renderiza a pagina do exame, passando o exame, a questão e o form para o template
    return render_template("relizarExame.html", exam=exam, question=question, form=form, question_index=question_index, tempo_restante=tempo_restante)

@bp.route("/exam/<int:id_exame>/submit_time", methods=["POST"])
@login_required
def salva_tempo(id_exame):

    if not TempoExameAluno.query.filter_by(exame_id=id_exame, matricula_aluno=current_user.matricula).first():
        tempo_atual = request.form.get('tempo_atual')
        tempo_atual = datetime.strptime(tempo_atual, "%Y-%m-%d %H:%M:%S")
        # print(tempo_atual)
        matricula = int(current_user.matricula)

        tempo = TempoExameAluno(matricula_aluno=matricula,
                                exame_id=id_exame,
                                tempo_inicio=tempo_atual,
                                terminou = False)
        db.session.add(tempo)
        db.session.commit()

    return jsonify(success=True)


@bp.route('/exam/review/<int:id>', methods=['GET'])
@login_required
def revisao(id):
    exam = Exame.query.get(id)
    if exam is None:
        abort(404)

    # Procura pelas respostas do aluno
    answers = RespostaAluno.query.filter_by(id_exame=exam.id, id_aluno=current_user.matricula).all()
    
    #Renderiza a pagina de revisao
    return render_template('revisao.html', exam=exam, answers=answers)

@bp.route("/exam/submit/<int:id>", methods=["GET", "POST"])
@login_required
def enviar_exame(id):
    exame = Exame.query.get(id)

    if exame is None:
        abort(404)
    nota = calcular_nota.calcular_nota_aluno(exame.id, current_user.matricula)
    nota_instance = Nota.query.filter_by(matricula_aluno=current_user.matricula, exame_id=exame.id).first()
    if nota_instance:
        nota_instance.nota = nota
    else:
        nota_instance = Nota(matricula_aluno=current_user.matricula, exame_id=exame.id, nota=nota)
        db.session.add(nota_instance)

    tempo_exame = TempoExameAluno.query.filter_by(exame_id=id, matricula_aluno=current_user.matricula).first()
    tempo_exame.terminou = True

    db.session.commit()

    return redirect(url_for("dashboards.loggedAluno"))

@bp.route("/grades", methods=["GET"])
@login_required
def ver_notas():
    notas = Nota.query.filter_by(matricula_aluno=current_user.matricula).all()
    dados_exame = []

    for nota in notas:
        respostas_aluno = RespostaAluno.query.filter_by(id_exame=nota.exame_id, id_aluno=current_user.matricula).all()
        dados_exame.append({
            "exame": nota.exame,
            "nota": nota,
            "respostas_aluno": respostas_aluno
        })

    return render_template("notas.html", dados_exame=dados_exame)

def datetime2int(datetime):
    return 3600*datetime.hour + 60*datetime.minute + datetime.second

def checa_datas(data_abertura, data_fechamento):
    ok = True
    if (data_fechamento-data_abertura).total_seconds() < 0:
        flash('Data de abertura depois da data de fechamento')
        ok = False
    if (data_abertura-datetime.now()).total_seconds() < 60:
        flash('Data de abertura com mínimo de um minuto de diferença do momento atual')
        ok = False
    
    return ok