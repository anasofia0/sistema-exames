from ..models.exame import Exame
from ..models.resposta_aluno import RespostaAluno
from ..models.questao import TipoQuestao


from decimal import Decimal

def calcular_nota_aluno(id_exame, id_aluno):
    exame = Exame.query.get(id_exame)

    respostas_aluno = RespostaAluno.query.filter_by(id_exame=id_exame, id_aluno=id_aluno).all()

    respostas_corretas = 0

    for questao in exame.questoes:

        resposta_aluno = next((resposta for resposta in respostas_aluno if resposta.id_questao == questao.id), None)

        if resposta_aluno:
            if questao.tipo_questao == TipoQuestao.ENTRADA_NUMERO:
                if Decimal(resposta_aluno.resposta) == Decimal(questao.resposta_certa):
                    respostas_corretas += 1
            else:
                if resposta_aluno.resposta == questao.resposta_certa:
                    respostas_corretas += 1

    nota = (respostas_corretas / len(exame.questoes)) * 10  

    return nota

