"""
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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
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
    print("0- Salir")

catalog = None

# Funciones para la impresión de tablas

def PrintTopCities(info):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["City", "Count"]
    for i in lt.iterator(info):
        x.add_row([ i["city"], i["count"]])
    print(x)

def printUfosTable(info):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["Datetime", "City", "State", "Country", "Shape", "Duration (seconds)"]
    for i in lt.iterator(info):
        x.add_row([ i["datetime"], i["city"], 
                    i["state"], i["country"], 
                    i["shape"], i["duration (seconds)"]])
    print(x)

def PrintReq1(cityname, topcities, cityinfo):
    print("="*15, " Req No. 1 Inputs ", "="*15)
    print("UFO Sightings in the city of:", cityname,"\n")
    print("="*15, " Req No. 1 Answer ", "="*15)
    print("There are", topcities[1], "defferent cities with UFO sightings...")
    print("The TOP 5 cities with the most UFO sightings are:")
    PrintTopCities(topcities[0])
    print("\nThere are",cityinfo[1],"sightings at the:", cityname,"city")

    if lt.size(cityinfo[0]) > 6:
        first = controller.getFirst(cityinfo[0], 3)
        last = controller.getLast(cityinfo[0], 3)
        print('The first 3 UFO sightings in the city are:')
        printUfosTable(first)
        print('\nThe last 3 UFO sightings in the city are:')
        printUfosTable(last)
    else:
        print('The UFO sightings in the city are:')
        printUfosTable(cityinfo[0])

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

    elif int(inputs[0]) == 2: #Req 1
        cityname = input('Ingrese la ciudad: ')
        cityinfo = controller.getUFOByCity(catalog, cityname.lower())

        if cityinfo:
            topcities = controller.getUFOTopCity(catalog)
            PrintReq1(cityname, topcities, cityinfo)
        else:
            print("La ciudad ingresada no tiene avistamientos de UFO\n")
        

    elif int(inputs[0]) == 3:
        duration = controller.getUFOTopDuration(catalog)
        print(duration)

        pass
        
        
    else:
        sys.exit(0)
sys.exit(0)
