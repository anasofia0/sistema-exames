from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///provas.db', echo=True)
Base = declarative_base()

class Prova(Base):
    __tablename__ = 'prova'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    nota = Column(Integer)
    prazo = Column(Date)
    data = Column(Date)

class Questao(Base):
    __tablename__ = 'questao'
    id = Column(Integer, primary_key=True)
    enunciado = Column(String)
    opcao_a = Column(String)
    opcao_b = Column(String)
    opcao_c = Column(String)
    opcao_d = Column(String)

class ProvaQuestao(Base):
    __tablename__ = 'prova_questao'
    id_prova = Column(Integer, ForeignKey('prova.id'), primary_key=True)
    id_questao = Column(Integer, ForeignKey('questao.id'), primary_key=True)

    prova = relationship("Prova", backref="prova_questao")
    questao = relationship("Questao", backref="prova_questao")

Base.metadata.create_all(engine)
