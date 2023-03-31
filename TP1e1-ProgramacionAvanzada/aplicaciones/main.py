# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:35:29 2023

@author: pedro
"""
import matplotlib.pyplot as plt
from funciones import normalizacion,porcentual

gofecha=[]
goprecio=[]
with open("../datos/google.csv","r") as archi:
    archi.readline()
    for linea in archi:
        gfecha,gprecio=linea.split(",")
        gofecha.append(gfecha)
        goprecio.append(float(gprecio.rstrip()))


nikefecha=[]
nikeprecio=[]
with open("../datos/nike.csv","r") as archi:
     archi.readline()
     for linea in archi:
         nfecha,nprecio=linea.split(",")
         nikefecha.append(nfecha)
         nikeprecio.append(float(nprecio.rstrip()))



googlenormalizados=normalizacion(goprecio)
googleporcentual=porcentual(goprecio,goprecio[0])
nikenormalizados=normalizacion(nikeprecio)
nikeporcentual=porcentual(nikeprecio,nikeprecio[0])


plt.plot(googlenormalizados, color = "b", label = "Google")
plt.plot(nikenormalizados, color = "r", label = "Nike")
plt.legend(loc="lower right", fontsize = 10)
plt.xlabel("Evolucion normalizada del precio de Google y Nike")
plt.title("Precios normalizados entre 0 y 1")
plt.grid()
plt.show()

plt.plot(googleporcentual, color = "b", label = "Google")
plt.plot(nikeporcentual, color = "r", label = "Nike")
plt.legend(loc="lower right", fontsize = 10)
plt.xlabel("Evolucion porcentual del precio de Google y Nike respecto al precio inicial")
plt.title("Evolucion porcentual de los precios")
plt.show()