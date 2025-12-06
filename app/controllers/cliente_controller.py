from flask import request, jsonify
from app.services.cliente_service import ClienteService

class ClienteController:

    @staticmethod
    def setCliente():
        data = request.get_json()
        cliente = ClienteService.set_cliente(data)
        return jsonify({"id": cliente.id, "nombre": cliente.nombre, "email": cliente.email}), 201

    @staticmethod
    def getCliente():
        data = request.get_json()
        cliente = ClienteService.login(data['email'], data['password'])
        if cliente:
            return jsonify({"id": cliente.id, "nombre": cliente.nombre, "email": cliente.email}), 200
        return jsonify({"error": "Credenciales inválidas"}), 401

    @staticmethod
    def modificarCliente():
        data = request.get_json()
        cliente = ClienteService.modificar_cliente(data['email'], data)
        if cliente:
            return jsonify({"id": cliente.id, "nombre": cliente.nombre, "email": cliente.email}), 200
        return jsonify({"error": "Cliente no encontrado"}), 404

    @staticmethod
    def generarCodigo():
        data = request.get_json()
        cliente = ClienteService.generar_codigo(data['email'])
        if cliente:
            return jsonify({"email": cliente.email, "codigo": cliente.codigo}), 200
        return jsonify({"error": "Cliente no encontrado"}), 404