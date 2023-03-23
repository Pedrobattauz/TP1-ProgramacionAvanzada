# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:35:29 2023

@author: pedro
"""
gofecha=[]
goprecio=[]
with open("google.csv","r") as archi:
    archi.readline()
    for linea in archi:
        gfecha,gprecio=linea.split(",")
        gofecha.append(gfecha)
        goprecio.append(float(gprecio.rstrip()))


nikefecha=[]
nikeprecio=[]
with open("nike.csv","r") as archi:
     archi.readline()
     for linea in archi:
         nfecha,nprecio=linea.split(",")
         nikefecha.append(nfecha)
         nikeprecio.append(float(nprecio.rstrip()))

def normalizacion(lista):
    normalizados=[]
    for i in range(len(lista)):
        pnueva=(lista[i]-min(lista))/(max(lista)-min(lista))
        normalizados.append(pnueva)
    return normalizados

def porcentual(lista,ref):
    caida_porcentual=[]
    for i in range(len(lista)):
        caidaporc=((lista[i]-ref)/ref)*100
        caida_porcentual.append(caidaporc)
    return caida_porcentual


    
        