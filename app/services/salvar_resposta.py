from ..models.resposta_aluno import RespostaAluno
from ..app import db


def salver_resposta_estudante(exame_id, questao_id, aluno_id, resposta):
    
    #Procura pra ver se o aluno ja respondeu
    resposta_existente = RespostaAluno.query.filter_by(
        id_exame=exame_id,
        id_questao=questao_id,
        id_aluno=aluno_id
    ).first()
    if(resposta_existente):
        resposta_existente.resposta = resposta
    else:
        #  Cria novo RespostaAluno
        resposta_aluno = RespostaAluno(
            id_exame=exame_id,
            id_questao=questao_id,
            id_aluno=aluno_id,
            resposta=resposta,
            nota=0.0,  # Talvez seja bom calcular a nota aqui
        )
        db.session.add(resposta_aluno)

    db.session.commit()
