from flask.cli import AppGroup

from .app import db
from .models import Questao, User, Exame, QuestaoExame, TempoExameAluno, RespostaAluno, Nota
from .seed import questoes, users, exames, exames_questoes, tempo_exame_aluno, resposta_aluno, nota

seed_cli = AppGroup("seed")


@seed_cli.command("questoes")
def seed_questoes():
    "Add seed data to the database."
    for questao in questoes:
        db.session.add(Questao(**questao))
    db.session.commit()

@seed_cli.command("users")
def seed_users():
    for user in users:
        db.session.add(User(**user))
    db.session.commit()

@seed_cli.command("exames")
def seed_exames():
    for exame in exames:
        db.session.add(Exame(**exame))
    for eq in exames_questoes:
        db.session.add(QuestaoExame(**eq))
    for resp in resposta_aluno:
        db.session.add(RespostaAluno(**resp))
    for temp in tempo_exame_aluno:
        db.session.add(TempoExameAluno(**temp))
    for n in nota:
        db.session.add(Nota(**n))
    db.session.commit()

@seed_cli.command("all")
def seed_all():
    seed_questoes()
    seed_users()
    seed_exames()