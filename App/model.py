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

    catalog['durationIndex'] = om.newMap(omaptype='BST',
                                     comparefunction=compareFloat)
                        
    catalog['timeIndex'] = om.newMap(omaptype='BST',
                                     comparefunction=compareTime)

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
    updateDurationIndex(catalog['durationIndex'], info)
    updateTimeIndex(catalog['timeIndex'], info)

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
    cityentry['size']+=1

def updateDurationIndex (mapa, ufo):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    ufoduration = ufo['duration (seconds)']
    entry = om.get(mapa, ufoduration)
    if entry is None:
        durationentry = newDuration(ufoduration)
        om.put(mapa, ufoduration, durationentry)
    else:
        durationentry = me.getValue(entry)

    lt.addLast(durationentry['ufos'], ufo)

def updateTimeIndex (mapa, ufo):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    ufotime = ufo['datetime'].time()
    entry = om.get(mapa, ufotime)
    if entry is None:
        timeentry = newTime(ufotime)
        om.put(mapa, ufotime, timeentry)
    else:
        timeentry = me.getValue(entry)

    lt.addLast(timeentry['ufos'], ufo)
    timeentry['size'] += 1
    
# Funciones para creacion de datos

def newCity(city):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'city': None, 'ufos': None, 'size':0}
    entry['city'] = city
    entry['ufos'] = lt.newList('ARRAY_LIST')
    return entry
    
def newDuration(duration):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'duration': None, 'ufos': None}
    entry['duration'] = duration
    entry['ufos'] = lt.newList('ARRAY_LIST')
    return entry

def newTime(time):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'time': None, 'ufos': None, 'size':0}
    entry['time'] = time
    entry['ufos'] = lt.newList('ARRAY_LIST')
    
    return entry

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


#Requerimientos

def getUFOTopCity(catalog):
    """
    Req 1:
    Retorna el Top 5 ciudades con mas avistamientos
    """
    lista = lt.newList('ARRAY_LIST')
    keys = om.keySet(catalog['cityIndex']) 
    size = 0
    for key in lt.iterator(keys):
        entry = om.get(catalog['cityIndex'], key)
        value = me.getValue(entry)
        size = value['size']
        info={'city': key,
              'count': size}
        lt.addLast(lista, info)

    mer.sort(lista, cmpByCount)
    five = getFirst(lista, 5)

    return five, lt.size(keys)

def getUFOByCity(catalog, city):
    """
    Req 1:
    """
    entry = om.get(catalog['cityIndex'], city)
    if entry:
        value = me.getValue(entry)
        ltUfos = value['ufos']
        size = value['size']
        mer.sort(ltUfos, cmpDate)

        return ltUfos, size
    else:
        return None


def getUFOTopDuration(catalog):
    """
    Req 2
    """
    lista = lt.newList('ARRAY_LIST')
    dur = om.keySet(catalog['durationIndex'])
    for key in lt.iterator(dur):
        entry = om.get(catalog['durationIndex'], key)
        duration = me.getValue(entry)['ufos']
        lt.addLast(lista, {'duration': key})
    mer.sort(lista, cmpDuration)
    five = getFirst(lista, 5)
    return dur


def getUFOinTime(catalog, inf, sup):
    """
    Req 3
    """
    values = om.values(catalog['timeIndex'], inf, sup)
    ltUfos = lt.newList('ARRAY_LIST')
    for value in lt.iterator(values):
        for Ufo in lt.iterator(value['ufos']):
            lt.addLast(ltUfos, Ufo)
    return ltUfos

def getTopTime(catalog):
    mapa = catalog['timeIndex']
    size = om.size(mapa)
    top5 = om.values(mapa,om.select(mapa,size-5),om.maxKey(mapa))
    ltUfos = lt.newList('ARRAY_LIST')
    for value in lt.iterator(top5):
        info = {'time': value['time'],
                'count': value['size']}
        lt.addLast(ltUfos, info)
    return ltUfos

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

def compareFloat(num1, num2):
    """
    Compara dos Floats
    """
    num1 = float(num1)
    num2 = float(num2)
    if (num1 == num2):
        return 0
    elif (num1 > num2):
        return 1
    else:
        return -1
    
def compareTime (time1, time2):
    """
    Compara dos Fechas
    """
    if (time1 == time2):
        return 0
    elif (time1 > time2):
        return 1
    else:
        return -1


def cmpByCount (city1, city2):
    return city1['count'] > city2['count']

def cmpDuration(ufo1, ufo2):
    return ufo1['duration'] > ufo2['duration']

def cmpDate (ufo1, ufo2):
    return ufo1['datetime'] < ufo2['datetime']


# Funciones de ordenamiento
