# %%

from collections import Counter, defaultdict
from itertools import chain
from beautifultable import BeautifulTable
import numpy
import math


def handle_file(file):
    f = open(file)
    array = []
    for line in f:  # read lines
        array.append([int(x) for x in line.split()])
    f.close()
    #print("Números no arquivo: ", array, len(array))
    return array


def sort_nums(array):
    all_numbers = list(chain(*array))
    num_counted = Counter(all_numbers)
    #print("All num:", all_numbers)
    num_sorted = sorted(num_counted.items())
    print("Collection sorted:\t\t", num_sorted)
    num_individuais = sorted([key for key, value in num_sorted])
    total_de_num = len(all_numbers)
    print("\nNúmeros únicos ordenados:\t", num_individuais)
    print("Total de números:\t\t", total_de_num)

    return all_numbers, num_individuais, total_de_num


def amplitude(num_individuais, num_de_classes):
    amplitude_total = max(num_individuais) - min(num_individuais)
    print("Amplitude total:\t\t", amplitude_total)

    amplitude_intervalo = int(amplitude_total / num_de_classes)
    print("Amplitude de intervalo:\t\t", amplitude_intervalo)

    return amplitude_total, amplitude_intervalo


def num_inter(num_individuais, amplitude_intervalo):
    table_num_inter = []
    begin_num = num_individuais[0]
    table_num_inter.append(begin_num)
    rng = range(int(amplitude_total/amplitude_intervalo))
    #print("rng =", rng)

    for _ in rng:
        #print("for _ in rng: _ =", _)
        begin_num += amplitude_intervalo
        table_num_inter.append(begin_num)

    print("table_num_inter:\t\t", table_num_inter)
    return table_num_inter


def my_table(table_num_inter, num_de_classes, amplitude_intervalo):
    table = BeautifulTable()
    table.columns.header = ["", "Números"]

    limits = []
    for i, num in enumerate(table_num_inter):
        if i == num_de_classes:
            break
        if i == num_de_classes-1:
            table.rows.append([i, f"{num} |----| {num+amplitude_intervalo}"])
        else:
            table.rows.append([i, f"{num} |----  {num+amplitude_intervalo}"])
        limits.append(num+amplitude_intervalo)

    print()
    table.set_style(BeautifulTable.STYLE_GRID)
    print(table)
    return table


def fi(table, num_de_classes, all_numbers, table_num_inter, amplitude_intervalo):
    times = []
    rng = num_de_classes
    #print("Rng:\t", rng)
    for index in range(rng):  # 0 a 6 (7)
        value = table_num_inter[index]  # 15, 20, ..., 50
        #print("value = ", value)
        acc = 0
        for v in all_numbers:  # 14, 16, 17, ..., 49, 50
            if index != rng-1:  # index != 6
                if v >= value and v < value+amplitude_intervalo:
                    # print(v)
                    acc += 1
            elif index == rng-1:
                if v >= value and v <= value+amplitude_intervalo:
                    #print("index == rng-1", v)
                    acc += 1
        times.append(acc)

    #print("Times:\t", times)

    table_ = []
    j = 0
    for i in range(rng):
        val = table_num_inter[i]
        if j == rng:  # j == 7
            j = i - 1
        # print(j)
        #table_.append(f"{val} a {table_num_inter[j+1]}: {times[i]}")
        table_.append(f"{times[i]}")
        j += 1
    #print("Table:\t", table_)

    return table_, times


def Fi(fi):
    ret = []
    acc = 0
    for i in fi:
        acc += i
        ret.append(acc)
    return ret


def fri(fi, total_de_num):
    ret = []
    for i in fi:
        ret.append(round((i / total_de_num * 100), 2))
    return ret


def Fri(fri):
    ret = []
    sum = 0
    for i in fri:
        sum += i
        ret.append(sum)
    return ret


# Code flow

file1 = './exemplo 1: Disitribuição de Frequencia de Classe com Raiz.txt'

array = handle_file(file1)

################

all_numbers, num_individuais, total_de_num = sort_nums(array)
num_de_classes = math.ceil(math.sqrt(total_de_num))

################


amplitude_total, amplitude_intervalo = amplitude(
    num_individuais, num_de_classes)

################

table_num_inter = num_inter(num_individuais, amplitude_intervalo)

table = my_table(table_num_inter, num_de_classes, amplitude_intervalo)

################

fi_str, fi = fi(table, num_de_classes, all_numbers,
                table_num_inter, amplitude_intervalo)
table.columns.insert(2, fi_str, header="fi")
print(table)
print("\nfi:\t\t\t\t", fi)
print("Soma de fi == total_de_num:\t", sum(fi), "==", total_de_num)

################

Fi = Fi(fi)
#print("Frequência absoluta acum (Fi):\t", Fi)
table.columns.insert(3, Fi, header="Fi")
print(table)

################

fri = fri(fi, total_de_num)
#print("Frequência relativa (%):\t", fri)
table.columns.insert(4, fri, header="fri")
print(table)
print("Soma de fri tem que dar 100%:\t", sum(fri))

################

Fri = Fri(fri)
#print("Frequência relativa acum:\t", Fri)
table.columns.insert(5, Fri, header="Fri")
print(table)

# %%
