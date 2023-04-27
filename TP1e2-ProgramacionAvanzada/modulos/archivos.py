# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:35:33 2023

@author: pedro
"""
        
def leer_archivo(ARCHIVO):
    frases=[]
    peliculas=[]
    with open(ARCHIVO,'r',encoding='utf-8') as archi:
        for linea in archi:
            frase,pelicula=linea.split(";")
            frases.append(frase)
            peliculas.append(pelicula.rstrip())
    return frases,peliculas
    

def puntaje(lista1,lista2):
    import random
    lista=[]
    frase=random.choice(lista1)
    pos=lista1.index(frase)
    pelicula1=random.choice(lista2)
    pelicula2=random.choice(lista2)
    pelicula_ganadora=lista2[pos]
    lista.append(pelicula1);lista.append(pelicula2);lista.append(pelicula_ganadora)
    random.shuffle(lista)
    ind=lista.index(pelicula_ganadora)
    return frase, lista,ind
