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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Buenos videos por categoría y país")
    print("3- Encontrar video tendencia por país")
    print("4- Buscar video tendencia por categoria")
    print("5- Video con más likes")


def initCatalog():
    """inicializa el catalogo de videos"""
    return controller.initCatalog()

def loadData(catalog):
    """
    carga los videos en la estructura de datos
    """
    controller.loadData(catalog)


def GoodVideosByCategoryAndConuntry(compilation):
    """
    busca videos por categoria y país"""
    size=lt.size(compilation)
    if size:
        for video in lt.iterator:
            print("trending_date: "+ compilation["trending_date"]+"title"+compilation["title"]+"channel_title"+compilation["channel_title"]+
             )
    else:
        print("No se encontraron videos")


def FindTrendVideoByCountry(mosttrend):
    """
    busca video tendencia por país"""



def TrendByCategory(mosttrend):
    "video tendecia por categoría"
    

def MostLikedVideos(mostliked):
    """
    videos con mas likes"""
    





catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        print("1-LINKED_LIST")
        print("2-ARRAY_LIST")
        input("Su eleccion es... ")

    elif int(inputs[0]) == 2:
        country=input("Ingrese el país: ")
        category=input("Ingrese la categoria: ")
        number=input("cantidad de videos por listar: ")
        compilation= controller.getVideosByCategoryAndConuntry(catalog, str(category), str(country), int(number))
        GoodVideosByCategoryAndConuntry(compilation)

    elif int(inputs[0])==3:
        country=input("Ingrese el país: ")
        mosttrend=controller.FindTrendVideoByCountry(catalog, country)
        FindTrendVideoByCountry(mosttrend)


    elif int(imputs[0])==4:
        category=input("Ingrese la categoria: ")
        mosttrend=controller.TrendByCategory(catalog, category)
        TrendByCategory(mosttrend)


    elif int(input[0])==5:
        mostliked=controller.MostLikedVideos(catalog)
        MostLikedVideos(mostliked)
        

    else:
        sys.exit(0)
sys.exit(0)
