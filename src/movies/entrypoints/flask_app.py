from flask import Flask, request, render_template
from movies import models
import csv

app = Flask(__name__)
models.start_mappers()

# print("Comedy: 1\nDrama: 2\nSci-Fi: 3\nRomantic: 4\nAdventure: 5")
# first = int(input("Escribe tu genero cinematografico favorito: "))
# second = int(input("Escribe tu segundo genero cinematografico favorito: "))
# third = int(input("Escribe tu tercer genero cinematografico favorito: "))

@app.route("/")
def register():
    return render_template("form.html")
    # return render_template("register.html"), 200

@app.route("/movies", methods=["POST"])
def get_movies():
    nombreUser = request.form["nombreUser"]
    first = request.form["first"]
    second = request.form["second"]
    third = request.form["third"]
    preference_key = str(int(first) * int(second) * int(third) % 5 + 1)
    lista = []
    lista_filtrada = []
    # Abrir archivo
    with open("/src/movies/movie_results.csv") as data:
        reader = csv.reader(data)
        # Cargar el archivo en una lista
        lista = list(reader)
                
    with open("/src/movies/movie_filters.csv", "w") as data:
        writer = csv.writer(data)
        # Retornar la lista
        for row in lista:
            if row[0] == preference_key:
                print(row)
                writer.writerow(row)
        writer = str(writer)
    return "<div><h1>Bienvenido " + nombreUser + ".</h1><p>Las películas de acuerdo a tus elecciones las puedes encontrar en el archivo movie_filters.csv :D</p></div>"
