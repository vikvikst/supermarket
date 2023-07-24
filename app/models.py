from app import db


class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    address = db.Column(db.String(32), nullable=False)
    phone = db.Column(db.Integer(), nullable=False)
    account = db.Column(db.Integer(), nullable=False)

    lakeworkout = db.relationship('LakeWorkout', backref='lake', lazy=True)