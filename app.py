from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Configuración de conexión a PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

# Endpoint para consultar múltiples contadores con POST
@app.route('/mecons_query', methods=['POST'])
def mecons_query():
    data = request.json
    serial_numbers = data.get("serial_numbers")
    start_date = data.get("start_date")

    if not serial_numbers or not start_date:
        return jsonify({"error": "Los parámetros 'serial_numbers' y 'start_date' son obligatorios"}), 400

    if not isinstance(serial_numbers, list) or len(serial_numbers) == 0:
        return jsonify({"error": "serial_numbers debe ser una lista no vacía"}), 400

    conn = get_db_connection()
    cur = conn.cursor()

    query = """
        SELECT serial_number, volume, uom, timestamp 
        FROM mecons 
        WHERE serial_number = ANY(%s) AND timestamp >= %s
        ORDER BY timestamp ASC
    """
    cur.execute(query, (serial_numbers, start_date))
    mecons = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify([
        {
            "serial_number": m[0],
            "volume": float(m[1]),
            "uom": m[2],
            "timestamp": m[3].isoformat()
        }
        for m in mecons
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
