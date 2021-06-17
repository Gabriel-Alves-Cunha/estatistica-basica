# %%

from collections import Counter
from itertools import chain
from beautifultable import BeautifulTable
from beautifultable.enums import STYLE_GRID

#%%
def handle_file(file):
    f = open(file)
    array = []
    for line in f:  # read lines
        array.append([int(x) for x in line.split()])
    f.close()
    print("Números no arquivo:\n", array, len(array))
    return array
# file1 = './Exemplos/exemplo 1: Disitribuição de Frequencia Simples.txt'
# handle_file(file1)
#%%

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

    table.set_style(STYLE_GRID)
    print(table)
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


def dados_em_rol(collection_sorted, all_numbers, num_cols, num_rows):
    nums_table = BeautifulTable()
    nums_table.set_style(STYLE_GRID)

    nums = []
    for num, times in collection_sorted:
        #print("num:", num,"\ntimes:", times)
        for _ in range(0, times):
            nums.append(num)

    cols = []

    start_index = 0
    end_index = num_cols

    for _col_number in range(0, num_rows):
        cols.append([x for x in nums[start_index:end_index]])

        start_index += num_cols
        end_index += num_cols

    for i in cols:
        nums_table.rows.append(i)

    print("\nNúmeros em rol:")
    print(nums_table)
    # print(cols)
    assert len(nums) == len(all_numbers)

# Code flow


file1 = './exemplo 1: Disitribuição de Frequencia Simples.txt'
file2 = './exemplo 2: Disitribuição de Frequencia Simples.txt'

array = handle_file(file2)
# For file 2:
num_cols = 10
num_rows = 7

################

all_numbers, num_individuais, total_de_num, collection_sorted = sort_nums(
    array)

dados_em_rol(collection_sorted, all_numbers, num_cols, num_rows)

################

table = my_table(num_individuais)

################

fi = fi(collection_sorted)
#print("\nfi:\t\t\t\t", fi)
soma_de_fi = sum(fi)
table.columns.insert(2, fi, header="fi")
print("\nTabela de frequência (fi = frequência do número):")
print(table)
print("Média de fi =", soma_de_fi/len(fi))
print("Soma de fi == total_de_num:\t", soma_de_fi, "==", total_de_num)

################

Fi = Fi(fi)
# print("Frequência absoluta acum (Fi):\t", Fi)
table.columns.insert(3, Fi, header="Fi")
print("\nFrequência absoluta acumulada do número (Fi)\nFi = soma das frequências do número atual com os anteriores:")
print(table)

################

fri = fri(fi, soma_de_fi)
# print("Frequência relativa (%):\t", fri)
table.columns.insert(4, fri, header="fri (%)")
print("\nFrequência relativa do número (fri)\nfri = ( fi / soma de fi ) * 100:")
print(table)
print("Soma de fri tem que dar 100%:\t", sum(fri))

################

Fri = Fri(Fi)
# print("Frequência relativa acum:\t", Fri)
table.columns.insert(5, Fri, header="Fri (%)")
print("\nFrequência relativa acumulada do número (Fri)\nFri = ( Fi / soma de fi ) * 100:")
print(table)

################

fiX = fiX(num_individuais, fi)
#print("fiX:\t\t\t\t", fiX)
table.columns.insert(6, fiX, header="fiX")
print("\nfiX = Número * fi:")
print(table)
print("Soma de todos os números (fiX):\t\t", sum(fiX))

#############

média = sum(fiX) / soma_de_fi
print("Média (soma de fiX)/(soma de fi):\t", round(média, 6))

# %%
