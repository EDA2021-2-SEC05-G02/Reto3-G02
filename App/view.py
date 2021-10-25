﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
import prettytable
from prettytable import PrettyTable
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- (Req 1) Contar los avistamientos en una ciudad")
    #print("3- (Req 2) Contar los avistamientos por duración")    
    #print("4- (Req 3) Contar los avistamientos por Hora/Minutos del día")    
    #print("5- (Req 4) Contar los avistamientos en rango de fechas") 
    #print("5- (Req 5) Contar los avistamientos de una Zona Geográfica")       
    #print("6- (Bono) Visualizar los avistamientos de una zona geográfica")
    print("7- Salir")

catalog = None

# Funciones para la impresión de tablas

def printTopTable(info):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["city", "count"]
    for i in lt.iterator(info):
        x.add_row([ i["city"], i["count"]])

    print(x)

def printTable(info):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["datetime", "city", "state", "country", "shape", "duration(seconds)"]
    for i in lt.iterator(info):
        x.add_row([ i["datetime"], i["city"], 
                    i["state"], i["country"], 
                    i["shape"], i["duration (seconds)"]])
    print(x)


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        catalog = controller.initCatalog()
        print("Cargando información de los archivos ....")
        controller.loadData(catalog)
        print('Avistamientos cargadas:', controller.UfosSize(catalog))
        print('Altura del arbol de cityIndex:', controller.indexHeight(catalog,'cityIndex'))
        print('Elementos en el arbol de cityIndex:',controller.indexSize(catalog, 'cityIndex'))

    elif int(inputs[0]) == 2:
        numcity = controller.getUFOTopCity(catalog)
        print('Total: ' + str(numcity[1]))
        printTopTable(numcity[0])
        city = input('Ingrese la ciudad: ')
        top = controller.getUFOByCity(catalog, city)
        for x in top:
            printTable(x)
        
        
    else:
        sys.exit(0)
sys.exit(0)
