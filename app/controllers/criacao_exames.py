from flask import Blueprint, render_template
from ..models import Exame

bp = Blueprint('criacao_exames',__name__)

@bp.route('/', methods = ['GET', 'POST'])
def index():
    return 0

@bp.route('/create', methods = ['GET', 'POST'])
def cria_exame():
    return 0

def insere_questao():
    pass
