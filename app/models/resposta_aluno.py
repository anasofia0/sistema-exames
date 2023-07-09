from . import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class RespostaAluno(db.Model):
    __tablename__ = "resposta_aluno"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_exame = Column(Integer, ForeignKey("exame.id"), nullable=False)
    id_questao = Column(Integer, ForeignKey("questao.id"),  nullable=False)
    id_aluno = Column(Integer, ForeignKey("user.matricula"),  nullable=False)
    resposta = Column(String, nullable=True)
    nota = Column(Float, nullable=False)

    questao = db.relationship("Questao", back_populates="resposta_alunos")

    # get_id method
    def get_id(self):
        return str(self.id_exame)
