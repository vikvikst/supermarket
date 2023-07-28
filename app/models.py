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

classproduct_nameproduct = db.Table('classproduct_nameproduct',
                            db.Column('id_classp', db.Integer,
                                      db.ForeignKey('class_product.id')),
                            db.Column('id_namep', db.Integer,
                                      db.ForeignKey('name_product.id')))

class ClassProduct(db.Model):
    __tablename__ = 'class_product'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(32), nullable=False)
    # id_diver = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='cascade'))
    # client = db.relationship(
    #     'User', secondary=client_instructor,
    #     primaryjoin=(client_instructor.c.id_client == id),
    #     secondaryjoin=(client_instructor.c.id_instructor == id),
    #     backref=db.backref('client_instructor', lazy='dynamic'), lazy='dynamic')

    namep = db.relationship(
        'NameProduct', secondary=classproduct_nameproduct,
        backref=db.backref('classes', lazy='dynamic'),single_parent=True,
        cascade="all, delete, delete-orphan",lazy='dynamic')

    def __repr__(self):
        return "<{}:{}:{}>".format(self.id,
                                         self.name,
                                         self.description)


class NameProduct(db.Model):
    __tablename__ = 'name_product'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(32), nullable=False)
    # id_diver = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='cascade'))

    classp = db.relationship(
            'ClassProduct', secondary=classproduct_nameproduct,
            backref=db.backref('names', lazy='dynamic'),single_parent=True,
            cascade="all, delete, delete-orphan",lazy='dynamic')
    def is_attach_namep_to_classp(self, namep):
        return self.classp.filter(
            classproduct_nameproduct.c.id_classp == namep.id).count() > 0

    def attach_namep_to_classp(self, namep):
        if not self.is_attach_namep_to_classp(namep):
            self.classp.append(namep)
            return namep

    def detach_namep_to_classp(self, namep):
        if self.is_attach_namep_to_classp(namep):
            self.followed.remove(namep)

    def __repr__(self):
        return "<{}:{}:{}>".format(self.id,
                                   self.name,
                                   self.description)
