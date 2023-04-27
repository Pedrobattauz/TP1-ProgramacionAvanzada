# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:33:00 2023

@author: pedro
"""
from flask import Flask, render_template, request
from modulos.archivos import leer_archivo, puntaje
app=Flask(__name__)

RUTA = "./datos/"
ARCHIVO = RUTA + "frases.txt"
ARCHIVO_USUARIOS = RUTA + "usuarios.txt"
punt=0
frases,peliculas=leer_archivo(ARCHIVO)

jugadores = {

 }
usuarios=[]
puntajes=[]
try:
    leer_archivo(ARCHIVO)
except FileNotFoundError:
    with open(ARCHIVO,"w") as archi:
        pass

@app.route("/", methods=['GET', 'POST'])
def raiz():
    global punt
    if request.method == 'POST':
        usuario = request.form['nombre']
        usuarios.append(usuario)
    elif request.method== 'GET':
        if request.form.get('finalizar')=="true":
            # print(request.form["finalizar"])
            usuario = request.form['nombre']
            # Escribir los datos del usuario en el archivo "usuarios.txt"
            datos_usuario = usuarios + str(punt)
            print(datos_usuario)
            with open(ARCHIVO_USUARIOS, "a") as f:
                f.write(datos_usuario + "\n")
            # Redirigir al usuario a la página principal
    return render_template("home.html")

    #     # Guardar el usuario en un archivo
    #     with open(ARCHIVO_USUARIOS, "a") as f:
    #         f.write(usuario + "\n")
    #     return render_template("home.html", usuario=usuario)
    # return render_template("home.html")


@app.route("/add", methods=['GET', 'POST'])
def agregar():
    global punt
    f, p, ind = puntaje(frases, peliculas)

    if request.method == 'POST':
        global index
        opcion = int(request.form['opcion'])

        if index == (opcion - 1):
            n = "opcion correcta"
            index = ind
            punt += 1  # incrementa el puntaje en 1
        else:
            n = "opcion incorrecta"
            index = ind
         
        return render_template("add.html", f=f, variable_opcion=opcion, p=p, n_variable=n, punt_variable=punt,usuarios=usuarios)

    elif request.method == 'GET':
        index = ind
        return render_template("add.html", f=f, p=p)



@app.route("/add2",methods=['GET','POST'])
def historial():
    return render_template('add2.html', punt_variable=punt, usuarios=usuarios)
        

if __name__ =="__main__":
    app.run(debug=False)