from os import abort
from flask import Blueprint, render_template
from flask_login import login_required
from app.services.professor_anotation import professor_required
from ..models.resposta_aluno import RespostaAluno
from ..models.exame import Nota
from ..models.user import User

bp = Blueprint("professor", __name__)

@bp.route("/students", methods=["GET"])
@login_required
@professor_required
def listar_estudantes():
    alunos = User.query.filter_by(professor=False).all()
    return render_template("listaEstudantes.html", alunos=alunos)

@bp.route("/view_aluno/<int:matricula>", methods=["GET"])
@login_required
@professor_required
def ver_notas_aluno(matricula):
    aluno = User.query.get(matricula)
    if aluno is None:
        abort(404)
    notas = Nota.query.filter_by(matricula_aluno=matricula).all()
    dados_exame = []
    for nota in notas:
        respostas_aluno = RespostaAluno.query.filter_by(id_exame=nota.exame_id, id_aluno=matricula).all()
        dados_exame.append({
            "exame": nota.exame,
            "nota": nota,
            "respostas_aluno": respostas_aluno
        })

    return render_template("verAluno.html", aluno=aluno, dados_exame=dados_exame)
