from flask import Blueprint
from controllers.cliente_controller import set_cliente

cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route("/cliente", methods=["POST"])
def registrar():
    return set_cliente()