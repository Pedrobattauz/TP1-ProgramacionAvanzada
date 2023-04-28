# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:25:19 2023

@author: pedro
"""

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

def porcentaje_caida(l): 
    #p=[i[1] for i in l]
    minimo=min(l);maximo=max(l)
    r=round((minimo/maximo)*100,2)
    return r

def porcentaje_repunte(l): 
#     p=[i[1] for i in l]
    minimo=min(l)
    r=round(((l[-1]-minimo)/minimo *100),2)
    return r
