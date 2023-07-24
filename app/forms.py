from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError, NumberRange, \
    Length


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

class AddSupplierForm(FlaskForm):
    name = StringField('Наименование фирмы поставщика', validators=[
        DataRequired(), Length(max=32)])
    description = StringField('Описание', validators=[DataRequired(), Length(
        max=32)])
    address = StringField('Адрес', validators=[DataRequired(), Length(
        max=32)])
    phone = IntegerField('Телефон', validators=[DataRequired(), NumberRange(
        min=0, message='Значение не может быть отрицательным')])
    account = IntegerField('Расчетный счет', validators=[DataRequired(),
                                                     NumberRange(
        min=0, message='Значение не может быть отрицательным')])
    submit = SubmitField('Добавить')