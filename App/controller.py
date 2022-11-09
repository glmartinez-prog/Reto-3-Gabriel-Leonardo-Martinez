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
 """

import config as cf
import model
import csv
csv.field_size_limit(2147483647)


def newController():
    control = {
        'model': None
    }
    control['model'] = model.NuevoCatalogo()
    return control["model"]

def cargarcontenido(catalogo): 
    file = cf.data_dir + 'Speedruns/game_data_utf-8-small.csv' 
    input_file = csv.DictReader(open(file, encoding='utf-8')) 
    for contenido in input_file: 
        model.add_game_content(catalogo, contenido) 
    file = cf.data_dir + 'Speedruns/category_data_utf-8-small.csv' 
    input_file = csv.DictReader(open(file, encoding='utf-8')) 
    for contenido in input_file: 
        model.add_category_content(catalogo, contenido) 
    return catalogo

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def getFechas(plataforma,fechai,fechaf,catalogo):
    return model.getFechas(plataforma,fechai,fechaf,catalogo)

def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)
