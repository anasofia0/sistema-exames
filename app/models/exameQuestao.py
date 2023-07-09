from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from . import db

class ExameQuestao(db.Model):
    __tablename__ = 'exameQuestao'
    id_Exame = Column(Integer, ForeignKey('exame.id_exame'), primary_key=True)
    id_questao = Column(Integer, ForeignKey('questao.id'), primary_key=True)

    Exame = relationship("Exame", backref="exameQuestao")
    questao = relationship("Questao", backref="exameQuestao")
