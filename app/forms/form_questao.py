from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DecimalField,
    SubmitField,
    FieldList,
    FormField,
)
from wtforms.validators import DataRequired


class OpcaoForm(FlaskForm):
    value = StringField("Value", validators=[DataRequired()])
    label = StringField("Label", validators=[DataRequired()])


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


class CriacaoMultiplaEscolhaForm(FlaskForm):
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    resposta = StringField("Resposta", validators=[DataRequired()])  # Resposta correta
    opcoes = FieldList(FormField(OpcaoForm), min_entries=1)  # Opcoes de resposta
    nota = DecimalField(validators=[DataRequired()])
    submit = SubmitField("Criar questão")


class RespostaMultiplaEscolhaForm(FlaskForm):
    resposta = SelectField(
        "Resposta", coerce=str, validators=[DataRequired()]
    )  # Resposta do estudante
    submit = SubmitField("Salvar resposta")
