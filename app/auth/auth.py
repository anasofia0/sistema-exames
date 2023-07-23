from flask import Blueprint, render_template, redirect,request, url_for
from flask_login import login_required, login_user, logout_user
from .form import RegisterForm, LoginForm
from ..app import db
from ..models.user import User  

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        matricula = request.form.get("matricula")
        user = User.query.filter_by(matricula=matricula).first()
        senha = request.form.get("senha")
        remember = True if request.form.get("remember") else False

        if not user or user.senha != senha:
            print("Por favor verifique seus dados de login e tente novamente")
            return redirect(url_for("auth.login")) # Se não exisitir o usuário ou a senha estiver errada, redireciona para a página de login

        # se passar, faz o login e salva a sessão
        login_user(user, remember=remember)
        if(user.professor):
            print("Professor logado")
            return redirect(url_for("dashboards.loggedProfessor"))
        else:
            print("Aluno logado")
            return redirect(url_for("dashboards.loggedAluno"))
    return render_template("login.html", form=form)  

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        user = User(matricula = form.matricula.data,
                    nome = form.nome.data,
                    email = form.email.data,     
                    professor = form.professor.data,
                    senha = form.senha.data # poderiamos usar um hash, mas como é algo simples, não vamos nos preocupar com isso
        )
        
        db.session.add(user)
        db.session.commit()
        created_user = User.query.filter_by(email=form.email.data).first()

        if created_user:
            print("Usuário criado com sucesso!")
            print("Detalhes do usuário:", created_user)
        else:
            print("Falha ao criar usuário.")

        return redirect("/")
    
    return render_template("register.html", form=form)

@auth_bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login")) #desloga o usuário e redireciona para a página de login