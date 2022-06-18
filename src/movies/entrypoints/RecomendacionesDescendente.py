'''
Esta clase de RecomendacionesDescendente genera la lista de películas recomendadas en orden descendente,
es decir, de la más alta a la más baja, si el usuario teclea no teclea ningún valor para la variable
order.

import csv

class RecomnedacionesDescendente():
	def generarRecomendaciones(self, lista, preference_key, cont):
		for row in lista:
                if row[0] == preference_key and cont < 10:
                    writer.writerow(row)
                    cont += 1
        return writer

'''