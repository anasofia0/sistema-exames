from flask import Blueprint, render_template,redirect, url_for
from flask_login import login_required, logout_user
from ..app import db

bp = Blueprint("dashboards", __name__)

@bp.route("/loggedAluno", methods=["GET", "POST"])
@login_required
def loggedAluno():
    return render_template("loggedAluno.html") # se o login for bem sucedido, redireciona para a dashboard

@bp.route("/loggedProfessor", methods=["GET", "POST"])
@login_required
def loggedProfessor():
    return render_template("loggedProfessor.html") # se o login for bem sucedido, redireciona para a dashboard

@bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login")) #desloga o usuário e redireciona para a página de login