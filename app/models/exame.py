from . import db
from sqlalchemy import Column, String, Integer, Float, DATETIME, ForeignKey, Interval


class Exame(db.Model):
    __tablename__ = "exame"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    professor = Column(Integer, nullable=False) # todo
    nota = Column(Float, nullable=False)
    data_abertura = Column(DATETIME, nullable=False)
    data_fechamento = Column(DATETIME, nullable=False)
    duracao = Column(Integer, nullable=True)

    questoes = db.relationship("Questao", secondary="questao_exame", back_populates="exames") # many to many
    def get_id(self):
        return str(self.id)

    # get_name method
    def get_name(self):
        return self.nome

class QuestaoExame(db.Model):
    __tablename__ = "questao_exame"

    exame_id = Column(Integer, ForeignKey("exame.id"), nullable=False, primary_key=True)
    questao_id = Column(Integer, ForeignKey("questao.id"), nullable=False, primary_key=True)
    nota = Column(Float, nullable=False)

    #questao = db.relationship("Questao", back_populates="questao")
    #exame = db.relationship("Exame", back_populates="exame")
