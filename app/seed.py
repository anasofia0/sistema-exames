from datetime import datetime

questoes = [
    {
        "matricula_professor": 1234,
        "tipo_questao": "VERDADEIRO_FALSO",
        "enunciado": "A água é molhada",
        "resposta_certa": "1"
    },
    {
        "matricula_professor": 1234,
        "tipo_questao": "MULTIPLA_ESCOLHA",
        "enunciado": "Qual das opções abaixo é a letra 'a'?",
        "resposta_certa": "a"
    },
    {
        "matricula_professor": 1234,
        "tipo_questao": "ENTRADA_NUMERO",
        "enunciado": "Quantos dedos normalmente se tem em uma mão?",
        "resposta_certa": "5"
    },
]

users = [
    {
        "matricula": "1234",
        "nome": "pedro",
        "email": "pedro@unb.br",
        "professor": True,
        "senha": "asdfgh"
    },
    {
        "matricula": "1",
        "nome": "ester",
        "email": "ester@unb.br",
        "professor": False,
        "senha": "asdfgh"
    }
]

exames = [
    {
        "nome": "teste1",
        "professor": 1234,
        "nota": 10,
        "data_abertura": datetime.now(),
        "data_fechamento": datetime.now()
    }
]

exames_questoes = [
    {
        "exame_id": 1,
        "questao_id": 1,
        "nota": 5
    },
    {
        "exame_id": 1,
        "questao_id": 2,
        "nota": 5
    }
]
