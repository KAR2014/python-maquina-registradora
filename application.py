# -*- coding: utf-8 -*-
"""CAJA REGISTRADORA"""
import os
import time
import sys


INVENTARIO = {}
PRECIO = {}
COMPRAS = []
CANT = []
PARCIAL = []

"""Caja Registradora"""

def ingreso_datos():
    CONTADOR = 0

    RESPUESTA = True
    print u"                  **** Uso Exclusivo del Gerente *****"
    while RESPUESTA == True:

        CANTIDAD = raw_input("Ingrese cantidad de Artículos: ")
        try:
            CANTIDAD = int(CANTIDAD)
            if CANTIDAD > 0:
                break
            else:
                print u"Debe ingresar un número de Artículos Válido\n"
        except(RuntimeError, TypeError, NameError, ValueError):
            print u"Debe ingresar un número de Artículos Válido\n"
            RESPUESTA = True

    print "\n"

    for INDICE in range(0, CANTIDAD):

        CONTADOR += 1

        PRECIO2 = 0
        INVENTARIO2 = 0

        print "Producto: "+ str(CONTADOR)
        while RESPUESTA == True:
            INGRESO = raw_input("Ingrese Producto: ")
            INGRESO = INGRESO.lower()
            try:
                INGRESO = float(INGRESO)
                INGRESO = int(INGRESO)
                print u"Debe ingresar un producto válido\n"
            except(RuntimeError, NameError, ValueError):
                break

        while RESPUESTA == True:
            PRECIO2 = raw_input("Ingrese Precio Producto: ")
            try:
                PRECIO2 = float(PRECIO2)
                PRECIO[INGRESO] = PRECIO2
                break
            except(RuntimeError, NameError, ValueError):
                print u"Debe ingresar un precio válido\n"
                RESPUESTA = True

        while RESPUESTA == True:
            INVENTARIO2 = raw_input("Ingrese Existencias: ")
            try:
                INVENTARIO2 = int(INVENTARIO2)
                INVENTARIO[INGRESO] = INVENTARIO2
                break
            except(RuntimeError, TypeError, NameError, ValueError):
                print u"Debe ingresar un número de existencias válidas\n"
                RESPUESTA = True

        print "\n"

    print "                        Lista de Productos:          "

    for X in PRECIO:
        print "Producto: "+ X
        print "Precio: "+ str(PRECIO[X])
        print "Inventario: "+ str(INVENTARIO[X]) + "\n"

    print u"Cerrando Sesión"
    time.sleep(2)
    os.system("clear")
    return

