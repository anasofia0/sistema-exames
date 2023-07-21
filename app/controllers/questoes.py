from flask import Blueprint, render_template, redirect, abort, request
from flask_login import current_user, login_required
from ..app import db
from ..models import Questao, TipoQuestao

from ..forms import (CriacaoMultiplaEscolhaForm,
                     CriacaoNumericoForm,
                     CriacaoVFForm,
                     EditaVFForm,
                     EditaNumericoForm,
                     EditaMultiplaEscolhaForm
)

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

    if tipo == 0:
        form = CriacaoVFForm()
        enum_tipo = "VERDADEIRO_FALSO"
    elif tipo == 1:
        form = CriacaoNumericoForm()
        enum_tipo = "ENTRADA_NUMERO"
    elif tipo == 2:
        form = CriacaoMultiplaEscolhaForm()
        enum_tipo = "MULTIPLA_ESCOLHA"
    else:
        abort(404)
    
    if form.validate_on_submit():
        if tipo == 2:
            opcoes = request.form.getlist('opcoes')
            i = int(request.form.getlist('resposta')[0])
            resposta = opcoes[i]
        else:
            opcoes = None
            resposta = str(form.resposta.data)

        questao = Questao(
            matricula_professor=current_user.get_id(),
            tipo_questao=enum_tipo,
            enunciado=form.enunciado.data,
            resposta_certa=resposta,
            opcoes=opcoes,
            habilitada=True
        )
        db.session.add(questao)
        db.session.commit()

        return redirect("/questoes/create")
    return render_template("cria_questao.html", form = form, tipo = tipo)
    

@bp.route("/questoes/edit", methods=["GET"])
@login_required
def edita_questao_index():
    questoes = Questao.query.filter_by(matricula_professor=current_user.get_id()).all()
    return render_template("edita_questao_index.html", questoes = questoes)

@bp.route("/questoes/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edita_questao(id):

    questao = db.get_or_404(Questao, id)
    tipo = questao.tipo_questao
    opcoes = None
    if tipo == TipoQuestao.VERDADEIRO_FALSO:
        form = EditaVFForm(obj = questao)
    elif tipo == TipoQuestao.ENTRADA_NUMERO:
        form = EditaNumericoForm(obj = questao)
    else:
        form = EditaMultiplaEscolhaForm(obj = questao)
        opcoes = questao.opcoes
        opcoes = [(i, opcoes[i]) for i in range(len(opcoes))]

    if form.validate_on_submit():
        if tipo == TipoQuestao.MULTIPLA_ESCOLHA:
            opcoes = request.form.getlist('opcoes')
            i = int(request.form.getlist('resposta')[0])
            resposta = opcoes[i]
        else:
            opcoes = None
            resposta = str(form.resposta.data)
        print()
        print(resposta)
        print()

        questao.enunciado = form.enunciado.data
        questao.resposta_certa = resposta
        questao.opcoes = opcoes
        questao.habilitada=form.habilitada.data
        db.session.commit()

        return redirect("/questoes/edit")

    return render_template("edita_questao.html", form=form, tipo=tipo, id=id, opcoes=opcoes)


# def salva_questao(form, tipo, resposta, opcoes=None, habilitada=True, id=None):

#     questao = Questao(
#         matricula_professor=current_user.get_id(),
#         tipo_questao=tipo,
#         enunciado=form.enunciado.data,
#         resposta_certa=resposta,
#         opcoes=opcoes,
#         habilitada=habilitada
#     )
#     db.session.add(questao)
#     db.session.commit()