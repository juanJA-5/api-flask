from app import db
import random
import string

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # para login
    codigo = db.Column(db.String(6), nullable=True)

    def generar_codigo(self):
        self.codigo = ''.join(random.choices(string.digits, k=6))