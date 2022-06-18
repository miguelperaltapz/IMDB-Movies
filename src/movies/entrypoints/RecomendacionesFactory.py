'''
Se creó la clase RecomendacionesFactory para implementar el patrón de diseño de Simple Factory.
Esto nos permite tener dos clases para las recomendaciones según el orden de las reseñas que ingrese el
usuario, pero que utilizan los mismos métodos, de tal manera que podemos hacer uso de una fábrica para
crearlos y distinguirlos por medio de un string en un switch.

También se hace uso del principio de SOLID de sustitución de Liskov porque RecomendacionesFactory puede
aceptar todo tipo de órdenes de recomendación de las películas sin importar su tipo. En caso de que
creáramos una clase nueva para las recomendaciones, como lo podría ser RecomendacionesAleatorias, solo
tendríamos que agregarla a la clase de RecomendacionesFactory con su string correspondiente en el switch,
ya que haría uso de los mismos métodos.

class RecomnedacionesFactory():
	def createRecomendaciones(order):
		switch (order) {
            case "S":
                return new RecomnedacionesAscendente()
            default:
                return new RecomnedacionesDescendente()
        }
'''