from os import abort
from flask import Blueprint, render_template
from flask_login import current_user, login_required
from app.services.professor_anotation import professor_required
from ..models.resposta_aluno import RespostaAluno
from ..models.exame import Exame, Nota
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


@bp.route("/exam_grades/", methods=["GET"])
@login_required
@professor_required
def ver_provas():
    exams = Exame.query.filter_by(professor=current_user.matricula).all()
    exam_data = []
    for exam in exams:
        notas = Nota.query.filter_by(exame_id=exam.id).all()
        average_grade = sum(nota.nota for nota in notas) / len(notas) if notas else 0
        exam_data.append({
            "exam": exam,
            "average_grade": average_grade
        })
    return render_template("verProvasProfessor.html", exam_data=exam_data)

@bp.route("/exam_grades/<int:id>", methods=["GET"])
@login_required
@professor_required
def ver_notas_provas(id):
    notas = Nota.query.filter_by(exame_id=id).all()
    return render_template("notasProvaProfessor.html", notas=notas)


