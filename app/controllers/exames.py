from ..app import db
from flask import Blueprint, render_template
from ..models import Exame, Questao, QuestaoExame

bp = Blueprint('criacao_exames',__name__)

@bp.route('/', methods = ['GET', 'POST'])
def index():
    return 0

# inserir questoes para testar
# tentar fazer inserir questao_exame
# tela simples -> criar/começar exame
# form criar exame

@bp.route('/create/<nome>', methods = ['GET', 'POST'])
def cria_exame(nome):
    from datetime import datetime
    questoes = [1, 2, 3]
    novo_exame = Exame(nome = nome,
                       professor = 1, # todo
                       nota = 10.0,
                       data_abertura = datetime.now(),
                       data_fechamento = datetime.now())
    db.session.add(novo_exame)
    print(novo_exame.id)
    for questao_id in questoes:
        questao_exame = QuestaoExame(exame_id = novo_exame.id,
                                    questao_id = questao_id,
                                    nota = questao_id*10)
        db.session.add(questao_exame)
    db.session.commit()

    return 0

def insere_questao():
    pass
