import random

from flask import render_template, request, redirect, url_for, flash

from app import app, db
from app.forms import AddSupplierForm, AddClassProductForm, \
    AddMeasureForm, AddProductForm, AddDeliviryForm, AddSaleForm
from app.models import Supplier, ClassProduct, Measure, Product, Deliviry, Sale


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

@app.route('/delete_supplier/<int:id>')
def delete_user(id):
    supplier = Supplier.query.get(id)
    if not supplier:
        flash('Запрошенного поставщика не существует')
        return redirect(url_for('index'))
    try:
        db.session.delete(supplier)
        db.session.commit()
        flash('Запись удалена')
    except Exception as e:
        flash('Не удалось удалить запись')
    return redirect(url_for('get_suppliers'))


@app.route('/add_class_product', methods=['GET', 'POST'])
def add_class_product():
    form = AddClassProductForm()
    if request.method == "POST":
        if form.validate_on_submit():
            class_product = ClassProduct()
            class_product.name = form.name.data
            class_product.description = form.description.data
            try:
                db.session.add(class_product)
                db.session.commit()
            except Exception as e:
                flash('Не удалось добавить запись')
                return redirect(url_for('get_class_products'))
        return redirect(url_for('get_class_products'))
    else:
        return render_template('add_class_product.html', title='Добавление '
                                       'класса продуктов',form=form)

@app.route('/get_class_products')
def get_class_products():
    class_products = ClassProduct.query.all()
    return render_template('get_class_products.html', title='Список классов '
                                    'товаров',class_products=class_products)


@app.route('/edit_class_product/<int:id>', methods=['GET', 'POST'])
def edit_class_product(id):
    class_product = ClassProduct.query.get(id)
    if not class_product:
        flash('Запрошенной записи не существует')
        return redirect(url_for('get_class_products'))
    form = AddClassProductForm()
    if request.method == "POST":
        if form.validate_on_submit():
            class_product = ClassProduct()
            class_product.name = form.name.data
            class_product.description = form.description.data

            # todo: validate account
            try:
                db.session.add(class_product)
                db.session.commit()
            except Exception as e:
                flash('Не удалось отредактировать запись')
                return redirect(url_for('get_class_products'))
                print(e)
            flash('Запись отредактирована')
            return redirect(url_for('edit_class_product',id = id))
    # GET method
    else:
        class_product_id = class_product.id
        form.name.data = class_product.name
        form.description.data = class_product.description

        return render_template(
            'edit_class_product.html', title='Изменение данных класса продукта',
            form=form, class_product_id = class_product_id)

@app.route('/delete_class_product/<int:id>')
def delete_class_product(id):
    class_product = ClassProduct.query.get(id)
    if not class_product:
        flash('Запрошенной записи не существует')
        return redirect(url_for('get_class_products'))
    try:
        db.session.delete(class_product)
        db.session.commit()
    except Exception as e:
        flash('Не удалось удалить запись')
        return redirect(url_for('get_class_products'))
    flash('запись удалена')
    return redirect(url_for('get_class_products'))

# @app.route('/add_name_product', methods=['GET', 'POST'])
# def add_name_product():
#     form = AddNameProductForm()
#     if request.method == "POST":
#         if form.validate_on_submit():
#             name_product = NameProduct()
#             name_product.name = form.name.data
#             name_product.description = form.description.data
#             # name_product.classp = int(form.class_product.data)
#             name_product.id_measure = form.measure.data
#             classp_id = int(form.class_product.data)
#             print("if:{}".format(type(classp_id)))
#             #
#             classp = ClassProduct.query.get(classp_id)
#             try:
#                 name_product.classp.append(classp)
#                 db.session.add(name_product)
#                 db.session.commit()
#             except Exception as e:
#                 flash('Не удалось добавить запись')
#                 return redirect(url_for('get_names_products'))
#
#         return redirect(url_for('get_names_products'))
#     else:
#         return render_template('add_name_product.html', title='Добавление '
#                                                'класса продуктов',form=form)
#
# @app.route('/get_names_products')
# def get_names_products():
#     names_products = NameProduct.query.all()
#     return render_template('get_names_products.html', title='Список '
#                         'наименований товаров',names_products=names_products)
#
# @app.route('/edit_name_product/<int:id>', methods=['GET', 'POST'])
# def edit_name_product(id):
#     name_product = NameProduct.query.get(id)
#     if not name_product:
#         flash('Запрошенной записи не существует')
#         return redirect(url_for('get_names_products'))
#     class_product = name_product.classp[0]
#     form = AddNameProductForm(measure = name_product.id_measure,
#                               class_product = class_product.id)
#     if request.method == "POST":
#         if form.validate_on_submit():
#             name_product.name = form.name.data
#             name_product.description = form.description.data
#             name_product.id_measure = int(form.measure.data)
#             selected_id_class_product = int(request.form.get('class_product'))
#             if selected_id_class_product != class_product.id:
#                 try:
#                     class_product.namep.remove(name_product)
#                     # name_product.classp.remove(class_product)
#                     db.session.commit()
#                 except Exception as e:
#                     flash('Не удалось удалить запись')
#                     print(e)
#                     return redirect(url_for('get_name_products'))
#                 class_product = ClassProduct.query.get(selected_id_class_product)
#                 class_product.namep.append(name_product)
#             # return ("ffff")
#
#             # todo: validate account
#             try:
#                 db.session.add(name_product)
#                 db.session.commit()
#             except Exception as e:
#                 flash('Не удалось отредактировать запись')
#                 return redirect(url_for('get_name_products'))
#                 print(e)
#             flash('Запись отредактирована')
#             return redirect(url_for('edit_name_product',id = id))
#     # GET method
#     else:
#         name_product_id = name_product.id
#         form.name.data = name_product.name
#         form.description.data = name_product.description
#
#         return render_template(
#             'edit_name_product.html', title='Изменение данных класса продукта',
#             form=form, name_product_id = name_product_id)

