from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # memoria
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Rutas
    from app.routes.cliente_route import cliente_bp
    app.register_blueprint(cliente_bp, url_prefix='/cliente')

    with app.app_context():
        db.create_all()  # crea tablas en memoria

    return app