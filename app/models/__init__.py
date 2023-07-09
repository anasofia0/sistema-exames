<<<<<<< HEAD
from app.app import db
def tabelas():
    from .exame import Exame
    from .user import User
    from .questao import Questao
    from .exameQuestao import ExameQuestao
    return [Exame, User, Questao, ExameQuestao]
=======
from ..app import db
from .exame import Exame, QuestaoExame
from .questao import Questao
from .user import User
from .resposta_aluno import RespostaAluno
>>>>>>> origin/criacao-exames
