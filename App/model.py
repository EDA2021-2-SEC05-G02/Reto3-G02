"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
from DISClib.Algorithms.Sorting import mergesort as mer
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de avistamientos de UFOS
    """

    catalog = {'Ufos': None,
               'dateIndex': None}

    catalog['Ufos'] = lt.newList('ARRAY_LIST')
    catalog['cityIndex'] = om.newMap(omaptype='BST',
                                     comparefunction=compareString)

    return catalog
    

# Funciones para agregar informacion al catalogo

def addUFO(catalog, ufo):
    """
    Agrega un avistamiento de UFO al catálogo
    """
    info = {}
    info['datetime'] = datetime.datetime.strptime(ufo['datetime'], '%Y-%m-%d %H:%M:%S')
    info['city'] = ufo['city']
    info['state'] = ufo['state']
    info['country'] = ufo['country']
    info['shape'] = ufo['shape']
    info['duration (seconds)'] = float(ufo['duration (seconds)'])
    info['duration (hours/min)'] = ufo['duration (hours/min)']
    info['comments'] = ufo['comments']
    info['date posted'] = datetime.datetime.strptime(ufo['date posted'], '%Y-%m-%d %H:%M:%S')
    info['latitude'] = float(ufo['latitude'])
    info['longitude'] = float(ufo['longitude'])

    for key in info:
        if info[key] == "":
            info[key] = "Unknown"


    lt.addLast(catalog['Ufos'], info)
    updateCityIndex(catalog['cityIndex'], info)

def updateCityIndex (mapa, ufo):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    ufocity = ufo['city'].lower()
    entry = om.get(mapa, ufocity)
    if entry is None:
        cityentry = newCity(ufocity)
        om.put(mapa, ufocity, cityentry)
    else:
        cityentry = me.getValue(entry)

    lt.addLast(cityentry['ufos'], ufo)

def newCity(city):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'city': None, 'ufos': None}
    entry['city'] = city
    entry['ufos'] = lt.newList('ARRAY_LIST')
    return entry

# Funciones para creacion de datos




# Funciones de consulta

def getFirst(lista, num):
    """
    Retorna los primeros num elementos de una lista
    """
    lista = lt.subList(lista, 1, num)
    return lista

def getLast(lista, num):
    """
    Retorna los ultimos num elementos de una lista
    """
    lista = lt.subList(lista, lt.size(lista)-(num-1), num)
    return lista

def UfosSize(catalog):
    """
    Número de avistamientos totales
    """
    return lt.size(catalog['Ufos'])


def indexHeight(catalog, indice):
    """
    Altura del arbol
    """
    return om.height(catalog[indice])

def indexSize(catalog, indice):
    """
    Numero de elementos en el indice
    """
    return om.size(catalog[indice])



def getUFOTopCity(catalog):
    """
    Retorna los avistamientos de una ciudad
    
    Req 1

    """
    lista = lt.newList('ARRAY_LIST')
    cit = om.keySet(catalog['cityIndex'])
    for key in lt.iterator(cit):
        entry = om.get(catalog['cityIndex'], key)
        city = me.getValue(entry)['ufos']
        lt.addLast(lista, {'city': key, 'count': lt.size(city)})
    mer.sort(lista, lambda x, y: x['count'] >= y['count'])
    five = getFirst(lista, 5)
    return five, lt.size(lista)

def getUFOByCity(catalog, city):

    """
    Req 1

    """
    cit = om.get(catalog['cityIndex'], city)
    if cit['key'] is not None:
        value = me.getValue(cit)['ufos']
        mer.sort(value, lambda x, y: x['datetime'] <= y['datetime'])
        first = getFirst(value, 3)
        last = getLast(value, 3)
    return first, last




# Funciones utilizadas para comparar elementos dentro de una lista
def compareDates(date1, date2):
    """
    Compara dos tipos de fecha
    """
    date = me.getKey(date2)
    if (date1 == date):
        return 0
    elif (date1 > date):
        return 1
    else:
        return -1

def compareString(str1, str2):
    """
    Compara dos strings
    """
    if (str1.lower() == str2.lower()):
        return 0
    elif (str1.lower() > str2.lower()):
        return 1
    else:
        return -1

# Funciones de ordenamiento
