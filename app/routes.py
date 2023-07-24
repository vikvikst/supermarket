import random

from flask import render_template, request, redirect, url_for, flash

from app import app, db
from app.forms import AddSupplierForm
from app.models import Supplier


@app.route('/', methods=['GET', 'POST'])
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
            supplier.phone = form.phone.data
            supplier.account = random.randrange(10000000000000000000,
                                                99999999999999999999)
            try:
                db.session.add(supplier)
                db.session.commit()
            except Exception as e:
                flash('Не удалось добавить поставщика')
            return redirect(url_for('get_suppliers'))
    else:
        return render_template(
            'add_supplier.html', title='Добавление '
                                       'нового поставщика', form=form)
