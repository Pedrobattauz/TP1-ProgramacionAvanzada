# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 18:12:53 2023

@author: pedro
"""

from modulos.archivos import leer_archivo, puntaje

lista_peliculas=[]

RUTA = "./datos/"
ARCHIVO = RUTA + "frases.txt"

print(leer_archivo(ARCHIVO))