from flask_wtf import FlaskForm
from wtforms import RadioField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class VerdadeiroFalsoForm(FlaskForm):
    answer = RadioField('Answer', choices=[('Verdadeiro', 'True'), ('Falso', 'False')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class MultiplaEscolhaForm(FlaskForm):
    answer = SelectField('Answer', choices=[], validators=[DataRequired()])  # Choices should be set dynamically based on the question
    submit = SubmitField('Submit')

class EntradaNumeroForm(FlaskForm):
    answer = StringField('Answer', validators=[DataRequired(), NumberRange()])  # You might want to set min and max for NumberRange based on the question
    submit = SubmitField('Submit')
