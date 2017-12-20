#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#Importo paqueterías que utilizaré
#Necesario para resolver problemas de codificación, el texto de salida ajusta codificación a cualquier terminal, programa, etc.
import codecs,locale,sys
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
#Necesario para regex y su ordenamiento
import re, collections

#Defino en una variable la ruta al archivo que contiene mi texto
archivo = "analisis_reducido.csv"

#Abro mi archivo, yeah!!!
file = open(archivo,"r")

#Lo leo y lo convierto a utf-8
cadena = file.read().decode('utf-8')
#Le pido que cree una lista en donde los elementos se dividen en saltos de línea
fila_com = cadena.split(u"\n")
#Creo un diccionario para recolectar esas formas para cada construcción
caja = []
formas = {}
formasres = {}
ejemplos = {}
diccionario = {}
"""
###CREA UN LISTADO DE FORMAS Y DA SUS TOTALES EN BRUTO, SOLO DE MAYOR A MENOR SIN ORGANIZAR CONSTRUCCIONES
print u"ESTE PROGRAMITA DA TOTALES PARA CADA FORMA"
#Creo un loop, que ennumera filas y recorre f
for i,f in enumerate(fila_com):
	if i<1: #Para que no analice la fila 0, es decir, el ENCABEZADO
		continue #continue salta a la siguiente fila
	#Divide columnas en una nueva lista
	columnas = f.split(u"¬")
	#Creo un loop que va llenando la caja (con formas) y las formas las organiza 
	for j,celda in enumerate(columnas):
		if j!=0:continue
		caja.append(columnas[1])
contador = collections.Counter(caja).items()
#Las organizo de mayor a menor frecuencia
totales = sorted(contador,key=lambda i: i[1], reverse=True)
#Lo imprimo con acentos 
print u'\n'.join(u'{}= {}'.format(*x) for x in totales)
	#______________________________________________________Aqui termina el contador que solo dice que formas aparecieron pero no cuantas veces

"""
"""
###Este funciona para contar cada una de las veces que aparecio una forma
print u"ESTE PROGRAMITA DA TOTALES PARA CADA CONSTRUCCION Y FORMA"
for i,f in enumerate(fila_com):
	if i<1: #Para que no analice la fila 0, es decir, el ENCABEZADO
		continue #continue salta a la siguiente fila
	#Divide columnas en una nueva lista
	columna = f.split(u"¬")
	#Creo un loop que va llenando la caja (con formas) y las formas las organiza 
	for col,contenido in enumerate(columna):
		#FORMAS: Aquí le pido que solo consiere la columna 0 (correspondiente a la construcción)
		if col!=0 : continue
		#Voy llenando las variables: foras es un diccionario y cajas es una lista.
		if contenido not in formas.keys():
			formas[contenido]= [columna[1]]
		#Para que sigua llenando las formas
		else:
			formas[contenido].append(columna[1])
#Aquí le pido que cuente los items dentro del diccionario 'formas' y los organice
for clave, valor in formas.iteritems(): 
	cajitas = collections.Counter(valor).items()
	totales = sorted(cajitas,key=lambda i: i[1], reverse=True)
	print u'\n', u'CONSTRUCCIÓN:', clave, ':', u'Variantes:', len(totales), u'Observaciones:', len(valor)
	print u'\n'.join(u'{}= {}'.format(*x) for x in totales)
print u'\n', u'Observaciones totales:', i, u'\n', u'CONSTRUCCIONES TOTALES:', len(str(clave)), '\n', u'LISTADO DE CONSTRUCCIONES:', formas.keys()
#______________________________________________________Aqui termina el contador fino
#"""
"""
###AQUI ENCUENTRO E IMPRIMO EJEMPLOS PARA CADA FORMA
for i,f in enumerate(fila_com):
	if i<1: #Para que no analice la fila 0, es decir, el ENCABEZADO
		continue #continue salta a la siguiente fila
	#Divide columnas en una nueva lista
	fila = f.split(u"¬")
	#Creo un loop que va llenando la caja (con formas) y las formas las organiza 
	for busca,ejem in enumerate(fila):
		#FORMAS: Aquí le pido que solo consiere la columna 0 (correspondiente a la construcción)
		if busca!=1: continue
		#Voy llenando las variables: formas es un diccionario y cajas es una lista.
		if ejem not in ejemplos.keys():
			ejemplos[ejem]= [fila[2]]
		#Para que sigua llenando las formas
		else: continue
for llave, vale in ejemplos.iteritems(): 
	print u'\n', llave
	print u'\n'.join(vale)
#________________________________________________________Aqui termina el ejemplificador"
#"""

"""
# DICCIONARIO DE CONSTRUCCIONES>>FORMAS>>EJEMPLOS
for i,f in enumerate(fila_com):
	if i<1: #Para que no analice la fila 0, es decir, el ENCABEZADO
		continue #continue salta a la siguiente fila
	#Divide columnas en una nueva lista
	columna = f.split(u"¬")


#Aqui lleno formas
	for col,contenido in enumerate(columna):
		if col>0 :continue 
		if contenido not in formas.keys():
			formas[contenido]=[columna[1]]
		else: 
			formas[contenido].append(columna[1])
		if contenido not in formasres.keys():
			formasres[contenido]=[columna[1]]
			ejemplos[contenido]= [[columna[1]],[columna[2]]]
			caja.append([[columna[0]],[columna[1]],[columna[2]]])
		elif columna[1] not in formasres[contenido]:
			formasres[contenido].append(columna[1])
			ejemplos[contenido].append([[columna[1]],[columna[2]]])
			caja.append([[columna[0]],[columna[1]],[columna[2]]])

for clave, valor in formas.iteritems(): 
	cajitas = collections.Counter(valor).items()
	totales = sorted(cajitas,key=lambda i: i[1], reverse=True)
	print u'\n', u'CONSTRUCCIÓN:', clave, ':', u'Variantes:', len(totales), u'Observaciones:', len(valor)
	for c in totales:
		for y in c:
			for l, m in enumerate(caja):
				if y in m[1]:
					print u'', c
					print u''.join(m[2])
print u'\n', u'Observaciones totales:', i, u'\n', u'CONSTRUCCIONES TOTALES:', len(str(clave)), '\n', u'LISTADO DE CONSTRUCCIONES:', formas.keys()
#_________________________________________Aqui termina el diccionario de formas con cuneta y ejemplos.
#"""

#"""
#AQUI INICIA OTRO EXPERIMENTO
###Este funciona para contar cada una de las veces que aparecio una forma
for i,f in enumerate(fila_com):
	if i<1: #Para que no analice la fila 0, es decir, el ENCABEZADO
		continue #continue salta a la siguiente fila
	#Divide columnas en una nueva lista
	columna = f.split(u"¬")
	#Creo un loop que va llenando la caja (con formas) y las formas las organiza 
	for col,contenido in enumerate(columna):
		#FORMAS: Aquí le pido que solo consiere la columna 0 (correspondiente a la construcción)
		if col!=0 : continue
		#Voy llenando las variables: foras es un diccionario y cajas es una lista.
		if contenido not in formas.keys():
			formas[contenido]= [columna[1]]
		#Para que sigua llenando las formas
		else:
			formas[contenido].append(columna[1])
#Aquí le pido que cuente los items dentro del diccionario 'formas' y los organice
for clave, valor in formas.iteritems(): 
	cajitas = collections.Counter(valor).items()
	totales = sorted(cajitas,key=lambda i: i[1], reverse=True)
	for c in totales:
		print clave, c
#______________________________________________________Aqui termina el contador fino
#"""

