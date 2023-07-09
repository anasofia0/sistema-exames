from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class CriaExameForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired])
    nota = DecimalField("Nota", validators=[DataRequired])
    data_abertura = DateTimeField("Data abertura", format="%d/%m/%Y %H:%M:%S", validators=[DataRequired])
    data_fechamento = DateTimeField("Data fechamento", format="%d/%m/%Y %H:%M:%S", validators=[DataRequired])
    submit = SubmitField("Criar exame")

class SelecionaQuestaoForm(FlaskForm):
    pass