from app.app import db
def tabelas():
    from .exame import Exame
    from .user import User
    from .questao import Questao
    from .exameQuestao import ExameQuestao
    return [Exame, User, Questao, ExameQuestao]