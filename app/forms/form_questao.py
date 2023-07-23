from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DecimalField,
    SubmitField,
    RadioField,
    BooleanField
)
from wtforms.validators import DataRequired


# class OpcaoForm(FlaskForm):
#     value = StringField("Value", validators=[DataRequired()])
#     label = StringField("Label", validators=[DataRequired()])


class CriacaoVFForm(FlaskForm):
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    resposta = RadioField(
        choices=[(True, "Verdadeiro"), (False, "Falso")],
        coerce=bool,
        validators=[DataRequired()],
    )
    # nota = DecimalField(validators=[DataRequired()])
    submit = SubmitField("Criar questão")


class EditaVFForm(FlaskForm):
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    resposta = RadioField(
        choices=[('True', 'Verdadeiro'), ('False', 'Falso')],
        validators=[DataRequired()]
    )
    habilitada = BooleanField()
    submit = SubmitField("Salvar questão")


class RespostaVFForm(FlaskForm):
    resposta = RadioField(
        choices=[('True', 'Verdadeiro'), ('False', 'Falso')],
        validators=[DataRequired()]
    )
    submit = SubmitField("Próxima")


class CriacaoNumericoForm(FlaskForm):
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    resposta = DecimalField(validators=[DataRequired()])
    submit = SubmitField("Criar questão")

class EditaNumericoForm(FlaskForm):
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    resposta = DecimalField(validators=[DataRequired()])
    habilitada = BooleanField()
    submit = SubmitField("Salvar questão")


class RespostaNumericoForm(FlaskForm):
    resposta = DecimalField(validators=[DataRequired()])
    submit = SubmitField("Próxima")


class CriacaoMultiplaEscolhaForm(FlaskForm):
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    resposta = StringField(validators=[DataRequired()])  # Resposta correta
    submit = SubmitField("Criar questão")


class EditaMultiplaEscolhaForm(FlaskForm):
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    resposta = StringField(validators=[DataRequired()])  # Resposta correta
    habilitada = BooleanField()
    submit = SubmitField("Salvar questão")


class RespostaMultiplaEscolhaForm(FlaskForm):
    resposta = RadioField(
        coerce=str, validators=[DataRequired()]
    )  # Resposta do estudante
    submit = SubmitField("Próxima")
