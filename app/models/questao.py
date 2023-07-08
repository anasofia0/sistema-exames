from . import db
from sqlalchemy import Column, String, Integer, Float, DATETIME, Enum


class TipoQuestao(Enum):
    VERDADEIRO_FALSO = "verdadeiro_falso"
    MULTIPLA_ESCOLHA = "multipla_escolha"
    ENTRADA_NUMERO = "entrada_numero"


class Questao(db.Model):
    __tablename__ = "questao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    tipo_questao = Column(TipoQuestao, nullable=False)
    enunciado = Column(String, nullable=False)
    resposta_certa = Column(String, nullable=False)

    exames = db.relationship("Exame", secondary="questao_exame", back_populates="questoes") # many to many
    resposta_alunos = db.relationship("RespostaAluno", back_populates="questao") # one to many

    # get_id method
    def get_id(self):
        return str(self.id_exame)
