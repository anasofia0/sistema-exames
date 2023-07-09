from flask.cli import AppGroup

from .app import db
from .models import Questao
from .seed import questoes

seed_cli = AppGroup("seed")


@seed_cli.command("questoes")
def seed_questoes():
    "Add seed data to the database."
    for questao in questoes:
        db.session.add(Questao(**questao))
    db.session.commit()
