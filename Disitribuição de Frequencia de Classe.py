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
    return array


def sort_nums(array):
    all_numbers = list(chain(*array))
    num_counted = Counter(all_numbers)
    # print(num_counted)
    num_sorted = sorted(num_counted.items())
    print("Collection sorted:\t\t", num_sorted)
    num_individuais = sorted([key for key, value in num_sorted])
    total_de_num = len(num_individuais)
    print("\nNúmeros únicos ordenados:\t", num_individuais)
    print("Total de números:\t\t", total_de_num)

    return num_sorted, num_individuais, total_de_num


def amplitude(num_individuais, qnt_de_intervalos):
    amplitude_total = max(num_individuais) - min(num_individuais)
    print("Amplitude total:\t\t", amplitude_total)

    amplitude_intervalo = amplitude_total / qnt_de_intervalos
    print("Amplitude de intervalo:\t\t", amplitude_intervalo)

    return (amplitude_total, amplitude_intervalo)


def num_inter(num_individuais, amplitude_intervalo):
    table_num_inter = []
    begin_num = num_individuais[0]
    table_num_inter.append(begin_num)
    for _ in range(int(amplitude_intervalo)):
        begin_num += amplitude_intervalo
        table_num_inter.append(begin_num)

    print("table_num_inter:\t\t", table_num_inter)
    return table_num_inter


def my_table(table_num_inter, amplitude_intervalo):
    table = BeautifulTable()
    table.columns.header = ["", "Números"]

    limits = []
    for i, num in enumerate(table_num_inter):
        if i == amplitude_intervalo:
            break
        table.rows.append([i, f"{num} a {num+amplitude_intervalo}"])
        limits.append(num+amplitude_intervalo)

    print()
    table.set_style(BeautifulTable.STYLE_GRID)
    print(table)
    return table


def fi(table, amplitude_intervalo, num_individuais, table_num_inter):
    times = []
    for index in range(int(amplitude_intervalo)):  # 0 a 6
        value = table_num_inter[index]  # 14, 20, ..., 44
        acc = 0
        for v in num_individuais:  # 14, 16, 17, ..., 49, 50
            if index != (int(amplitude_intervalo)-1):
                if v >= value and v < value+amplitude_intervalo:
                    # print(v)
                    acc += 1
            elif index == (int(amplitude_intervalo)-1):
                if v >= value and v <= value+amplitude_intervalo:
                    # print(v)
                    acc += 1
        times.append(acc)

    # print(times)

    table_ = []
    j = 0
    for i in range(int(amplitude_intervalo)):
        val = table_num_inter[i]
        if j == int(amplitude_intervalo):
            j = i - 1
        table_.append(f"{val} a {table_num_inter[j+1]}: {times[i]}")
        j += 1
    # print(t)

    return table_, times


def Fi(fi):
    ret = []
    acc = 0
    for i in fi:
        acc += i
        ret.append(acc)
    return ret


def fr(fi, amplitude_total):
    ret = []
    for i in fi:
        ret.append(round((i / amplitude_total * 100), 2))
    return ret


# Code flow


array = handle_file('./exemplo: Disitribuição de Frequencia de Classe.txt')

num_sorted, num_individuais, total_de_num = sort_nums(array)

amplitude_total, amplitude_intervalo = amplitude(
    num_individuais, qnt_de_intervalos=6)

table_num_inter = num_inter(num_individuais, amplitude_intervalo)

table = my_table(table_num_inter, amplitude_intervalo)

fi_str, fi = fi(table, amplitude_intervalo, num_individuais, table_num_inter)
table.columns.insert(2, fi_str, header="fi")
print(table)
print("\nSoma de fi == total_de_num:\t", sum(fi), "==", total_de_num)

Fi = Fi(fi)
#print("Frequência absoluta acum (Fi):\t", Fi)
table.columns.insert(3, Fi, header="Fi")
print(table)

fr = fr(fi, amplitude_total)
#print("Frequência relativa (%):\t", fr)
table.columns.insert(4, fr, header="fr")
print(table)
print("Soma de fr tem que dar 100%:\t", sum(fr))


# %%
