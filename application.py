# -*- coding: utf-8 -*-
import os
import time
import sys


INVENTARIO={}
PRECIO={}
COMPRAS=[]
CANT=[]
PARCIAL=[]

"""Caja Registradora"""

def ingreso_datos():
	
	pro=0

	RES=True
	print u"                  **** Uso Exclusivo del Gerente *****"
	while RES==True:

		CANTIDAD= raw_input("Ingrese cantidad de Artículos: ")
		try:
			CANTIDAD = int(CANTIDAD)
			if CANTIDAD > 0:
				break
			else:
				print u"Debe ingresar un número de Artículos Válido\n"
		except(RuntimeError, TypeError, NameError, ValueError):
			print u"Debe ingresar un número de Artículos Válido\n"
			Res=True

	print "\n"

	for I in range(0,CANTIDAD):

		PRO += 1

		PRE = 0
		INV = 0

		print "Producto: "+ str(PRO)

		

		while RES==True:
			ING=raw_input("Ingrese Producto: ")
			ING=ING.lower()
			try:
				ING = float(ING)
				ING=int(ING) 
				print u"Debe ingresar un producto válido\n"
				pass
			except(RuntimeError, NameError, ValueError):
				break

		while RES==True:
			PRE = raw_input("Ingrese Precio Producto: ")
			try:
				PRE=float(PRE)
				PRECIO[ING]=PRE
				break
			except(RuntimeError, NameError, ValueError):
				print u"Debe ingresar un precio válido\n"
				Res=True

		while RES==True:
			INV = raw_input("Ingrese Existencias: ")
			try:
				INV=int(INV)
				INVENTARIO[ING]=INV
				break
			except(RuntimeError, TypeError, NameError, ValueError):
				print u"Debe ingresar un número de existencias válidas\n"
				Res=True

		print "\n"

		
	print "                        Lista de Productos:          "

	for X in PRECIO:
		print "Producto: "+ X
		print "Precio: "+ str(PRECIO[X])
		print "Inventario: "+ str(INVENTARIO [X]) + "\n"

	return

#OPCION 2: Aqui ingresamos a la funcion del cliente
def cliente():
	LOOP = True
	COMIDA = ""
	RES = "si"
	SUBTOTAL = 0
	
	print U"\n                         **** Wall-Mart S.A © ****"
	print u"                       Bienvenidos al área de compras:"
	
	
	print "Lista de Productos: \n"
	#Mostramos los productos para que el cliente elija
	for X in PRECIO:
		print "Producto: "+ X
		print "Precio: "+ str(PRECIO[X])
		print "\n"


	#Pedimos el ingreso de los productos
	while RES !="no":
		RES2 = "si"
		while LOOP == True:
			COMIDA =raw_input("Ingrese Producto: ")
			COMIDA=COMIDA.lower()
			try:
				COMIDA = float(COMIDA)
				COMIDA = int(COMIDA)
				print "Error ingrese el nombre del Producto: \n"
				pass

			except(RuntimeError, TypeError, NameError, ValueError):
				break

		busqueda(COMIDA)

		if busqueda(COMIDA) == 0:
			print "Producto No Encontrado\n"
			pass
		elif busqueda(COMIDA) == 1:
			print "Producto Encontrado\n"
			
			SUBTOTAL+=factura(COMIDA)
			COMPRAS.append(COMIDA)
			print COMPRAS
			print CANT
		while RES2 != "no":

			RES=raw_input("Desea Elegir otro producto si/no \n")
			RES=RES.lower()

			try:
				RES=float(RES)
				RES = int(RES)
				print "Error ingrese opcion válida: \n"
			except(RuntimeError, TypeError, NameError, ValueError):
				RES = RES

			if RES == "si":
				break
			elif RES == "no":
				break

	#print "SubTotal: "+ str(subtotal)
	return SUBTOTAL


#Aqui mandamos a buscar el producto a la lista
def busqueda(COMIDA):
	BUS = 0
	if INVENTARIO.has_key(COMIDA):
		BUS = 1
	else:
		BUS = 0

	return BUS

