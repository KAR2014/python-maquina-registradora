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

		pro+=1

		PRE = 0
		INV = 0

		print "Producto: "+ str(pro)

		

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
	loop=True
	comida=""
	res="si"
	subtotal=0
	
	print U"\n                         **** Wall-Mart S.A © ****"
	print u"                       Bienvenidos al área de compras:"
	
	
	print "Lista de Productos: \n"
	#Mostramos los productos para que el cliente elija
	for X in PRECIO:
		print "Producto: "+ X
		print "Precio: "+ str(PRECIO[X])
		print "\n"


	#Pedimos el ingreso de los productos
	while res !="no":
		res2="si"
		while loop == True:
			comida =raw_input("Ingrese Producto: ")
			comida=comida.lower()
			try:
				comida = float(comida)
				comida = int(comida)
				print "Error ingrese el nombre del Producto: \n"
				pass

			except(RuntimeError, TypeError, NameError, ValueError):
				break

		busqueda(comida)

		if busqueda(comida) == 0:
			print "Producto No Encontrado\n"
			pass
		elif busqueda(comida) == 1:
			print "Producto Encontrado\n"
			
			subtotal+=factura(comida)
			COMPRAS.append(comida)
			print COMPRAS
			print CANT
		while res2 != "no":

			res=raw_input("Desea Elegir otro producto si/no \n")
			res=res.lower()

			try:
				res=float(res)
				res = int(res)
				print "Error ingrese opcion válida: \n"
			except(RuntimeError, TypeError, NameError, ValueError):
				res=res

			if res=="si":
				break
			elif res=="no":
				break

	#print "SubTotal: "+ str(subtotal)
	return subtotal	


#Aqui mandamos a buscar el producto a la lista
def busqueda(comida):
	bus=0
	if INVENTARIO.has_key(comida):
		bus = 1
	else:
		bus = 0

	return bus

#Aqui calculamos los productos
def factura(comida):
	art=0
	fac=0
	if INVENTARIO[comida] > 0:
		print 'Si hay existencias'
		art=input("Cuantos Desea: ")
		print "Existencias: "
		INVENTARIO[comida]=INVENTARIO[comida]-art
		print INVENTARIO[comida]
		fac=(PRECIO[comida]*art)
		CANT.append(art)

	else:
		print "No hay Existencias"
		fac=0
	
	return fac

#Aqui iniciamos con la factura del cliente
def facturacion():
	nombre=""
	nit=""
	totalpar=0
	totalpag=0
	totalfinal=0
	tarjeta=0
	tarj=""
	total1=0
	
	subtotal=cliente()
	print U"\n                         **** Wall-Mart S.A © ****\n"
	print u"                       Bienvenidos al área de facturacion: "
	print "\n"
	nombre=raw_input("Nombre: ")
	nit=raw_input("NIT: ")
	print "Calculando Factura..."


	#print "		DESCRIPCION 	 CANTIDAD 	 PRECIO UNIT. 	  PARCIAL"
	#for i in COMPRAS:
	#	print str(PRECIO[i]) + " "+str(CANT[x1]) +" "+ str(PRECIO[COMPRAS]) +" "+ str(PARCIAL[x1]) 
	totalpar=subtotal*0.12

	print "Factura No.: 0001 "
	print "Nombre: " + nombre
	print "NIT: "+ nit +"\n"

	while True:
		print "Modo de Pago: "
		print "1. Cliente Frecuente Gold "
		print "2. Cliente Frecuente Silver "
		print "3. Cliente Particular\n"

		op=input("Ingresa una opción: ")

		if op == 1:
			print "Cliente Gold: "
			tarjeta=0.05
			break
		elif op == 2:
			print "Cliente Silver: "
			tarjeta=0.02
			break
		elif op == 3:
			print "Cliente Particular: "
			tarjeta=1
			break
		else:
			print "Ingrese opción válida\n"
			time.sleep(2)
			os.system("clear")

	totalpag=subtotal+totalpar
	total1=totalpag*tarjeta
	totalfinal=totalpag-total1


	print "SubTotal sin IVA:     Q. " + str(subtotal)
	print "SubTotal con IVA:     Q. "+ str(totalpag)
	print "Descuento de Cliente: Q. "+str(total1)
	print "Total a Pagar:        Q. "+ str(totalfinal)
	return

#MENU: Aqui va detallado el Menu de opciones
def menu():
	op=0
	clave=0
	loop=True
	restriccion=0
	restriccion2=0
	#print u"                              ***** Cognits *****"
	
	while loop==True:
		print U"\n                         **** Wall-Mart S.A © ****"
		print "1. Ingresar a Gerencia "
		print "2. Comprar y Facturar "
		print "3. Salir\n"

		op=input("Ingresa una opción: ")

		if op == 1:
			print "Bienvenido Gerente: "
			while clave != "KAR2014":

				clave=raw_input("Ingrese Contraseña: ")

				if clave== "KAR2014":
					restriccion=1
					ingreso_datos()
					break
				elif clave=="salir":
					os.system("clear")
					break
				else: 
					print u"Contraseña Invalida\n"

		elif op== 2 and restriccion != 1:
			print "Error Ingreso de Datos Fallido\n"
			time.sleep(3)
			os.system("clear")
		elif op == 2 and restriccion==1:
			facturacion()
		elif op == 3:
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