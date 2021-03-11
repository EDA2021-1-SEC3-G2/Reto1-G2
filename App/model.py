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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import sys
import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10) 

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos
listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newLinkedCatalog():
    catalog = {'videos': None,
               'category': None}
    catalog['videos'] = lt.newList()
    catalog['category'] = lt.newList('LINKED_LIST',
                                     cmpfunction=comparecategories)

    return catalog


def newArrayCatalog():
    catalog = {'videos': None,
               'category': None}
    catalog['videos'] = lt.newList()
    catalog['category'] = lt.newList('ARRAY_LIST',
                                     cmpfunction=comparecategories)
    return catalog


def list_user(cantidad):
    return 4


# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)


def addCategory(catalog, category):
    c = newCategory(category['id'], category['name'])
    lt.addLast(catalog['category'], c)


# Funciones para creacion de datos
def newCategory(name, id):
    category = {'id': name, 'name': id}
    return category


# Funciones de consulta


def getCategory_ID(catalog, category_name):
    categories = catalog['category']
    for element in categories["elements"]:
        if lt.isPresent(element["name"], category_name) != 0:
            pos = lt.isPresent(element["name"], category_name)
        return categories['id'][pos]


def getFinalList(lis):
    final = {'trending_date': "", 'title': "",
             'channel_title': "", 'publish_time': "",
             'views': "", 'likes': "", 'dislikes': ""}
    final['trending_date'] = lis['trending date']
    final['title'] = lis['title']
    final['channel_title'] = lis['channel_title']
    final['publish_time'] = lis['publish_time']
    final['views'] = lis['views']
    final['likes'] = lis['likes']
    final['dislikes'] = lis['dislikes']
    return final


def getVideosByCategoryAndCountry(catalog, category_name, country,  numvid):
    videos = catalog['videos']
    mostviewedbycountandcat = lt.newList()
    templist = lt.newList()
    cat_id = getCategory_ID(catalog, category_name)
    cont = 0
    temp = numvid
    while cont < len(videos) and temp > 0:
        if videos[cont]['country'].lower() == country.lower() and videos[cont]['category_id'] == cat_id:
            lt.addLast(templist, videos[cont])
            temp -= 0
        cont += 1
    #mostviewedbycountandcat = getFinalList(templist)
    return mostviewedbycountandcat


def FindTrendVideoByCountry(catalog, country):
    videos_list = catalog['videos']
    sorted_list = merg.sort(videos_list, cmpVideosByCountry)
    pos = FindStartPosition(sorted_list, country)
    final_list = lt.subList(sorted_list, pos[0], pos[1])
    sorted_final_list = merg.sort(final_list, cmpVideosByTitle)
    
    return result


def FindStartPosition(catalog, country):
    pos = -1
    i = 0
    while pos == -1 and pos != i:
        if catalog[i]['country'] == country:
            pos = i
        i += 1
    numpos = FindEndPosition(catalog, country, pos)
    return (pos, numpos)


def FindEndPosition(catalog, country, pos):
    ver = True
    i = pos
    while ver:
        if catalog[i]['country'] != country:
            i -= 2
            ver = False
        i += 1
    numpos = (i - pos) + 1
    return numpos


def getFinalListTrendVidByCount(catalog, cant):
    final_list = {}
    final_list['title'] = catalog['title']
    final_list['channel_title'] = catalog['channel_title']
    final_list['country'] = catalog['country']
    final_list['días'] = cant
    return final_list
# Funciones utilizadas para comparar elementos dentro de una lista


def comparecategories(name, category):
    return (name == category['name'])


def cmpVideosByViews(video1, video2):
    return(float(video1['views']) > float(video2['views']))


def cmpVideosByCountry(country1, country2):
    return(country1 > country2)


def cmpVideosByTitle(title1, title2):
    return(title1 == title2)

# Funciones de ordenamiento


def sortVideos(catalog, size, alg):
    sub_list = lt.subList(catalog['videos'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if alg == 1:
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
    elif alg == 2:
        sorted_list = sel.sort(sub_list, cmpVideosByViews)
    elif alg == 3:
        sorted_list = ins.sort(sub_list, cmpVideosByViews)
    elif alg == 4:
        sorted_list = merg.sort(sub_list, cmpVideosByViews)
    else:
        sorted_list = quick.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
