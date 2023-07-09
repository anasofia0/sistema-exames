from ..app import db
from flask import Blueprint, render_template, redirect, request
from ..models import Exame, Questao, QuestaoExame
from flask_login import current_user, login_required
from ..forms import CriaExameForm

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
    questoes = Questao.query.filter_by(matricula=matricula).all()
    form.questoes.choices = [(q.id, q.description) for q in Question.query.all()]

    if form.validate_on_submit():

        novo_exame = Exame(nome=request.form.get("nome"),
                           professor=matricula,
                           nota=request.form.get("nota"),
                           data_abertura=request.form.get("data_abertura"),
                           data_fechamento=request.form.get("data_fechamento"),
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

        return redirect("/")

    return render_template('criacao_exame.html', form=form)


def insere_questao():
    pass
