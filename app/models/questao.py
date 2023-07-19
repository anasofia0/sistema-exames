import enum
from . import db
from sqlalchemy import Column, String, Integer, Enum, PickleType


class TipoQuestao(enum.Enum):
    VERDADEIRO_FALSO = "verdadeiro_falso"
    MULTIPLA_ESCOLHA = "multipla_escolha"
    ENTRADA_NUMERO = "entrada_numero"


class Questao(db.Model):
    __tablename__ = "questao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    matricula_professor = Column(Integer, nullable=False)
    tipo_questao = Column(Enum(TipoQuestao), nullable=False)
    enunciado = Column(String, nullable=False)
    resposta_certa = Column(String, nullable=False)
    opcoes = Column(PickleType, nullable=True)  # Novo campo para salvar as opções de uma questão de múltipla escolha

    exames = db.relationship("Exame", secondary="questao_exame", back_populates="questoes") # many to many
    resposta_alunos = db.relationship("RespostaAluno", back_populates="questao") # one to many

    # get_id method
    def get_id(self):
        return str(self.id)