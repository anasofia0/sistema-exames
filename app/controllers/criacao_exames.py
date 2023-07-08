from ..app import db
from flask import Blueprint, render_template
from ..models import Exame, Questao

bp = Blueprint('criacao_exames',__name__)

@bp.route('/', methods = ['GET', 'POST'])
def index():
    return 0

#fazer um de cada vez

@bp.route('/create/<nome>', methods = ['GET', 'POST'])
def cria_exame(nome):
    from datetime import datetime
    novo_exame = Exame(nome = nome,
                       professor = 1,
                       nota = 10.0,
                       data_abertura = datetime.now(),
                       data_fechamento = datetime.now())
    db.session.add(novo_exame)
    db.session.commit()
    return 0

def insere_questao():
    pass
