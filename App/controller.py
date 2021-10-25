﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog
# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos.
    """
    loadUfos(catalog)

def loadUfos(catalog):
    """
    Carga las obras del archivo. Por cada obra se indica al
    modelo que debe adicionarla al catalogo.
    """
    Ufosfile = cf.data_dir + 'UFOS-utf8-small.csv'
    input_file = csv.DictReader(open(Ufosfile, encoding='utf-8'))
    for ufo in input_file:
        model.addUFO(catalog, ufo)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def UfosSize(catalog):
    return model.UfosSize(catalog)

def indexHeight(catalog, indice):
    return model.indexHeight(catalog, indice)

def indexSize(catalog, indice):
    return model.indexSize(catalog, indice)

def getUFOTopCity(catalog):
    return model.getUFOTopCity(catalog)

def getUFOByCity(catalog, city):
    return model.getUFOByCity(catalog, city)

def getUFOTopDuration(catalog):
    return model.getUFOTopDuration(catalog)

def getUFOByDuration(catalog, minimo, maximo):
    return model.getUFOByDuration(catalog, minimo, maximo)
