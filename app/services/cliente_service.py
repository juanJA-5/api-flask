from app.models import Cliente
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class ClienteService:

    @staticmethod
    def set_cliente(data):
        # Guardar cliente nuevo
        cliente = Cliente(
            nombre=data['nombre'],
            email=data['email'],
            password=generate_password_hash(data['password'])
        )
        db.session.add(cliente)
        db.session.commit()
        return cliente

    @staticmethod
    def login(email, password):
        cliente = Cliente.query.filter_by(email=email).first()
        if cliente and check_password_hash(cliente.password, password):
            return cliente
        return None

    @staticmethod
    def modificar_cliente(email, data):
        cliente = Cliente.query.filter_by(email=email).first()
        if cliente:
            cliente.nombre = data.get('nombre', cliente.nombre)
            if 'password' in data:
                cliente.password = generate_password_hash(data['password'])
            db.session.commit()
        return cliente

    @staticmethod
    def generar_codigo(email):
        cliente = Cliente.query.filter_by(email=email).first()
        if cliente:
            cliente.generar_codigo()
            db.session.commit()
        return cliente