#Aqui calculamos los productos
def factura(COMIDA):
	ART = 0
	FAC = 0
	if INVENTARIO[COMIDA] > 0:
		print 'Si hay existencias'
		art=input("Cuantos Desea: ")
		print "Existencias: "
		INVENTARIO[COMIDA]=INVENTARIO[COMIDA]-ART
		print INVENTARIO[COMIDA]
		FAC =(PRECIO[COMIDA]*ART)
		CANT.append(ART)

	else:
		print "No hay Existencias"
		FAC = 0
	
	return FAC

#Aqui iniciamos con la factura del cliente
def facturacion():
	NOMBRE = ""
	NIT = ""
	TOTALPAR = 0
	TOTALPAG = 0
	TOTALFINAL = 0
	TARJETA = 0
	TARJ = ""
	TOTAL1 = 0
	
	SUBTOTAL=cliente()
	print U"\n                         **** Wall-Mart S.A © ****\n"
	print u"                       Bienvenidos al área de facturacion: "
	print "\n"
	NOMBRE = raw_input("Nombre: ")
	NIT = raw_input("NIT: ")
	print "Calculando Factura..."


	#print "		DESCRIPCION 	 CANTIDAD 	 PRECIO UNIT. 	  PARCIAL"
	#for i in COMPRAS:
	#	print str(PRECIO[i]) + " "+str(CANT[x1]) +" "+ str(PRECIO[COMPRAS]) +" "+ str(PARCIAL[x1]) 
	TOTALPAR = SUBTOTAL*0.12

	print "Factura No.: 0001 "
	print "Nombre: " + NOMBRE
	print "NIT: "+ NIT +"\n"

	while True:
		print "Modo de Pago: "
		print "1. Cliente Frecuente Gold "
		print "2. Cliente Frecuente Silver "
		print "3. Cliente Particular\n"

		OP=input("Ingresa una opción: ")

		if OP == 1:
			print "Cliente Gold: "
			TARJETA = 0.05
			break
		elif OP == 2:
			print "Cliente Silver: "
			TARJETA = 0.02
			break
		elif OP == 3:
			print "Cliente Particular: "
			TARJETA = 1
			break
		else:
			print "Ingrese opción válida\n"
			time.sleep(2)
			os.system("clear")

	TOTALPAG=SUBTOTAL+TOTALPAR
	TOTAL1=TOTALPAG*TARJETA
	TOTALFINAL=TOTALPAG-TOTAL1

	print "SubTotal sin IVA:     Q. " + str(SUBTOTAL)
	print "SubTotal con IVA:     Q. "+ str(TOTALPAG)
	print "Descuento de Cliente: Q. "+str(TOTAL1)
	print "Total a Pagar:        Q. "+ str(TOTALFINAL)
	return

#MENU: Aqui va detallado el Menu de opciones
def menu():
	OP = 0
	CLAVE = 0
	LOOP = True
	RESTRICCION = 0
	#print u"                              ***** Cognits *****"
	
	while LOOP == True:
		print U"\n                         **** Wall-Mart S.A © ****"
		print "1. Ingresar a Gerencia "
		print "2. Comprar y Facturar "
		print "3. Salir\n"

		OP = input("Ingresa una opción: ")

		if OP == 1:
			print "Bienvenido Gerente: "
			while CLAVE != "KAR2014":

				CLAVE = raw_input("Ingrese Contraseña: ")

				if CLAVE == "KAR2014":
					RESTRICCION=1
					ingreso_datos()
					break
				elif CLAVE == "salir":
					os.system("clear")
					break
				else: 
					print u"Contraseña Invalida\n"

		elif OP == 2 and RESTRICCION != 1:
			print "Error Ingreso de Datos Fallido\n"
			time.sleep(3)
			os.system("clear")
		elif OP == 2 and RESTRICCION == 1:
			facturacion()
		elif OP == 3:
			print "Gracias por su Compra.\nEsperamos que Vuelva...."
			time.sleep(2)
			os.system("cls")
			print 
			print u"                    **** Caja Registradora Full Pro 2.0 © **** "
			print u"                              ***** Cognits *****"
			print u"                         Third Generation Grupo: KAR-FER :\n"
			print u"                                  Fernando López"
			print u"                                   Kevin Herrera\n"
			print u"                          KAR_KO,INDUSTRIS Copyright ®"
			time.sleep(3)
			sys.exit(2)
		else:
			print "Ingrese opción válida\n"
			time.sleep(2)
			os.system("clear")

menu() #Llamo a mi funcion menu