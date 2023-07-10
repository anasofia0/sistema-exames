from flask.cli import AppGroup

from .app import db
from .models import Questao, User, Exame, QuestaoExame
from .seed import questoes, users, exames, exames_questoes

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
    db.session.commit()
