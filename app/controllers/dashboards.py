from flask import Blueprint, render_template, redirect,request, url_for, flash
from flask_login import login_required, login_user
from ..auth.form import RegisterForm, LoginForm
from ..app import db
from ..models.user import User 

bp = Blueprint("dashboards", __name__)

@bp.route("/loggedAluno", methods=["GET", "POST"])
@login_required
def loggedAluno():
    return render_template("loggedAluno.html") # se o login for bem sucedido, redireciona para a dashboard

@bp.route("/loggedProfessor", methods=["GET", "POST"])
@login_required
def loggedAluno():
    return render_template("loggedProfessor.html") # se o login for bem sucedido, redireciona para a dashboard