#OPCION 2: Aqui ingresamos a la funcion del cliente
def cliente():
    LOOP = True
    COMIDA = ""
    RESPUESTA1 = "si"
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
    while RESPUESTA1 != "no":
        RESPUESTA2 = "si"
        while LOOP == True:
            COMIDA = raw_input("Ingrese Producto: ")
            COMIDA = COMIDA.lower()
            try:
                COMIDA = float(COMIDA)
                COMIDA = int(COMIDA)
                print "Error ingrese el nombre del Producto: \n"

            except(RuntimeError, TypeError, NameError, ValueError):
                break

        busqueda(COMIDA)

        if busqueda(COMIDA) == 0:
            print "Producto No Encontrado\n"
        elif busqueda(COMIDA) == 1:
            print "Producto Encontrado\n"
            SUBTOTAL += factura(COMIDA)
            COMPRAS.append(COMIDA)
            print COMPRAS
            print CANT
        while RESPUESTA2 != "no":

            RESPUESTA1 = raw_input("Desea Elegir otro producto si/no \n")
            RESPUESTA1 = RESPUESTA1.lower()

            try:
                RESPUESTA1 = float(RESPUESTA1)
                RESPUESTA1 = int(RESPUESTA1)
                print "Error ingrese opcion válida: \n"
            except(RuntimeError, TypeError, NameError, ValueError):
                RESPUESTA1 = RESPUESTA1
            if RESPUESTA1 == "si":
                break
            elif RESPUESTA1 == "no":
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
        ART = int(raw_input("Cuantos Desea: "))
        print "Existencias: "
        INVENTARIO[COMIDA] = INVENTARIO[COMIDA]-ART
        print INVENTARIO[COMIDA]
        FAC = (PRECIO[COMIDA]*ART)
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
    TOTAL1 = 0
    SUBTOTAL = cliente()
    print U"\n                         **** Wall-Mart S.A © ****\n"
    print u"                       Bienvenidos al área de facturacion: "
    print "\n"
    NOMBRE = raw_input("Nombre: ")
    NIT = raw_input("NIT: ")
    print "Calculando Factura..."


    #print "		DESCRIPCION 	 CANTIDAD 	 PRECIO UNIT. 	  PARCIAL"
    #for i in COMPRAS:
    #print str(PRECIO[i]) + " "+str(CANT[x1]) +" "+ str(PRECIO[COMPRAS]) +" "+ str(PARCIAL[x1])
    TOTALPAR = SUBTOTAL*0.12

    print "Factura No.: 0001 "
    print "Nombre: " + NOMBRE
    print "NIT: "+ NIT +"\n"

    while True:
        print "Modo de Pago: "
        print "1. Cliente Frecuente Gold "
        print "2. Cliente Frecuente Silver "
        print "3. Cliente Particular\n"

        OP = int(raw_input("Ingresa una opción: "))
        if OP == 1:
            print "Cliente Gold: "
            TARJETA = 0.05
            TOTALPAG = SUBTOTAL + TOTALPAR
            TOTAL1 = TOTALPAG * TARJETA
            TOTALFINAL = TOTALPAG - TOTAL1
            break
        elif OP == 2:
            print "Cliente Silver: "
            TARJETA = 0.02
            TOTALPAG = SUBTOTAL + TOTALPAR
            TOTAL1 = TOTALPAG * TARJETA
            TOTALFINAL = TOTALPAG - TOTAL1
            break
        elif OP == 3:
            print "Cliente Particular: "
            TARJETA = 1
            TOTALPAG = SUBTOTAL + TOTALPAR
            TOTAL1 = 0.0
            TOTALFINAL = TOTALPAG
            break
        else:
            print "Ingrese opción válida\n"
            time.sleep(2)
            os.system("clear")


    print "SubTotal sin IVA:     Q. " + str(SUBTOTAL)
    print "SubTotal con IVA:     Q. "+ str(TOTALPAG)
    print "Descuento de Cliente: Q. "+ str(TOTAL1)
    print "Total a Pagar:        Q. "+ str(TOTALFINAL)

    for X in COMPRAS[:]:
        COMPRAS.remove(X)

    for X in CANT[:]:
        CANT.remove(X)
    return

#MENU: Aqui va detallado el Menu de opciones
def menu():
    OP = 0
    CLAVE = 0
    RESTRICCION = 0
    #print u"                              ***** Cognits *****"

    while True:

        while (OP != 1) or (OP != 2) or (OP != 3):
            print U"\n                         **** Wall-Mart S.A © ****"
            print "1. Ingresar a Gerencia "
            print "2. Comprar y Facturar "
            print "3. Salir\n"

            OP = raw_input("Ingresa una opción: ")

            try:
                OP = int(OP)
                if OP > 0:
                    break
                else:
                    print "Ingrese opción válida\n"
                    time.sleep(2)
                    os.system("clear")
            except(RuntimeError, TypeError, NameError, ValueError):
                print "Ingrese opción válida\n"
                time.sleep(2)
                os.system("clear")
                pass

        if OP == 1:
            print "Bienvenido Gerente: "
            while CLAVE != "KAR2014":
                CLAVE = raw_input("Ingrese Contraseña: ")
                if CLAVE == "KAR2014":
                    RESTRICCION = 1
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
            os.system("clear")
            print
            print u"                    **** Caja Registradora Full Pro 2.0 © **** "
            print u"                              ***** Cognits *****"
            print u"                         Third Generation Grupo: KAR-FER :\n"
            print u"                                  Fernando López"
            print u"                                   Kevin Herrera\n"
            print u"                          KAR_KO,INDUSTRIS Copyright ®"
            time.sleep(3)
            sys.exit(2)
    return
menu() #Llamo a mi funcion menu
