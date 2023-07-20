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

class Nota(db.Model):
    __tablename__ = "nota"

    id = db.Column(db.Integer, primary_key=True)
    matricula_aluno = db.Column(db.Integer, db.ForeignKey('user.matricula'), nullable=False)
    exame_id = db.Column(db.Integer, db.ForeignKey('exame.id'), nullable=False)
    nota = db.Column(db.Float, nullable=False)  # Changed from Integer to Float

    aluno = db.relationship('User', backref=db.backref('notas', lazy=True))
    exame = db.relationship('Exame', backref=db.backref('notas', lazy=True))

