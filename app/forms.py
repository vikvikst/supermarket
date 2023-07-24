from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError, NumberRange

def validate_isalpha(form, field):
    if not (field.data).isalpha():
        raise ValidationError('Допустимы только буквы')

class EditUserForm(FlaskForm):
    firstname = StringField('Имя',
                            validators=[DataRequired(), validate_isalpha])
    middlename = StringField('Отчество',
                             validators=[DataRequired(), validate_isalpha])
    lastname = StringField('Фамилия',
                           validators=[DataRequired(), validate_isalpha])
    age = IntegerField('Возраст', validators=[DataRequired(), NumberRange(
        min=0, message='Значение не может быть отрицательным')])
    submit = SubmitField('Изменить')