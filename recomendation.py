# recommendation.py

def recomendar_productos(historial_compras):
    """
    Esta función sugiere productos basados en el historial de compras.
    Argumentos:
    - historial_compras: lista de productos comprados anteriormente.

    Retorna una lista de productos recomendados.
    """
    # Simulamos una base de datos de productos populares
    productos_disponibles = ['Manzanas', 'Plátanos', 'Yogurt', 'Naranjas', 'Fresas']
    
    # Contamos la frecuencia de cada producto en el historial
    from collections import Counter
    conteo_productos = Counter(historial_compras)
    
    # Ordenamos los productos por popularidad
    productos_populares = sorted(conteo_productos, key=conteo_productos.get, reverse=True)
    
    # Creamos la lista de recomendaciones (excluyendo productos ya comprados)
    recomendaciones = [producto for producto in productos_disponibles if producto not in historial_compras]

    # Añadimos productos populares no comprados
    recomendaciones += [producto for producto in productos_populares if producto not in recomendaciones]

    return recomendaciones[:3]  # Retornamos las tres principales recomendaciones


