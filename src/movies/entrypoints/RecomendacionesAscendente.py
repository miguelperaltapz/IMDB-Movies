'''
Esta clase de RecomendacionesAscendente genera la lista de películas recomendadas en orden ascendente,
es decir, de las má baja a la más alta, si el usuario teclea un valor de "S" para la variable order.

import csv

class RecomnedacionesAscendente():
	def generarRecomendaciones(self, lista, preference_key, cont):
		for row in reversed(lista):
                if row[0] == preference_key and cont < 10:
                    writer.writerow(row)
                    cont += 1
        return writer

'''