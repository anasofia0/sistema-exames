from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DecimalField,
    SubmitField,
    FieldList,
    FormField,
    RadioField
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
    # nota = DecimalField(validators=[DataRequired()])
    submit = SubmitField("Criar questão")


class RespostaVFForm(FlaskForm):
    resposta = RadioField(
        choices=[('True', 'Verdadeiro'), ('False', 'Falso')],
        validators=[DataRequired()]
    )
    submit = SubmitField("Próxima")


class CriacaoNumericoForm(FlaskForm):
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    resposta = DecimalField(validators=[DataRequired()])
    # nota = DecimalField(validators=[DataRequired()])
    submit = SubmitField("Criar questão")


class RespostaNumericoForm(FlaskForm):
    resposta = DecimalField(validators=[DataRequired()])
    submit = SubmitField("Próxima")


class CriacaoMultiplaEscolhaForm(FlaskForm):
    enunciado = StringField("Enunciado", validators=[DataRequired()])
    resposta = StringField(validators=[DataRequired()])  # Resposta correta
    submit = SubmitField("Criar questão")

    # def init(self, args, **kwargs):
    #     super(CriacaoMultiplaEscolhaForm, self).init(args, **kwargs)
    #     self.opcoes = FieldList(StringField('Opção', validators=[DataRequired()]), min_entries=2)


class RespostaMultiplaEscolhaForm(FlaskForm):
    resposta = RadioField(
        coerce=str, validators=[DataRequired()]
    )  # Resposta do estudante
    submit = SubmitField("Próxima")
