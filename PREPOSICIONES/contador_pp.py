#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Importo paqueterías que utilizaré
import re, collections
#Defino en una variable la ruta al archivo que contiene mi texto
archivo = "/home/varinia/Dropbox/Varinia Estrada/DATOS/DATOS_REGEX/PREPOSICIONES/analisis_prep.csv"

#Abro mi archivo
file = open(archivo,"r")
#Lo leo y lo convierto a utf-8
cadena = file.read().decode('utf-8')
#Le pido que cree una lista en donde los elementos se dividen en saltos de línea
filas = cadena.split(u"\n")
#Creo un loop, que ennumera filas
for i,f in enumerate(filas):
	if i<1: continue
	columnas = f.split(u"¬")
	fila = columnas[1:4] + columnas[14:16]
	print i, fila
	