from datetime import datetime

from app import db


class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    address = db.Column(db.String(32), nullable=False)
    phone = db.Column(db.Integer(), nullable=False)
    account = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return "<{}:{}:{}:{}:{}>".format(self.id,
                                         self.name,
                                         self.address,
                                         self.phone,
                                         self.account)
    # def is_client(self):
    #     return User.query.filter(self.role_client == True).count() > 0
    # def get_my_clients(self):
    #     return User.query.join(client_instructor,
    #                            (client_instructor.c.id_client == User.id)). \
    #         filter(client_instructor.c.id_instructor == self.id)
    #
    # @staticmethod
    # def get_all_instructors():
    #     return User.query.filter_by(role_instructor=True).all()

# classproduct_product = db.Table('classproduct_product',
#                             db.Column('id_classp', db.Integer,
#                                       db.ForeignKey('class_product.id')),
#                             db.Column('id_product', db.Integer,
#                                       db.ForeignKey('product.id')))

class ClassProduct(db.Model):
    __tablename__ = 'class_product'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(32), nullable=False)

    # products = db.relationship(
    #     'Product', secondary=classproduct_product,
    #     backref=db.backref('classes', lazy='dynamic'), lazy='dynamic')
    #     # backref=db.backref('classes', lazy='dynamic'),single_parent=True,
    #     # cascade="all, delete, delete-orphan",lazy='dynamic')

    def __repr__(self):
        return "<{}:{}:{}>".format(self.id,
                                         self.name,
                                         self.description)

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer(), primary_key=True)
    id_classp = db.Column(db.Integer, db.ForeignKey('class_product.id'))
    id_measure = db.Column(db.Integer, db.ForeignKey('measure.id'))
    name = db.Column(db.String(32), nullable=False)
    price_buy = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    price_sell = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    description = db.Column(db.String(32), nullable=False)

    # classp = db.relationship(
    #     'ClassProduct', secondary=classproduct_product,
    #     backref=db.backref('names', lazy='dynamic'), lazy='dynamic')
    # # backref=db.backref('names', lazy='dynamic'),single_parent=True,
    # # cascade="all, delete, delete-orphan",lazy='dynamic')

    def __repr__(self):
        return "<{}:{}:{}:{}:{}:{}>".format(self.id,
                                         self.name,
                                         self.price_buy,
                                         self.price_sell,
                                         self.number,
                                         self.id_measure)


# class NameProduct(db.Model):
#     __tablename__ = 'name_product'
#     id = db.Column(db.Integer(), primary_key=True)
#     products = db.relationship('Product', backref='namep', lazy=True)
#     name = db.Column(db.String(32), nullable=False)
#     description = db.Column(db.String(32), nullable=False)
#     id_measure = db.Column(db.Integer, db.ForeignKey('measure.id'))
#     # id_diver = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='cascade'))
#
#     classp = db.relationship(
#             'ClassProduct', secondary=classproduct_nameproduct,
#         backref=db.backref('names', lazy='dynamic'), lazy='dynamic')
#             # backref=db.backref('names', lazy='dynamic'),single_parent=True,
#             # cascade="all, delete, delete-orphan",lazy='dynamic')
#     def get_id_classp_for_namep(self):
#         # a =  ClassProduct.query.join(
#         #     classproduct_nameproduct, (classproduct_nameproduct.c.id_namep ==
#         #                                self.id)).first()
#         a = self.classp
#         # for i in a:
#         print(a[0].id)
#         # print(a)
#         return 2

    # def is_attach_namep_to_classp(self, namep):
    #     return self.classp.filter(
    #         classproduct_nameproduct.c.id_classp == namep.id).count() > 0
    #
    # def attach_namep_to_classp(self, namep):
    #     if not self.is_attach_namep_to_classp(namep):
    #         self.classp.append(namep)
    #         return namep
    #
    # def detach_namep_to_classp(self, namep):
    #     if self.is_attach_namep_to_classp(namep):
    #         self.followed.remove(namep)
    #
    # def __repr__(self):
    #     return "<{}:{}:{}>".format(self.id,
    #                                self.name,
    #                                self.description)



class Measure(db.Model):
    __tablename__ = 'measure'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(32), nullable=False)
    products = db.relationship('Product', backref='measures', lazy=True)
    def __repr__(self):
        return "<{}:{}:{}>".format(self.id,
                                   self.name,
                                    self.description)
class Deliviry(db.Model):
    __tablename__ = 'deliviry'
    id = db.Column(db.Integer(), primary_key=True)
    # id_classp = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    id_supplier = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    id_product = db.Column(db.Integer, db.ForeignKey('product.id'))
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    number = db.Column(db.Integer, nullable=False)
    supplier = db.relationship('Supplier', backref='measures', lazy=True)
    product = db.relationship('Product', backref='deliviry', lazy=True)

    def __repr__(self):
        return "<{}:{}:{}:{}:{}>".format(self.id,
                                         self.id_supplier,
                                         self.id_product,
                                         self.date,
                                         self.number)

class Sale(db.Model):
    __tablename__ = 'sale'
    id = db.Column(db.Integer(), primary_key=True)
    id_product = db.Column(db.Integer, db.ForeignKey('product.id'))
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    number = db.Column(db.Integer, nullable=False)
    product = db.relationship('Product', backref='sales', lazy=True)

    def __repr__(self):
        return "<{}:{}:{}:{}:{}>".format(self.id,
                                         self.id_product,
                                         self.date,
                                         self.number)