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

caja = []
formas = {}
print "ESTE PROGRAMITA AGRUPA E IMPRIME LAS FORMAS QUE SALIERON POR CADA UNO DE LOS DIEZ ELEMENTOS EN COLUMNA_0"

#Creo un loop, que ennumera filas
for i,f in enumerate(fila_com):
	if i<1: #Para que no analice la fila 0, es decir, el ENCABEZADO
		continue #continue salta a la siguiente fila
	#Divide columnas en una nueva lista
	columnas = f.split(u"¬")
	#0:ID_FORMA¬1:FORMA¬2:OBSERVACION¬3:VERBO¬4:PATH_VB¬5:TOP_VERBO¬6:Causa¬7-11:F5¬F4¬F3¬F2¬F1¬12-17:S5¬S4¬S3¬S2¬S1¬18:AÑO¬19:CORPUS
	for j,celda in enumerate(columnas):
		if j!=0:continue
	#	caja.append(str(i))
		caja.append(celda)
		caja.append(columnas[1])
		

		if celda not in formas.keys():
			formas[celda]= [columnas[1]]
		elif columnas[1] not in formas[celda]:
			formas[celda].append(columnas[1])

#cuenta = collections.Counter(caja).items()
#cuenta = sorted(cuenta,key=lambda i: i[1], reverse=True)

print caja
print
#print formas
#print formas