# @app.route('/delete_name_product/<int:id>')
# def delete_name_product(id):
#     name_product = NameProduct.query.get(id)
#     if not name_product:
#         flash('Запрошенной записи не существует')
#         return redirect(url_for('get_names_products'))
#     try:
#         class_product = name_product.classp[0]
#         # class_product.namep.remove(name_product)
#         name_product.classp.remove(class_product)
#         db.session.commit()
#         db.session.delete(name_product)
#         db.session.commit()
#     except Exception as e:
#         flash('Не удалось удалить запись')
#         return redirect(url_for('get_names_products'))
#     flash('запись удалена')
#     return redirect(url_for('get_names_products'))

@app.route('/add_measure', methods=['GET', 'POST'])
def add_measure():
    form = AddMeasureForm()
    if request.method == "POST":
        if form.validate_on_submit():
            measure = Measure()
            measure.name = form.name.data
            measure.description = form.description.data
            #
            try:
                db.session.add(measure)
                db.session.commit()
            except Exception as e:
                flash('Не удалось добавить запись')
                return redirect(url_for('get_measures'))

        return redirect(url_for('get_measures'))
    else:
        return render_template('add_measure.html', title='Добавление '
                                          'единиц измерения',form=form)

@app.route('/get_measures')
def get_measures():
    measures = Measure.query.all()
    return render_template('get_measures.html', title='Список '
                            'единиц измерения',measures=measures)

@app.route('/edit_measure/<int:id>', methods=['GET', 'POST'])
def edit_measure(id):
    measure = Measure.query.get(id)
    if not measure:
        flash('Запрошенной записи не существует')
        return redirect(url_for('get_measures'))
    form = AddMeasureForm()
    if request.method == "POST":
        if form.validate_on_submit():
            measure.name = form.name.data
            measure.description = form.description.data

            # todo: validate account
            try:
                db.session.add(measure)
                db.session.commit()
            except Exception as e:
                flash('Не удалось отредактировать запись')
                return redirect(url_for('get_measures'))
                print(e)
            flash('Запись отредактирована')
            return redirect(url_for('edit_measure',id = id))
    # GET method
    else:
        measure_id = measure.id
        form.name.data = measure.name
        form.description.data = measure.description

        return render_template(
            'edit_measure.html', title='Изменение единицы измерения',
            form=form, measure_id = measure_id)

@app.route('/delete_measure/<int:id>')
def delete_measure(id):
    measure = Measure.query.get(id)
    if not measure:
        flash('Запрошенноой записи не существует')
        return redirect(url_for('get_measures'))
    try:
        db.session.delete(measure)
        db.session.commit()
        flash('Запись удалена')
    except Exception as e:
        flash('Не удалось удалить запись')
    return redirect(url_for('get_measures'))

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm()
    if request.method == "POST":
        if form.validate_on_submit():
            product = Product()
            product.id_classp = int(form.id_classp.data)
            product.id_measure = int(form.id_measure.data)
            product.name = form.name.data
            product.description = form.description.data
            product.price_buy = round(float(form.price_buy.data),2)
            product.price_sell = round(float(form.price_sell.data),2)
            product.id_measure = int(form.id_measure.data)
            #
            try:
                db.session.add(product)
                db.session.commit()
            except Exception as e:
                flash('Не удалось добавить запись')
                return redirect(url_for('get_products'))

        return redirect(url_for('get_products'))
    else:
        return render_template('add_product.html', title='Добавление '
                                                         'продукта',form=form)

