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


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sel
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos
listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(tipe):
    catalog = {'videos': None,
               'category': None,
               'country': None}
    catalog['videos'] = lt.newList()
    x = ""
    if tipe == "1":
        x = 'SINGLE_LINKED'
    else:
        x = 'ARRAY_LIST'
    catalog['category'] = lt.newList(x,
                                     cmpfunction=comparecategories)
    catalog['country'] = lt.newList(x,
                                    cmpfunction=comparecountries)

    return catalog


def list_user(cantidad):
    return 4


# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)


def addCategory(catalog, category):
    c = newCategory(category['id'], category['name'])
    lt.addLast(catalog['category'], c)


def addCountry(catalog, country):
    c = newCountry(country['name'])
    lt.addLast(catalog['country'], c)


# Funciones para creacion de datos
def newCategory(name, id):
    category = {'id': id, 'name': name}
    return category


def newCountry(name):
    coutry = {'name': name}
    return coutry

# Funciones de consulta


def getCategory_ID(catalog, category_name):
    categories = catalog['category']
    pos = lt.isPresent(categories['name'], category_name)
    if pos != 0:
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
    while cont < len(videos) and numvid > 0:
        if videos[cont]['country'] == country and videos[cont]['category_id'] == cat_id:
            lt.addLast(templist, videos[cont])
            numvid -= 0
        cont += 1
    mostviewedbycountandcat = getFinalList(templist)
    return mostviewedbycountandcat


def FindTrendVideoByCountry(catalog, country):
    return 1


# Funciones utilizadas para comparar elementos dentro de una lista


def comparecategories(name, category):
    return (name == category['name'])


def cmpVideosByViews(video1, video2):
    return(float(video1['views']) > float(video2['views']))


def comparecountries(name, country):
    return (name == country['name'])

# Funciones de ordenamiento


def sortVideos(catalog, size, alg):
    sub_list = lt.subList(catalog['videos'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if alg == 1:
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
    elif alg == 2:
        sorted_list = sel.sort(sub_list, cmpVideosByViews)
    else:
        sorted_list = ins.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
