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
    print("2- Seleccionar el tipo de algoritmo que desee utilizar para ordenar la lista")
    print("3- Buenos videos por categoría y país")
    print("4- Encontrar video tendencia por país")
    print("5- Buscar video tendencia por categoria")
    print("6- Video con más likes")


def initLinkedCatalog():
    # intento pasar la info tomada del imput en el menú.
    """inicializa el catalogo de videos"""
    return controller.initLinkedCatalog()


def initArrayCatalog():
    return controller.initArrayCatalog()


def loadData(catalog):
    """
    carga los videos en la estructura de datos
    """
    controller.loadData(catalog)


def GoodVideosByCategoryAndConuntry(compilation):
    """
    busca videos por categoria y país"""
    size = lt.size(compilation)
    if size:
        for video in lt.iterator:
            print("Día que fue trending: " + compilation["trending_date"] + "Nombre del video: " + compilation["title"]+"Canal: " + compilation["channel_title"])
    else:
        print("No se encontraron videos")


def FindTrendVideoByCountry(mosttrend):
    """
    busca video tendencia por país
    """


def TrendByCategory(mosttrend):
    """video tendecia por categoría
    """


def MostLikedVideos(mostliked):
    """
    videos con mas likes
    """


catalog = {}


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
        tipe = int(input("Su eleccion es... "))
        if tipe == 1:
            catalog = initLinkedCatalog()
        else:
            catalog = initArrayCatalog()
        loadData(catalog)
        print("Categorias cargadas: " + str(lt.size(catalog['category'])))
        print("Videos cargados: " + str(lt.size(catalog['videos'])))
        #title, cannel_title, trending_date, country, views, likes, dislikes
        print(catalog["category"])
    elif int(inputs[0]) == 2:
        print("Indique el tipo de algoritmo que desse utilizar")
        print("1 - shellshort")
        print("2 - selectionsort")
        print("3 - insertionsort")
        print("4 - mergesort")
        print("5 - quicksort")
        alg = int(input("Su selección es..."))
        size = input("Indique tamaño de la muestra que desee: ")
        result = controller.sortVideos(catalog, int(size), alg)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))

    elif int(inputs[0]) == 3:
        country = input("Ingrese el país: ")
        category = input("Ingrese la categoria: ")
        number = input("cantidad de videos por listar: ")
        
        compilation = controller.getVideosByCategoryAndCountry(catalog, str(category), str(country), int(number))
        GoodVideosByCategoryAndConuntry(compilation)

    elif int(inputs[0]) == 4:
        country = input("Ingrese el país: ")
        mosttrend = controller.FindTrendVideoByCountry(catalog, country)
        FindTrendVideoByCountry(mosttrend)

    elif int(input[0]) == 5:
        category = input("Ingrese la categoria: ")
        mosttrend = controller.TrendByCategory(catalog, category)
        TrendByCategory(mosttrend)

    elif int(inputs[0]) == 6:
        mostliked = controller.MostLikedVideos(catalog)
        MostLikedVideos(mostliked)

    else:
        sys.exit(0)
sys.exit(0)
