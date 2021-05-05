# %%

from collections import Counter, defaultdict
from itertools import chain
from beautifultable import BeautifulTable
import numpy


def handle_file(file):
    f = open(file)
    array = []
    for line in f:  # read lines
        array.append([int(x) for x in line.split()])
    f.close()
    # print("Números no arquivo: ", array, len(array))
    return array


def sort_nums(array):
    all_numbers = list(chain(*array))
    num_counted = Counter(all_numbers)
    # print("All num:", all_numbers)
    collection_sorted = sorted(num_counted.items())
    print("Collection sorted:\t\t", collection_sorted)
    num_individuais = sorted([key for key, value in collection_sorted])
    total_de_num = len(all_numbers)
    print("\nNúmeros únicos ordenados:\t", num_individuais)
    print("Total de números:\t\t", total_de_num)

    return all_numbers, num_individuais, total_de_num, collection_sorted


def my_table(num_individuais):
    table = BeautifulTable()
    table.columns.header = ["", "Números"]

    for i, num in enumerate(num_individuais):
        table.rows.append([i, num])

    table.set_style(BeautifulTable.STYLE_GRID)
    print('\n', table)
    return table


def fi(collection_sorted):
    return [value for key, value in collection_sorted]


def Fi(fi):
    ret = []
    acc = 0
    for i in fi:
        acc += i
        ret.append(acc)
    return ret


def fri(fi, soma_de_fi):
    ret = []
    for i in fi:
        ret.append(round(i/soma_de_fi * 100, 2))
    return ret


def Fri(Fi):
    ret = []
    for i in Fi:
        ret.append(round(i/soma_de_fi * 100, 2))
    return ret


def fiX(num_individuais, fi):
    ret = []
    for index, num in enumerate(num_individuais):
        ret.append(num * fi[index])
    return ret


# Code flow

file1 = './exemplo 1: Disitribuição de Frequencia Simples.txt'

array = handle_file(file1)

################

all_numbers, num_individuais, total_de_num, collection_sorted = sort_nums(
    array)

################

table = my_table(num_individuais)

################

fi = fi(collection_sorted)
soma_de_fi = sum(fi)
table.columns.insert(2, fi, header="fi")
print(table)
#print("\nfi:\t\t\t\t", fi)
print("Soma de fi == total_de_num:\t", sum(fi), "==", total_de_num)

################

Fi = Fi(fi)
# print("Frequência absoluta acum (Fi):\t", Fi)
table.columns.insert(3, Fi, header="Fi")
print(table)

################

fri = fri(fi, soma_de_fi)
# print("Frequência relativa (%):\t", fri)
table.columns.insert(4, fri, header="fri (%)")
print(table)
print("Soma de fri tem que dar 100%:\t", sum(fri))

################

Fri = Fri(Fi)
# print("Frequência relativa acum:\t", Fri)
table.columns.insert(5, Fri, header="Fri (%)")
print(table)

################

fiX = fiX(num_individuais, fi)
#print("fiX:\t\t\t\t", fiX)
table.columns.insert(6, fiX, header="fiX")
print(table)
print("Soma de todos os números:\t", sum(fiX))

#############

média = sum(fiX) / soma_de_fi
print("Média:\t\t\t\t", round(média, 6))

# %%
