from datetime import datetime, timedelta

questoes = [
    {
        "matricula_professor": 1234,
        "tipo_questao": "VERDADEIRO_FALSO",
        "enunciado": "A água é molhada",
        "resposta_certa": "True",
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
        "nome": "Pedro",
        "email": "pedro@unb.br",
        "professor": True,
        "senha": "asdfgh"
    },
    {
        "matricula": "1",
        "nome": "Ester",
        "email": "ester@unb.br",
        "professor": False,
        "senha": "asdfgh"
    },
    {
        "matricula": "2",
        "nome": "Jorginho",
        "email": "jorginho@unb.br",
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
        "exame_id": 1,
        "questao_id": 3,
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

tempo_exame_aluno = [
    {
        "matricula_aluno": 2,
        "exame_id": 1,
        "tempo_inicio": datetime.now(),
        "terminou": True
    }
]

resposta_aluno = [
    {
        "id_exame": 1,
        "id_questao": 1,
        "id_aluno": 2,
        "resposta": "True",
        "nota": 0
    },
    {
        "id_exame": 1,
        "id_questao": 2,
        "id_aluno": 2,
        "resposta": "b",
        "nota": 0
    },
    {
        "id_exame": 1,
        "id_questao": 3,
        "id_aluno": 2,
        "resposta": "10",
        "nota": 0
    }
]

nota = [
    {
        "matricula_aluno": 2,
        "exame_id": 1,
        "nota": 10/3
    }
]