import csv

lista = []

'''Se creó la clase de LeerArchivos para pasar el método de leer, que se encargaría de recibir el
archivo .csv con la lista de películas para poder leerlo y cargarlo en la variable lista.'''

'''Se hace uso del principio de SOLID de responsabilidad única porque, en flask_app.py, nada más se está
creando una variable que representa a la lista y se manda llamar el método leer() de esta clase.
Flask_app.py desconoce la lógica para leer el archivo .csv, porque esa no es su responsabilidad, sino que
está siendo delegada a otra clase que se encargará de leer el archivo. No es necesario que sepa cómo
funciona el método, sino que simplemente lo mande llamar.'''

class LeerArchivos():
        def __init__(self):
                _;

        def leer(self):
                with open("/src/movies/movie_results.csv") as data:
                        reader = csv.reader(data)
                        # Cargar el archivo en una lista
                        lista = list(reader)
                        return lista