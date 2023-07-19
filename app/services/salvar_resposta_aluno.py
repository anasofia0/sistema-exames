from ..models.resposta_aluno import RespostaAluno
from ..app import db


def save_student_answer(exame_id, questao_id, aluno_id, resposta):
    # Create a new RespostaAluno object
    resposta_aluno = RespostaAluno(
        id_exame=exame_id,
        id_questao=questao_id,
        id_aluno=aluno_id,
        resposta=resposta,
        nota=0.0,  # You might want to calculate this based on the correctness of the answer
    )

    # Add the new object to the session
    db.session.add(resposta_aluno)

    # Commit the session to save the changes
    db.session.commit()
