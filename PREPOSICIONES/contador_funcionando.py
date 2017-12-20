#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#Importo paqueterías que utilizaré
#Necesario para resolver problemas de codificación, el texto de salida ajusta codificación a cualquier terminal, programa, etc.
import codecs,locale,sys
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
#Necesario para regex y su ordenamiento
import re, collections


print u"ESTE PROGRAMITA AGRUPA POR CONSTRUCCIONES DONDE HUBO DESPLAZAMIENTOS (LIT O FIG) Y DA TOTALES"

#Defino en una variable la ruta al archivo que contiene mi texto
archivo = "analisis_reducido.csv"

#Abro mi archivo, yeah!!!
file = open(archivo,"r")

#Lo leo y lo convierto a utf-8
cadena = file.read().decode('utf-8')
#Le pido que cree una lista en donde los elementos se dividen en saltos de línea
fila_com = cadena.split(u"\n")
#Creo una caja para recolectar formas
#Creo un diccionario para recolectar esas formas para cada construcción
formas = {}


#Creo un loop, que ennumera filas y recorre f
for i,f in enumerate(fila_com):
	if i<1: #Para que no analice la fila 0, es decir, el ENCABEZADO
		continue #continue salta a la siguiente fila
	#Divide columnas en una nueva lista
	fila = f.split(u"¬")
	#Creo un loop que va llenando la caja (con formas) y las formas las organiza 
	for col,contenido in enumerate(fila):
		#Aquí le pido que consiere la columna 0 (correspondiente a la construcción y si no, no haga nada)
		if col!=0 : continue
		#Voy llenando la caja con el contenido de cada celda en la columna 1 (correspondiente a las formas)
		#____es el bueno // NO LO TOQUES
		#Sólo la primera vez
		if contenido not in formas.keys():
			formas[contenido]= [fila[1]]
		#Para que sigua llenando las formas
		elif fila[1] not in formas[contenido]:
			formas[contenido].append(fila[1])

#Aqui imprimo el diccionario creado> keys: contrucciones, calores: formas
#print formas

"""
#Aquí cuento y agrupo los items en caja asociados a cada construcción (formas)
contador = collections.Counter(caja).items()
#Las organizo de mayor a menor frecuencia
totales = sorted(contador,key=lambda i: i[1], reverse=True)
#Lo imprimo con acentos 
print u'\n'.join(u'{}= {}'.format(*x) for x in totales)

"""
#Aquí cuento y agrupo los items en formas asociados a cada construcción (formas)
contador = collections.Counter(formas).items()
#Las organizo de mayor a menor frecuencia
totales = sorted(contador,key=lambda i: i[1], reverse=True)
#Lo imprimo con acentos 
print u'\n\n'.join(u'{}= {}'.format(*x) for x in totales)
#"""