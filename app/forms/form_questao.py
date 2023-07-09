from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, SubmitField
from wtforms.validators import DataRequired


class CriacaoVFForm(FlaskForm):
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    resposta = SelectField(
        choices=[(True, "Verdadeiro"), (False, "Falso")],
        coerce=bool,
        validators=[DataRequired()],
    )
    nota = DecimalField(validators=[DataRequired()])
    submit = SubmitField("Criar questão")


class RespostaVFForm(FlaskForm):
    resposta = SelectField(
        choices=[(True, "Verdadeiro"), (False, "Falso")],
        coerce=bool,
        validators=[DataRequired()],
    )
    submit = SubmitField("Salvar resposta")


class CriacaoNumericoForm(FlaskForm):
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    resposta = DecimalField(validators=[DataRequired()])
    nota = DecimalField(validators=[DataRequired()])
    submit = SubmitField("Criar questão")


class RespostaNumericoForm(FlaskForm):
    resposta = DecimalField(validators=[DataRequired()])
    submit = SubmitField("Salvar resposta")


class CriacaoMultiplaEscolhaForm(FlaskForm):
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    resposta = ""
    nota = DecimalField(validators=[DataRequired()])


# class MultiplaEscolhaForm(FlaskForm):
#     enunciado = StringField('Enunciado', validators=[DataRequired()])
#     items =
