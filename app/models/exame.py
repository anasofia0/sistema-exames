from . import db
from sqlalchemy import Column, String, Integer, Boolean, Float, DATETIME
from flask_login import UserMixin

class Exame(db.Model):
    __tablename__ = "exame"

    id_exame = Column(Integer, primary_key=True)
    nome = Column(String(50))
    professor = Column(Integer)
    nota = Column(Float)
    data_criacao = Column(DATETIME)
    prazo = Column(DATETIME)

    # get_id method
    def get_id(self):
        return str(self.id_exame)

# from . import db
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy import String, Boolean


# class User(db.Model):
#     __tablename__ = "user"

#     matricula: Mapped[String] = mapped_column(String(), primary_key=True)
#     nome: Mapped[String] = mapped_column(String(50))
#     email: Mapped[String] = mapped_column(String())
#     professor: Mapped[Boolean] = mapped_column(Boolean())
#     senha: Mapped[String] = mapped_column(String())
