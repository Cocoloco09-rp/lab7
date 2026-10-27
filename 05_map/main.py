"""EJERCICIO 05 — Subtotales de pedidos

ENUNCIADO
Cada pedido es una tupla (producto, precio_unitario, cantidad).
Usa map con lambda para calcular precio_unitario * cantidad de cada pedido.
Devuelve una lista en el orden original. Convierte el resultado de map con list.
No uses ciclos ni comprensiones. Los valores son enteros no negativos.
Para [] devuelve [].

Entrada: [("cafe", 10, 2), ("te", 8, 3), ("torta", 25, 1)]
Resultado esperado: [20, 24, 25]

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 05".
"""

def calcular_subtotales(pedidos):
   entrada = [(precio_unitario * cantidad) for _, precio_unitario, cantidad in pedidos]
   return list(map(lambda x: x, entrada))


# Ejemplo de uso: inicialmente imprime None porque falta la implementación.
pedidos = [("cafe", 10, 2), ("te", 8, 3), ("torta", 25, 1)]
print(calcular_subtotales(pedidos))

pedidos2 = [("pan", 5, 2), ("leche", 2, 3)]
print(calcular_subtotales(pedidos2))  # Esperado: [10, 6]
