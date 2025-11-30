from flask import request, jsonify
from services.cliente_service import guardar_cliente

def set_cliente():
    data = request.get_json()
    resultado = guardar_cliente(data)
    return jsonify(resultado)