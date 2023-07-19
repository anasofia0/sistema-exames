from flask import Flask, redirect, url_for, Blueprint
from .app.models import exame, questao
from .app.app import db
from datetime import datetime, timedelta


bp = Blueprint("preencher", __name__)


@bp.route('/create_exam')
def create_exam():
    # Create a new exam
    new_exame = exame.Exame(
        nome='Sample Exam',
        professor=1,  # Assuming a professor with ID 1 exists
        nota=10.0,
        data_abertura=datetime.now(),
        data_fechamento=datetime.now() + timedelta(days=7)
    )
    db.session.add(new_exame)
    db.session.commit()
    # Create a verdadeiro_falso question
    vf_question = questao.Questao(
        matricula_professor=1,
        tipo_questao=questao.TipoQuestao.VERDADEIRO_FALSO,
        enunciado='True or False: The sky is blue.',
        resposta_certa='True'
    )
    db.session.add(vf_question)

    # Create a entrada_numero question
    num_question = questao.Questao(
        matricula_professor=1,
        tipo_questao=questao.TipoQuestao.ENTRADA_NUMERO,
        enunciado='What is 2 + 2?',
        resposta_certa='4'
    )
    db.session.add(num_question)

    # Create a multipla_escolha question
    me_question = questao.Questao(
        matricula_professor=1,
        tipo_questao=questao.TipoQuestao.MULTIPLA_ESCOLHA,
        enunciado='What is the capital of France?',
        resposta_certa='Paris'
    )
    db.session.add(me_question)

    # Add the questions to the exam
    vf_questao_exame = exame.QuestaoExame(exame_id=new_exame.id, questao_id=vf_question.id, nota=0.0)
    num_questao_exame = exame.QuestaoExame(exame_id=new_exame.id, questao_id=num_question.id, nota=0.0)
    me_questao_exame = exame.QuestaoExame(exame_id=new_exame.id, questao_id=me_question.id, nota=0.0)

    db.session.add(vf_questao_exame)
    db.session.add(num_questao_exame)
    db.session.add(me_questao_exame)

    db.session.commit()

    return redirect(url_for('index'))  # Redirect to the index page after creating the exam

