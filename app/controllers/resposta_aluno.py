from flask import render_template, request, redirect, url_for
from flask_login import current_user
from flask import Blueprint

from ..forms import form_resposta_aluno
from ..services import salvar_resposta_aluno
from ..models.questao import Questao


resposta_aluno_bp = Blueprint("resposta_aluno", __name__)


def answer_question(exame_id, questao_id):
    # Busca a questão no banco de dados
    questao = Questao.query.get(questao_id)

    # Verifica se a questão existe
    if questao is None:
        return redirect(
            url_for("error_page")
        )  # Substituir 'error_page' com o nome da pagina de erro

    # Cria o form
    if questao.tipo_questao == form_resposta_aluno.TipoQuestao.VERDADEIRO_FALSO:
        form = form_resposta_aluno.VerdadeiroFalsoForm()
    elif questao.tipo_questao == form_resposta_aluno.TipoQuestao.MULTIPLA_ESCOLHA:
        form = form_resposta_aluno.MultiplaEscolhaForm()
        form.answer.choices = questao.get_options()
    elif questao.tipo_questao == form_resposta_aluno.TipoQuestao.ENTRADA_TEXTO:
        form = form_resposta_aluno.EntradaNumeroForm()
    else:
        return redirect(
            url_for("error_page")
        )  # Substituir 'error_page' com o nome da pagina de erro'
    if form.validate_on_submit():
        # Pega o id do aluno
        aluno_id = current_user.matricula

        # Salva a resposta do aluno
        salvar_resposta_aluno(exame_id, questao_id, aluno_id, form.answer.data)

        # Redireciona para a próxima questao
        return redirect(
            url_for("next_page")
        )  # Substituir 'next_page' com o nome da rota da proxima pagina

    return render_template("answer_question.html", form=form)
