# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:33:00 2023

@author: pedro
"""
import random
from flask import Flask, render_template, request
from modulos.archivos import leer_archivo, puntaje

app=Flask(__name__)
# lista_peliculas=[]

RUTA = "./datos/"
ARCHIVO = RUTA + "frases.txt"

frases,peliculas=leer_archivo(ARCHIVO)
f,p=puntaje(frases,peliculas)
try:
    leer_archivo(ARCHIVO)
except FileNotFoundError:
    with open(ARCHIVO,"w") as archi:
        pass

@app.route("/", methods=['GET', 'POST'])
def raiz():

    return render_template("home.html")

@app.route("/add",methods=['GET','POST'])
def agregar():  
    if request.method == 'POST':
        opcion=request.form['opcion']
        return render_template("add.html",frases=f,variable_opcion=opcion,lista=p)
    elif request.method == 'GET':
        return render_template("add.html", frases=f, lista=p)



if __name__ =="__main__":
    app.run(debug=False)