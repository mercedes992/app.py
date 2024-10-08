import pandas as pd
from collections import Counter

# Datos de ejemplo
data = {
    'Cliente': ['A', 'A', 'B', 'C', 'B', 'C', 'A', 'B', 'C', 'A'],
    'Producto': ['Manzanas', 'Plátanos', 'Yogurt', 'Manzanas', 'Yogurt', 'Plátanos', 'Yogurt', 'Manzanas', 'Plátanos', 'Yogurt']
}

df = pd.DataFrame(data)

def recomendar_productos(cliente_id):
    # Filtrar productos comprados por el cliente
    productos_cliente = df[df['Cliente'] == cliente_id]['Producto']

    # Calcular frecuencia de compra de cada producto
    productos_populares = dict(Counter(df['Producto']))

    # Excluir productos que el cliente ya compró
    for producto in productos_cliente:
        productos_populares.pop(producto, None)

    # Ordenar productos por frecuencia
    productos_recomendados = sorted(productos_populares, key=productos_populares.get, reverse=True)

    return productos_recomendados

from flask import Flask, request, jsonify
from recomendation import recomendar_productos

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Página principal'


app = Flask(__name__)

@app.route('/recomendar', methods=['POST'])
def recomendar():
    cliente_id = request.json.get('cliente_id')
    recomendaciones = recomendar_productos(cliente_id)
    return jsonify({'recomendaciones': recomendaciones})

if __name__ == '__main__':
    app.run(debug=True)
    
    


