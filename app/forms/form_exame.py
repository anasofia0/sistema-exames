from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, DecimalField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class CriaExameForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    nota = DecimalField("Nota", validators=[DataRequired()])
    data_abertura = DateTimeField("Data abertura", format="%d   /%m/%Y %H:%M:%S", validators=[DataRequired()])
    data_fechamento = DateTimeField("Data fechamento", format="%d/%m/%Y %H:%M:%S", validators=[DataRequired()])
    questoes = SelectMultipleField("Questões", coerce=int)
    submit = SubmitField("Criar exame")