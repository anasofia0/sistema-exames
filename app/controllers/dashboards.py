from flask import Blueprint, render_template,redirect, url_for
from flask_login import login_required, logout_user
from ..app import db

bp = Blueprint("dashboards", __name__)

@bp.route("/logged/aluno", methods=["GET", "POST"])
@login_required
def loggedAluno():
    return render_template("loggedAluno.html") # se o login for bem sucedido, redireciona para a dashboard

@bp.route("/logged/professor", methods=["GET", "POST"])
@login_required
def loggedProfessor():
    return render_template("loggedProfessor.html") # se o login for bem sucedido, redireciona para a dashboard

