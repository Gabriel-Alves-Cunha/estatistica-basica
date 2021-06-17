# %%

from collections import Counter
from itertools import chain
from beautifultable import BeautifulTable
from beautifultable.enums import STYLE_GRID
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
    collection_sorted = sorted(num_counted.items())
    print("Collection sorted:\t\t", collection_sorted)
    num_individuais = sorted([key for key, value in collection_sorted])
    total_de_num = len(all_numbers)
    print("\nNúmeros únicos ordenados:\t", num_individuais)
    print("Total de números:\t\t", total_de_num)

    return all_numbers, num_individuais, total_de_num, collection_sorted


def amplitude(num_individuais, num_de_classes):
    amplitude_total = max(num_individuais) - min(num_individuais)
    print("Amplitude total (AT) = valor máximo encontrado menos valor mínimo:", amplitude_total)

    amplitude_intervalo = int(amplitude_total / num_de_classes)
    print("Amplitude do intervalo (H) = amplitude total / número de classes: ", amplitude_intervalo)

    return amplitude_total, amplitude_intervalo


def num_inter(num_individuais, amplitude_intervalo):
    table_num_inter = []
    begin_num = num_individuais[0]
    table_num_inter.append(begin_num)
    rng = range(int(amplitude_total/amplitude_intervalo))
    #print("rng =", rng)

    for _ in rng:
        begin_num += amplitude_intervalo
        table_num_inter.append(begin_num)

    print("table_num_inter:", table_num_inter)
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


def fi(num_de_classes, all_numbers, table_num_inter, amplitude_intervalo):
    times = []
    rng = num_de_classes

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
        arr_to_append = [x for x in nums[start_index:end_index]]
        if len(arr_to_append) < num_cols:
            for i in range(0,(num_cols-len(arr_to_append))):
                arr_to_append.append("")
        cols.append(arr_to_append)
        start_index += num_cols
        end_index += num_cols

    #print(cols)
    for i in cols:
        #print(i)
        nums_table.rows.append(i)

    print("\nNúmeros em rol:")
    print(nums_table)
    print()
    assert len(nums) == len(all_numbers)


# Code flow

file1 = './Exemplos/exemplo 1: Disitribuição de Frequencia de Classe com Raiz.txt'
file2 = './Exemplos/exemplo 2: Disitribuição de Frequencia de Classe com Raiz.txt'

array = handle_file(file2)
# For file 2:
num_cols = 10
num_rows = 15

################

all_numbers, num_individuais, total_de_num, collection_sorted = sort_nums(
    array)

num_de_classes = math.ceil(math.sqrt(total_de_num))
print("Número de classes:\t\t", num_de_classes)

dados_em_rol(collection_sorted, all_numbers, num_cols, num_rows)

################

amplitude_total, amplitude_intervalo = amplitude(
    num_individuais, num_de_classes)

################

table_num_inter = num_inter(num_individuais, amplitude_intervalo)

table = my_table(table_num_inter, num_de_classes, amplitude_intervalo)

################

fi_str, fi = fi(num_de_classes, all_numbers,
                table_num_inter, amplitude_intervalo)
table.columns.insert(2, fi_str, header="fi")
print("\nA tabela de frequência (fi = frequência do número) nos diz quantos números há em uma designada faixa de valores:")
print(table)
#print("\nfi:\t\t\t\t", fi)
print("""

x |---- y Significa fechado no inicio e aberto no final (o número x faz parte da classe e o número y não).
x ----| y Significa aberto no início e fechado no final (o número x não faz parte da classe e o número y faz).
x |---| y Significa fechado no início e no final (o número x e y fazem parte da classe). Sempre a utilizamos na última classe para contemplar todos os valores encontrados na pesquisa.

""")
print("Média de fi =", sum(fi)/len(fi))
print("Soma de fi == total_de_num:\t", sum(fi), "==", total_de_num)

################

Fi = Fi(fi)
table.columns.insert(3, Fi, header="Fi")
#print("Frequência absoluta acum (Fi):\t", Fi)
print("""
Frequência absoluta acumulada do número (Fi)
Fi = soma das frequências do número atual com os anteriores.
Ela representa a soma de todas as frequências até o ponto presente no conjunto de dados:""")
print(table)

################

fri = fri(fi, total_de_num)
#print("Frequência relativa (%):\t", fri)
table.columns.insert(4, fri, header="fri (%)")
print("""
Frequência relativa do número (fri)
fri = ( fi / soma de fi ) * 100. É a porcentagem de um determinado valor na amostra:""")
print(table)
print("Soma de fri tem que dar 100%:\t", sum(fri))

################

Fri = Fri(fri)
#print("Frequência relativa acum:\t", Fri)
table.columns.insert(5, Fri, header="Fri (%)")
print("""
Frequência relativa acumulada do número (Fri)
Fri = ( Fi / soma de fi ) * 100.
Ela representa a soma de todas as frequências relativas até o ponto presente no conjunto de dados:""")
print(table)

# %%
