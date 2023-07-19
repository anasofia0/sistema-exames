from ..app import db
from flask import Blueprint, render_template, redirect, request
from ..models import Exame, Questao, QuestaoExame
from flask_login import current_user, login_required
from ..forms import CriaExameForm
from datetime import datetime

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

        data_abertura = form.data_abertura.data
        data_fechamento = form.data_fechamento.data

        checa_datas(data_abertura, data_fechamento)

        novo_exame = Exame(nome=request.form.get("nome"),
                           professor=matricula,
                           nota=request.form.get("nota"),
                           data_abertura=data_abertura,
                           data_fechamento=data_fechamento,
                           duracao = datetime2int(form.duracao.data)
        )
        db.session.add(novo_exame)
        db.session.flush()
        for questao in questoes:
            questao_exame = QuestaoExame(exame_id=novo_exame.id,
                                         questao_id=questao.id,
                                         nota=questao.id * 10
            )
            db.session.add(questao_exame)
        db.session.commit()

        return redirect("/logged/professor")
    print(form.errors)
    return render_template('criacao_exame.html', form=form)

def datetime2int(datetime):
    return 3600*datetime.hour + 60*datetime.minute + datetime.second

def checa_datas(data_abertura, data_fechamento):
    if (data_fechamento-data_abertura).total_seconds() < 0:
        raise ValueError('Data de abertura depois da data de fechamento')
    if (data_abertura-datetime.now()).total_seconds() < 60:
        raise ValueError('Data de abertura com mínimo de um minuto de diferença do momento atual')