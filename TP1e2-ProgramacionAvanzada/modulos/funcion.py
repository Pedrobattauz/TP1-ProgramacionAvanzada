# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:45:45 2023

@author: pedro
"""
from datetime import datetime
def historial(opcion):
    fecha_opcion=datetime.now()
    with open("historial.txt","a") as archi:
        archi.write(str(opcion)+","+str(fecha_opcion)+"\n")
    return 
        
