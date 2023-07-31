from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, \
    SelectField, FloatField, DecimalField
from wtforms.validators import DataRequired, ValidationError, NumberRange, \
    Length

from app.models import ClassProduct, NameProduct, Measure


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
    description = TextAreaField('Описание', validators=[DataRequired(), Length(
        max=32)])
    submit = SubmitField('Добавить')

class AddNameProductForm(FlaskForm):
    name = StringField('Наименование товара',
                       validators=[DataRequired(), validate_isalpha])
    description = TextAreaField('Описание', validators=[DataRequired(), Length(
        max=32)])
    class_product = SelectField('Класс продукт', choices=lambda: [(r.id, r.name)
                       for r in ClassProduct.query.all()], coerce=int)
    submit = SubmitField('Добавить')

class AddMeasureForm(FlaskForm):
    name = StringField('Единица измерения',
                       validators=[DataRequired(), validate_isalpha])
    description = TextAreaField('Описание', validators=[DataRequired(), Length(
                        max=32)])
    submit = SubmitField('Добавить')

class AddProductForm(FlaskForm):
    name = StringField('Наименование товара',
                       validators=[DataRequired(), validate_isalpha])
    description = TextAreaField('Описание', validators=[DataRequired(), Length(
        max=32)])
    name_product = SelectField('Наименование товара',
                                choices=lambda: [(r.id, r.name)
                                for r in NameProduct.query.all()], coerce=int)
    price_buy = DecimalField('Цена покупки',places=2)
    price_sell = DecimalField('Цена продажи',places=2)
    # price_sell = FloatField('Цена продажи', validators=[DataRequired()])
    phone = IntegerField('Количество', validators=[DataRequired(), NumberRange(
        min=0, message='Значение не может быть отрицательным')])
    submit = SubmitField('Добавить')
