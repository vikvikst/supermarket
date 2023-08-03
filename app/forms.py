from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, \
    SelectField, FloatField, DecimalField, DateTimeLocalField, DateField
from wtforms.validators import DataRequired, ValidationError, NumberRange, \
    Length

from app.models import ClassProduct, Measure, Product, Supplier


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

# class AddNameProductForm(FlaskForm):
#     name = StringField('Наименование товара',
#                        validators=[DataRequired(), validate_isalpha])
#     description = TextAreaField('Описание', validators=[DataRequired(), Length(
#         max=32)])
#     class_product = SelectField('Класс продукт', choices=lambda: [(r.id, r.name)
#                        for r in ClassProduct.query.all()], coerce=int)
#     measure = SelectField('Единица измерения',
#                                choices=lambda: [(r.id, r.name)
#                                                 for r in Measure.query.all()],
#                           coerce=int)
#     submit = SubmitField('Добавить')
#
class AddMeasureForm(FlaskForm):
    name = StringField('Единица измерения',
                       validators=[DataRequired(), validate_isalpha])
    description = TextAreaField('Описание', validators=[DataRequired(), Length(
                        max=32)])
    submit = SubmitField('Добавить')

class AddProductForm(FlaskForm):
    # id readonly my_field = fields.StringField('Label', render_kw={'readonly': True})
    id_classp = SelectField('Класс продукт', choices=lambda: [(r.id, r.name)
                              for r in ClassProduct.query.all()], coerce=int)
    name = StringField('Наименование товара',
                       validators=[DataRequired(), validate_isalpha])
    price_buy = DecimalField('Цена покупки',places=2)
    price_sell = DecimalField('Цена продажи',places=2)
    description = TextAreaField('Описание', validators=[DataRequired(), Length(
        max=32)])
    id_measure = SelectField('Единица измерения',
      choices=lambda: [(r.id, r.name) for r in Measure.query.all()],
      coerce=int)

    submit = SubmitField('Применить')

class AddDeliviryForm(FlaskForm):
    id_supplier = SelectField('Поставщик', choices=lambda: [(r.id, r.name)
                              for r in Supplier.query.all()], coerce=int)
    id_product = SelectField('Выбор продукта', choices=lambda: [(r.id, r.name)
                                for r in Product.query.all()], coerce=int)
    # date = DateTimeLocalField('Дата/время',
    date = DateField('Дата',
                              format='%Y-%m-%d',
                              validators=[DataRequired()])
    number = IntegerField('Количество', validators=[DataRequired(), NumberRange(
        min=1, message='Значение не может быть отрицательным')])

    submit = SubmitField('Применить')

class AddSaleForm(FlaskForm):
    id_product = SelectField('Выбор продукта', choices=lambda: [(r.id, r.name)
                                    for r in Product.query.all()], coerce=int)

    number = IntegerField('Количество', validators=[DataRequired(), NumberRange(
        min=1, message='Значение не может быть отрицательным')])

    submit = SubmitField('Применить')

class EditSaleForm(FlaskForm):
    id_product = SelectField('Выбор продукта', choices=lambda: [(r.id, r.name)
                                                                for r in Product.query.all()], coerce=int)
    date = DateField('Дата',
                     format='%Y-%m-%d',
                     validators=[DataRequired()])
    number = IntegerField('Количество', validators=[DataRequired(), NumberRange(
        min=1, message='Значение не может быть отрицательным')])

    submit = SubmitField('Применить')