# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:35:33 2023

@author: pedro
"""

# def cargar_lista_desde_archivo(nombre_archivo,lista_peliculas):
#     with open (nombre_archivo,"r") as archi:
#         for linea in archi:
#             lista_peliculas=linea.rstrip().split(";")
#             peli={
#                 "nombre":lista_peliculas[0],
#                 "frase":lista_peliculas[1]
#                     }
#             lista_peliculas.append(peli)
#             return lista_peliculas
            
# def guardar_lista_en_archivo(nombre_archivo, lista_peliculas):  
#     with open(nombre_archivo, "w", encoding="utf-8") as archi:                
#         for peli in lista_peliculas:
#             nombre = peli["nombre"]
#             frase = peli["frase"]
#             archi.write(nombre + "," + frase + "\n" )   

# def guardar_peli_en_archivo(nombre_archivo, peli):
    
#     with open(nombre_archivo, "a") as archi:
#         archi.write(f"{peli['nombre']},{peli['autor']},\n")
        
def leer_archivo(ARCHIVO):
    frases=[]
    peliculas=[]
    with open(ARCHIVO,'r') as archi:
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
    return frase, lista
