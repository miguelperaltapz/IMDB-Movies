from flask import Flask, request, render_template
from movies import models
import csv
#from LeerArchivos import *
#from RecomendacionesAscendente import *

app = Flask(__name__)
models.start_mappers()

@app.route("/")
def register():
    return render_template("form.html")

@app.route("/movies", methods=["POST"])
def get_movies():
    nombreUser = request.form["nombreUser"]
    first = request.form["first"]
    second = request.form["second"]
    third = request.form["third"]
    order = request.form["order"]
    preference_key = str(int(first) * int(second) * int(third) % 5 + 1)
    lista = []

    #lista = LeerArchivos.leer()

    #Leer el archivo .csv
    with open("/src/movies/movie_results.csv") as data:
        reader = csv.reader(data)
        # Cargar el archivo en una lista
        lista = list(reader)
                
    # Escribir dentro del nuevo archivo csv
    with open("/src/movies/movie_filters.csv", "w") as data:
        writer = csv.writer(data)
        cont = 0
        # Verificar si el usuario quiere el orden
        # de las peliculas de manera ascendente
        if order == "S":
            # Retornar peliculas de manera ascendente
            
            '''
            Aquí tratamos de hacer uso del patrón de diseño de SimpleFactory para generar la lista de las
            películas recomendadas según el orden que haya escogido el usuario. Si la variable order
            tiene un valor de "S", entonces se generan las recomendaciones de manera ascendente.
            '''

            #Recomendaciones recomendacionesAscendente = RecomendacionesFactory.createRecomendaciones("S")
            #recomendacionesAscendente.generarRecomendaciones(lista, preference_key, cont)

            for row in reversed(lista):
                if row[0] == preference_key and cont < 10:
                    writer.writerow(row)
                    cont += 1
        else:
            # Retornar las peliculas de manera descendente
            
            '''
            Aquí tratamos de hacer uso del patrón de diseño de SimpleFactory para generar la lista de las
            películas recomendadas según el orden que haya escogido el usuario. Si la variable order
            no tiene ningún valor, entonces se generan las recomendaciones de manera descendente.
            '''
            
            #Recomendaciones recomendacionesDescendente = RecomendacionesFactory.createRecomendaciones("")
            #recomendacionesDescendente.generarRecomendaciones(lista, preference_key, cont)
            
            for row in lista:
                if row[0] == preference_key and cont < 10:
                    writer.writerow(row)
                    cont += 1

    return "<div><h1>Bienvenido " + nombreUser + ".</h1><p>Las películas de acuerdo a tus elecciones las puedes encontrar en el archivo movie_filters.csv :D</p></div>"
