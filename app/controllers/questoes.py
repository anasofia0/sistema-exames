from flask import Blueprint, render_template, redirect, abort
from flask_login import current_user, login_required
from ..app import db
from ..models import Questao
from ..forms import CriacaoMultiplaEscolhaForm, CriacaoNumericoForm, CriacaoVFForm

bp = Blueprint("questoes", __name__)

@bp.route("/questoes/", methods=["GET"])
@login_required
def index():
    return render_template()

@bp.route("/questoes/create", methods=["GET"])
@login_required
def cria_questoes():
    return render_template("cria_questao_base.html")

@bp.route("/questoes/create/<int:tipo>", methods=["GET", "POST"])
@login_required
def cria_questao(tipo):

        print('\n\n\n\nBBBBs\n\n\n')
    if tipo == 0:
        form = CriacaoVFForm()

        if form.validate_on_submit():
            print('\n\n\n\naaaaaaaa\n\n\n')
            salva_questao(form, "VERDADEIRO_FALSO")
            return redirect("/questoes/create")
        return render_template("cria_vf.html", form = form)
    
    elif tipo == 1:
        return render_template()
    elif tipo == 2:
        return render_template()
    else:
        abort(404)

def salva_questao(form, tipo, opcoes=None):

    questao = Questao(
        matricula=current_user.get_id(),
        tipo_questao=tipo,
        enunciado=form.enunciado,
        resposta_certa=form.resposta,
        opcoes=opcoes
    )
    db.session.add(questao)
    db.session.commit()