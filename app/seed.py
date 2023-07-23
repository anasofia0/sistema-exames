from datetime import datetime, timedelta

questoes = [
    {
        "matricula_professor": 1234,
        "tipo_questao": "VERDADEIRO_FALSO",
        "enunciado": "A água é molhada",
        "resposta_certa": "1",
        "habilitada": True
    },
    {
        "matricula_professor": 1234,
        "tipo_questao": "MULTIPLA_ESCOLHA",
        "enunciado": "Qual das opções abaixo é a letra 'a'?",
        "resposta_certa": "a",
        "opcoes": ["a", "b", "c", "d"],
        "habilitada": True
    },
    {
        "matricula_professor": 1234,
        "tipo_questao": "ENTRADA_NUMERO",
        "enunciado": "Quantos dedos normalmente se tem em uma mão?",
        "resposta_certa": "5",
        "habilitada": True
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

min10 = datetime.now()
min10 += timedelta(minutes=10)

min60 = datetime.now()
min60 += timedelta(hours=1)

exames = [
    {
        "nome": "teste1",
        "professor": 1234,
        "nota": 10,
        "data_abertura": datetime.now(),
        "data_fechamento": min60,
        "duracao": 3600
    },
    {
        "nome": "teste2",
        "professor": 1234,
        "nota": 10,
        "data_abertura": datetime.now(),
        "data_fechamento": min10,
        "duracao": 60
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
    },
        {
        "exame_id": 2,
        "questao_id": 1,
        "nota": 5
    },
    {
        "exame_id": 2,
        "questao_id": 2,
        "nota": 5
    }
]
