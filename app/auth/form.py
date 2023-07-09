from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import (DataRequired, Email, Length, Optional, Regexp,
                                ValidationError, InputRequired)


class ProfessorCodeCheck:
    def __init__(self, message=None):
        if not message:
            message = "Codigo incorreto fornecido"
        self.message = message

    def __call__(self, form, field):
        if form.professor.data and (not field.data or field.data != 'debugmode'):
            raise ValidationError(self.message)


class RegisterForm(FlaskForm):
    # Your existing fields...
    nome = StringField(
        "Nome", 
        validators=[
            DataRequired(),
            InputRequired(),
            Length(1, 50, message="Nome com no mínimo 1 e máximo de 50 caracteres")
        ], render_kw={"placeholder": "Nome"}
    )
    matricula = StringField(
        "Matricula",
        validators=[
            DataRequired(),
            Regexp("\d", message="Matrícula deve conter somente digitos numéricos"),
            InputRequired()
        ],render_kw={"placeholder": "Matricula"}
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(), 
            Email(message="Inserir endereço de e-mail válido"), 
            InputRequired()
        ],render_kw={"placeholder": "Email"}
    )
    senha = PasswordField(
        "Senha",
        validators=[
            DataRequired(),
            Length(6, 20, message="Senhas com no mínimo 6 caracteres e máximo 20",),
            InputRequired()
        ], render_kw={"placeholder": "Senha"}
    )
    professor = BooleanField("Professor")
    professor_code = StringField(
        "Codigo do professor", 
        validators=[Optional(), ProfessorCodeCheck()],
        render_kw={"placeholder": "codigo do professor"}
    )
    submit = SubmitField("Criar usuário")

class LoginForm(FlaskForm):
    matricula = StringField(
        "matricula",
        validators=[
            DataRequired(),
            Regexp("\d", message="Matrícula deve conter somente digitos numéricos"),
        ],
    )
    senha = PasswordField(
        validators=[
            DataRequired(),
            Length(
                min=6, max=20, message="Senhas com no mínimo 6 caracteres e máximo 20"
            ),
        ]
    )
    submit = SubmitField('Entrar')