@app.route('/get_products')
def get_products():
    products = Product.query.all()
    return render_template('get_products.html', title='Товары',
                           products=products)

@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get(id)
    if not product:
        flash('Запрошенной записи не существует')
        return redirect(url_for('get_products'))
    form = AddProductForm()
    if request.method == "POST":
        if form.validate_on_submit():
            product.id_classp = int(form.id_classp.data)
            product.id_measure = int(form.id_measure.data)
            product.name = form.name.data
            product.description = form.description.data
            product.price_buy = round(float(form.price_buy.data),2)
            product.price_sell = round(float(form.price_sell.data),2)
            product.id_measure = int(form.id_measure.data)
            # todo: validate account
            try:
                db.session.add(product)
                db.session.commit()
            except Exception as e:
                flash('Не удалось отредактировать запись')
                return redirect(url_for('get_products'))
                print(e)
            flash('Запись отредактирована')
            return redirect(url_for('edit_product',id = id))
    # GET method
    else:
        product_id = product.id
        form.id_classp.data = product.id_classp
        form.name.data = product.name
        form.price_buy.data = product.price_buy
        form.price_sell.data = product.price_sell
        form.description.data = product.description
        form.id_measure.data = product.id_measure

        return render_template(
            'edit_product.html', title='Редактирование товара',
            form=form, product_id = product_id)

@app.route('/delete_product/<int:id>')
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        flash('Запрошенноой записи не существует')
        return redirect(url_for('get_products'))
    try:
        db.session.delete(product)
        db.session.commit()
        flash('Запись удалена')
    except Exception as e:
        flash('Не удалось удалить запись')
    return redirect(url_for('get_products'))

@app.route('/add_deliviry', methods=['GET', 'POST'])
def add_deliviry():
    form = AddDeliviryForm()
    if request.method == "POST":
        if form.validate_on_submit():
            deliviry = Deliviry()
            deliviry.id_supplier = int(form.id_supplier.data)
            deliviry.id_product = int(form.id_product.data)
            deliviry.date = form.date.data
            deliviry.number = int(form.number.data)
            #
            try:
                db.session.add(deliviry)
                db.session.commit()
            except Exception as e:
                flash('Не удалось добавить запись')
                return redirect(url_for('get_deliviries'))

        return redirect(url_for('get_deliviries'))
    else:
        return render_template('add_deliviry.html', title='Добавление '
                                                         'продукта',form=form)

@app.route('/edit_deliviry/<int:id>', methods=['GET', 'POST'])
def edit_deliviry(id):
    deliviry = Deliviry.query.get(id)
    if not deliviry:
        flash('Запрошенной записи не существует')
        return redirect(url_for('get_deliviries'))
    form = AddDeliviryForm(id_suppllier = deliviry.id_supplier,
                                  id_product = deliviry.id_product)
    if request.method == "POST":
        if form.validate_on_submit():
            deliviry.id_supplier = int(form.id_supplier.data)
            deliviry.id_product = int(form.id_product.data)
            deliviry.date = form.date.data
            deliviry.number = int(form.number.data)
            #
            # todo: validate account
            try:
                db.session.add(deliviry)
                db.session.commit()
            except Exception as e:
                flash('Не удалось отредактировать запись')
                return redirect(url_for('get_deliviries'))
                print(e)
            flash('Запись отредактирована')
            return redirect(url_for('edit_deliviry',id = id))
    # GET method
    else:
        deliviry_id = deliviry.id
        form.date.data = deliviry.date
        form.number.data = deliviry.number
        form.id_supplier.data = deliviry.id_supplier
        return render_template(
            'add_deliviry.html', title='Редактирование поставки',
            form=form, deliviry_id = deliviry_id)

@app.route('/get_deliviries')
def get_deliviries():
    deliviries = Deliviry.query.all()
    # for d in deliviries:
    #     print('__________________________________________________')
    #     print(deliviries.get_supplier())
    return render_template('get_deliviries.html', title='Поставки',
                           deliviries=deliviries)

@app.route('/add_sale', methods=['GET', 'POST'])
def add_sale():
    form = AddSaleForm()
    if request.method == "POST":
        if form.validate_on_submit():
            sale = Sale()
            sale.id_product = int(form.id_product.data)
            sale.number = int(form.number.data)
            try:
                db.session.add(sale)
                db.session.commit()
            except Exception as e:
                flash('Не удалось добавить запись')
                return redirect(url_for('get_deliviries'))

        return redirect(url_for('get_deliviries'))
    else:
        return render_template('add_sale.html', title='Продажа '
                                                          'продукта',form=form)

@app.route('/get_sales')
def get_sales():
    sales = Sale.query.all()
    return render_template('get_sales.html', title='Поставки',
                           sales=sales)