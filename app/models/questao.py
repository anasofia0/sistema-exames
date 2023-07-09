from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from . import db

class Questao(db.Model):
    __tablename__ = 'questao'
    id = Column(Integer, primary_key=True)
    enunciado = Column(String)
    opcao_a = Column(String)
    opcao_b = Column(String)
    opcao_c = Column(String)
    opcao_d = Column(String)
