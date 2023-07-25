import random

from flask import render_template, request, redirect, url_for, flash

from app import app, db
from app.forms import AddSupplierForm
from app.models import Supplier


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    msg = ""
    return render_template("index.html",
                           title="index page",
                           msg=msg)


@app.route('/get_suppliers')
def get_suppliers():
    suppliers = Supplier.query.all()
    return render_template('get_suppliers.html', title='Список поставщиков',
                           suppliers=suppliers)
    return "all"


@app.route('/add_supplier', methods=['GET', 'POST'])
def add_supplier():
    form = AddSupplierForm()
    if request.method == "POST":
        if form.validate_on_submit():
            supplier = Supplier()
            supplier.name = form.name.data
            supplier.address = form.address.data
            supplier.phone = int(form.phone.data)
            supplier.account = random.randrange(10000000000000000000,
                                                99999999999999999999)
            # todo: validate account
            try:
                db.session.add(supplier)
                db.session.commit()
            except Exception as e:
                flash('Не удалось добавить поставщика')
                print(e)
            return redirect(url_for('get_suppliers'))
    else:
        return render_template(
            'add_supplier.html', title='Добавление '
                                       'нового поставщика', form=form)

@app.route('/edit_supplier/<int:id>', methods=['GET', 'POST'])
def edit_supplier(id):
    supplier = Supplier.query.get(id)
    if not supplier:
        flash('Запрошенного на редактирование поставщика не существует')
        return redirect(url_for('get_suppliers'))
    form = AddSupplierForm()
    if request.method == "POST":
        if form.validate_on_submit():
            supplier = Supplier()
            supplier.name = form.name.data
            supplier.address = form.address.data
            supplier.phone = int(form.phone.data)
            supplier.account = int(form.account.data)

            # todo: validate account
            try:
                db.session.add(supplier)
                db.session.commit()
            except Exception as e:
                flash('Не удалось отредактировать данные поставщика')
                return redirect(url_for('get_suppliers'))
                print(e)
            flash('Данные поставщика отредактирваны')
            return redirect(url_for('edit_supplier',id = id))
    # GET method
    else:
        supplier_id = supplier.id
        form.name.data = supplier.name
        form.address.data = supplier.address
        form.phone.data = supplier.phone
        form.account.data = supplier.account

        return render_template(
            'edit_supplier.html', title='Изменение данных поставщика',
            form=form, supplier_id = supplier_id)