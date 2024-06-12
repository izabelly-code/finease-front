from models import db

from datetime import datetime


class Gasto(db.Model):
    __tablename__ = "gastos"
    id_payment = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    value = db.Column(db.Float(), nullable=False)
    date_payment = db.Column(db.Date(), nullable=False, default=datetime.today())


    def insert_gasto(name, value, date_payment):
        gasto = Gasto(name=name, value=value, date_payment=date_payment)
        db.session.add(gasto)
        db.session.commit()
        return gasto


    def get_payment(id_payment):
        payment = Gasto.query.filter_by(id_payment=id_payment).first()
        return payment


    def get_payments():
        payments = Gasto.query.all()
        return payments
