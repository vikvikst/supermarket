from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError, NumberRange, \
    Length


def validate_isalpha(form, field):
    if not (field.data).isalpha():
        raise ValidationError('Допустимы только буквы')

class AddSupplierForm(FlaskForm):
    name = StringField('Наименование фирмы поставщика', validators=[
        DataRequired(), Length(max=32)])
    address = StringField('Адрес', validators=[DataRequired(), Length(
        max=32)])
    phone = IntegerField('Телефон', validators=[DataRequired(), NumberRange(
        min=0, message='Значение не может быть отрицательным')])
    account = IntegerField('Расчетный счет', validators=[DataRequired(),
                                                     NumberRange(
        min=0,max=99999999999999999999, message='Значение не может быть '
                                        'отрицательным')])
    submit = SubmitField('Применить')

class AddClassProductForm(FlaskForm):
    name = StringField('Имя класса товаров',
                       validators=[DataRequired(), validate_isalpha])
    description = StringField('Описание', validators=[DataRequired(), Length(
        max=32)])
    submit = SubmitField('Добавить')

class AddNameProductForm(FlaskForm):
    name = StringField('Наименование товаро',
                       validators=[DataRequired(), validate_isalpha])
    description = StringField('Описание', validators=[DataRequired(), Length(
        max=32)])
    submit = SubmitField('Добавить')