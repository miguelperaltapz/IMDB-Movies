'''

Se creó la interfaz Recomendaciones para implementar el patrón de diseño de Simple Factory. Esto nos
permite tener dos clases para las recomendaciones, pero que utilizan los mismos métodos, de tal manera
que podemos hacer uso de una fábrica para crearlos y distinguirlos por medio de un string en un switch.

interface Recomendaciones {
	def generarRecomendaciones (lista, preference_key, cont)
}

'''