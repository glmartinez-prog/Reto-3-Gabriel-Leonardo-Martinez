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
from DISClib.ADT import orderedmap as ormp
from DISClib.DataStructures import rbt
from DISClib.DataStructures import mapentry as mpe
#from DISClib.Algorithms.Sorting import shellsort as sa
from datetime import datetime
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def NuevoCatalogo():
    catalogo={"juegos":None,
              "speedruns":None,
              "fechas":None,
              "nombres":None}
    catalogo["juegos"]=lt.newList("ARRAY_LIST")
    catalogo["speedruns"]=lt.newList("ARRAY_LIST")
    catalogo["nombres"]=mp.newMap(numelements=1000,maptype="CHAINING")
    catalogo["fechas"]=ormp.newMap(omaptype="RBT",comparefunction=cmpFecha)
    return catalogo

#-----------------------------------------------------------------------------------

def add_category_content(catalogo,contenido):
    nombre=mp.get(catalogo["nombres"],int(contenido["Game_Id"]))
    nombre=mpe.getValue(nombre)
    info=dicc_array(contenido)
    lt.addLast(info,nombre)
    lt.addLast(catalogo["speedruns"],info)
    pass

def add_game_content(catalogo,contenido):
    info=dicc_array2(contenido)
    lt.addLast(catalogo["juegos"],info)
    addDate(catalogo["fechas"],info)
    mp.put(catalogo["nombres"],int(contenido["Game_Id"]),contenido["Name"])
    pass

def dicc_array(contenido):
    array=lt.newList("ARRAY_LIST")
    lt.addFirst(array,contenido["Game_Id"])#1
    lt.addLast(array,contenido["Category"])#2
    lt.addLast(array,contenido["Category_Id"])#3
    lt.addLast(array,contenido["Country_0"])#4
    lt.addLast(array,contenido["Country_1"])#5
    lt.addLast(array,contenido["Country_2"])#6
    lt.addLast(array,contenido["Misc"])#7
    lt.addLast(array,contenido["Num_Runs"])#8
    lt.addLast(array,contenido["Players_0"])#9
    lt.addLast(array,contenido["Players_1"])#10
    lt.addLast(array,contenido["Players_2"])#11
    lt.addLast(array,contenido["Record_Date_0"][0:10]+" "+contenido["Record_Date_0"][11:19])#12
    lt.addLast(array,contenido["Record_Date_1"][0:10]+" "+contenido["Record_Date_1"][11:19])#13
    lt.addLast(array,contenido["Record_Date_2"][0:10]+" "+contenido["Record_Date_2"][11:19])#14
    """lt.addLast(array,cambio(contenido["Record_Date_0"]))#12
    lt.addLast(array,cambio(contenido["Record_Date_1"]))#13
    lt.addLast(array,cambio(contenido["Record_Date_2"]))#14"""
    lt.addLast(array,contenido["Subcategory"])#15
    lt.addLast(array,contenido["Subcategory_Id"])#16
    lt.addLast(array,contenido["Time_0"])#17
    lt.addLast(array,contenido["Time_1"])#18
    lt.addLast(array,contenido["Time_2"])#19
    # nombre 20
    return array

def cambio(str):
    if len(str)>3:
        str2=str[0:10]+" "+str[11:19]
        fecha=datetime.strptime(str2, "%Y-%m-%d %H:%M:%S")
    else:
        fecha=datetime.strptime("1000-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    return fecha

def dicc_array2(contenido):
    array=lt.newList("ARRAY_LIST")
    lt.addFirst(array,contenido["Game_Id"])#1
    lt.addLast(array,contenido["Abbreviation"])#2
    lt.addLast(array,contenido["Genres"])#3
    lt.addLast(array,contenido["Name"])#4
    lt.addLast(array,contenido["Platforms"])#5
    lt.addLast(array,contenido["Release_Date"])#6
    lt.addLast(array,contenido["Total_Runs"])#7
    return array
# Funciones para creacion de datos

def addDate(arbol,info):
    fecha=datetime.strptime(lt.getElement(info,6), "%y-%m-%d")
    exist=ormp.contains(arbol,fecha)
    if exist:
        array=ormp.get(arbol,fecha)
        array=mpe.getValue(array)
        lt.addLast(array,info)

    else:
        #anada
        array=lt.newList("ARRAY_LIST")
        lt.addFirst(array,info)
    ormp.put(arbol,fecha,array)
    pass
# Funciones de consulta
def getFechas(plataforma,fechai,fechaf,arbol):
    fecha_i=datetime.strptime(fechai, "%y-%m-%d")
    fecha_f=datetime.strptime(fechaf, "%y-%m-%d")
    array=lt.newList("ARRAY_LIST")
    array2=rbt.valuesRange(arbol["root"],fecha_i,fecha_f,array,cmpFecha)
    array3=lt.newList("ARRAY_LIST")
    for i in lt.iterator(array2):
        plat=lt.getElement(i["elements"][0],5)
        if plataforma in plat:
            lt.addLast(array3,i["elements"][0])

    return array3

def indexHeight(catalogo):
    """
    Altura del arbol
    """
    return ormp.height(catalogo["fechas"])

def indexSize(catalogo):
    """
    Numero de elementos en el indice
    """
    return ormp.size(catalogo["fechas"])

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def cmpFecha(fecha1,fecha2):
    if fecha1<fecha2:
        return 1
    elif fecha1>fecha2:
        return -1
    else:
        return 0