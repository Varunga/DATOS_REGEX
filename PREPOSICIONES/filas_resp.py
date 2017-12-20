#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#Importo paqueterías que utilizaré
import re, collections
# Esto permite que la salida se ajuste a cualquier terminal, salida, etc.
import codecs,locale,sys
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

#_______________________________________________________________

#Defino en una variable la ruta al archivo que contiene mi texto
archivo = "analisis_reducido.csv"

#Abro mi archivo, yeah!!!
file = open(archivo,"r")

#Lo leo y lo convierto a utf-8
cadena = file.read().decode('utf-8')
#Le pido que cree una lista en donde los elementos se dividen en saltos de línea
fila_com = cadena.split(u"\n")

for i,f in enumerate(fila_com):
	if i<1:
		continue #continue significa saltar al siguiente
	#Divide columnas en una nueva lista
	columnas = f.split(u"¬")[1:]
	print i, columnas[0], '\n', columnas[1]
	print columnas[11], columnas[12], columnas[13], columnas[14], columnas[15]
