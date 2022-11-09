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
assert cf
from tabulate import tabulate

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar los videojuegos publicados en un rango de tiempo para una plataforma ")
    print("3- Conocer los registros más recientes para un rango de tiempos récord  ")
    print("4- Encontrar el TOP N de los videojuegos más rentables para retransmitir")
    print("0- Salir")
    print("*******************************************")

catalogo = controller.newController()

"""
Menu principal
"""
def cargarjuegos(lista): #append()
    
    list_aux=[]
    list_aux_2=[]
    size=lt.size(lista)
    if size<6:
        for i in lt.iterator(lista):
            list_aux.append(i)
    else:
        list_aux.append(lt.getElement(lista,1))
        list_aux.append(lt.getElement(lista,2))
        list_aux.append(lt.getElement(lista,3))
        list_aux.append(lt.getElement(lista,size-2))
        list_aux.append(lt.getElement(lista,size-1))
        list_aux.append(lt.getElement(lista,size))
    for j in list_aux:
        list_aux2=["","","","","","",""]
        list_aux2[0]=lt.getElement(j,1)
        list_aux2[1]=lt.getElement(j,6)
        list_aux2[2]=lt.getElement(j,4)
        list_aux2[3]=lt.getElement(j,2)
        list_aux2[4]=lt.getElement(j,5)
        list_aux2[5]=lt.getElement(j,7)
        list_aux2[6]=lt.getElement(j,3)


        list_aux_2.append(list_aux2)
    columnas = ["ID","Fecha Lanzamiento","Titulo","Abreviacion","Plataformas","Total de Runs","Genero"]
    print(tabulate(list_aux_2, headers = columnas, tablefmt = "grid", maxcolwidths = [5,13,18,13,30,8,13]))


def cargarspeedruns(lista): #append()
    list_aux=[]
    list_aux_=[]
    size=lt.size(lista)
    if size<6:
        for i in lt.iterator(lista):
            list_aux.append(i)
    else:
        list_aux.append(lt.getElement(lista,1))
        list_aux.append(lt.getElement(lista,2))
        list_aux.append(lt.getElement(lista,3))
        list_aux.append(lt.getElement(lista,size-2))
        list_aux.append(lt.getElement(lista,size-1))
        list_aux.append(lt.getElement(lista,size))
    for info in list_aux:
        list_aux2=["","","","","","","","",""]
        list_aux2[0]=lt.getElement(info,1)#Id
        list_aux2[1]=lt.getElement(info,12)#fecha
        list_aux2[2]=lt.getElement(info,8)#runs
        list_aux2[3]=lt.getElement(info,20)#nombre
        list_aux2[4]=lt.getElement(info,2)#category
        list_aux2[5]=lt.getElement(info,15)#sub
        list_aux2[6]=lt.getElement(info,4)#pais
        list_aux2[7]=lt.getElement(info,9)
        list_aux2[8]=lt.getElement(info,17)

        list_aux_.append(list_aux2)
    columnas = ["ID","Fecha","Runs","Nombre","Categoria","Subcategoria","Pais","Jugadores","Tiempo2"]
    print(tabulate(list_aux_, headers = columnas, tablefmt = "grid", maxcolwidths = [5,12,5,13,8,20,13,13,8]))

def printFechas(juegos):
    
    pass


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        catalogo=controller.cargarcontenido(catalogo)
        print("------------------------------------------------------")
        print("loaded Speedruning data properties...")
        print("Total loaded videogames: " + str(lt.size(catalogo["juegos"])))
        print("Total loaded category records: " + str(lt.size(catalogo["speedruns"])))
        print("------------------------------------------------------")
        print("The first 3 and last 3 videogames loaded in ADTs are...")
        print("Data from games displayed as read from CSV file")
        cargarjuegos(catalogo["juegos"])
        print("-------------------------------------------------------------")
        print("The first 3 and last 3 category redords loaded in ADTs are...")
        print("Data from games displayed as read from CSV file")
        cargarspeedruns(catalogo["speedruns"])


    elif int(inputs[0]) == 2: #req 1
        plataforma = input("Ingrese la plataforma a buscar: ")
        fecha1 = input("Ingrese la fecha inicial (en formato yy-mm-dd): ")
        fecha2 = input("Ingrese la fecha final (en formato yy-mm-dd): ")
        juegos = controller.getFechas(plataforma,fechai,fechaf,catalogo["fechas"])
        print("Avaible games in " + plataforma + ": " + INFOOOOOO)
        print("Date range between " + fecha1 + " and " + fecha2)
        print("Released games: " + INFOOOOO)
        #print("Altura del arbol: " + str(controller.indexHeight(catalogo)))
        #print("Elementos del arbol: " + str(controller.indexSize(catalogo)))
        print("There are " + INFOOOO + " elements in range.".format(lt.size(juegos),plataforma))
        print("The first 3 and last 3 in range are: ")
        printFechas(juegos)
        pass
    elif int(inputs[0]) == 3: #req 5
        lim_inf = input("Ingrese el límite inferior de la duración: ")
        lim_sup = input("Ingrese el límite superior de la duración: ")
        
        pass
    elif int(inputs[0]) == 4: #requ 7
        pass
    else:
        sys.exit(0)
sys.exit(0)
