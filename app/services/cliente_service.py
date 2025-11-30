from db.bd import get_connection

def guardar_cliente(data):
    con = get_connection()
    cursor = con.cursor(dictionary=True)

    cursor.callproc("sp_setCliente", [
        data["id"],
        data["nombre"],
        data["correo"],
        data["telefono"]
    ])

    for result in cursor.stored_results():
        rows = result.fetchall()

    con.commit()
    cursor.close()
    con.close()

    return rows