# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:30:40 2023

@author: pedro
"""
import random

def iniciar_trivia(archivo):
    peliculas=[]
    frases=[]
    with open('../datos/frases.txt','r') as archi:
        for linea in archi:
            frase,pelicula=linea.split(";")
            frases.append(frase)
            peliculas.append(pelicula.rstrip())
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