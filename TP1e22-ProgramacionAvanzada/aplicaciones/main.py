# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 11:58:36 2023

@author: pedro
"""
import random
import sys
from modulos.funcion import historial

frases=[]
peliculas=[]

with open('../datos/frases.txt','r') as archi:
    for linea in archi:
        frase,pelicula=linea.split(";")
        frases.append(frase)
        peliculas.append(pelicula.rstrip())



print("########################################")

print("#  "+"Peliculas: Preguntas y respuestas"+"  #")

print("########################################")

print("1 - Mostrar lista de películas.")
print("2 - ¡Trivia de película!")
print("3 - Mostrar secuencia de opciones seleccionadas previamente.")
print("4 - Borrar historial de opciones.")
print("5 - Salir")

opciones=int(input('Elige una opcion:'))

while opciones!=5:
    if opciones==1:
            print("Mostrando la lista de peliculas: ")
            print(peliculas)
            historial(opciones)
    
    if opciones==2:
        historial(opciones)
        print("Iniciando juego:")
        lista=[]
        frase=random.SystemRandom().choice(frases)
        for i in range(len(peliculas)):
            if frases[i]==frase:
                pos=i
        pelicula1=random.choice(peliculas)
        pelicula2=random.choice(peliculas)
        pelicula_ganadora=peliculas[pos]
        lista.append(pelicula1)
        lista.append(pelicula2)
        lista.append(pelicula_ganadora)
        random.shuffle(lista)
        print(frase)
        print(lista)
        print("Seleccione la opcion correcta (1,2,3):")
        opcion=int(input())
        if lista[opcion-1]==pelicula_ganadora:
            print("La opcion es correcta")
        else:
            print("La opcion es incorrecta")     
                
        
        
        
    if opciones==3:
        historial(opciones)
        print("Mostrando historial de opciones:")
        with open("historial.txt","r") as archi:
            for linea in archi:
                opcion=linea[0]
                fecha=linea[2:27]
                print("Opcion elegida:"+opcion+"//"+"En la fecha y hora:"+fecha)
            
    if opciones==4:
        print("Eliminando las opciones del historial...")
        open("historial.txt","w").close()

    
    opciones=int(input('Elige una opcion:'))
    
    if opciones==5:
        historial(opciones)
        print("¡Gracias por jugar!, Adios")
        sys.exit()