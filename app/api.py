from flask import Flask, request, jsonify
from app.cupones import calcular_precio_final

# inicializamos la app
app = Flask(__name__)

# creamos nuestra ruta, indicamos ruta y método a usar. POST es para enviar


@app.route('/precio', methods=['POST'])
def calcular():
    # obtenemos nuestra solicitud
    data = request.get_json()
    # separamos los datos que nos interesan
    precio = data.get("precio")
    cupon = data.get("cupon")
    impuesto = data.get("impuesto", 0.19)

    final = calcular_precio_final(precio, cupon, impuesto)
    return jsonify({"precio_final": final})
