# %%

import math


def get_cols_from_file(file_name):
    f = open(file_name)

    lines = []

    for line in f:
        lines.append(line.split())
    f.close()

    cols_tuple = zip(*lines)
    cols_str = list(map(list, cols_tuple))

    cols = []
    for col in cols_str:
        col = [int(num_str) for num_str in col]
        cols.append(col)

    return cols


def amplitude(list):
    print(max(list), min(list))
    return max(list) - min(list)


def média(list):
    return round(sum(list)/len(list), 2)


def variance(list):
    list_sq = []
    for num in list:
        list_sq.append(num*num)

    length = len(list)
    sum_of_x_sq = sum(list_sq)
    sum_sq_of_x = sum(list) * sum(list)
    n_minus_1 = length - 1

    return round(((sum_of_x_sq - sum_sq_of_x / length) / n_minus_1), 2)


def desvio_padrão(variance):
    return round(math.sqrt(variance), 2)


def erro_padrão_da_média(desvio_padrão, length):
    return round(desvio_padrão / math.sqrt(length), 2)


def coef_de_variação(desvio_padrão, média):
    return round((desvio_padrão/média), 3)*100


file1 = "./exemplos/exemplo 1: Dispersão de dados.txt"
file2 = "./exemplos/exemplo 2: Dispersão de dados.txt"
file3 = "./exemplos/exemplo 3: Dispersão de dados.txt"

cols = get_cols_from_file(file1)

amplitudes = []
for col_index in range(len(cols)):
    amplitudes.append(amplitude(cols[col_index]))
print("Amplitudes:\t\t", amplitudes)

médias = []
for col_index in range(len(cols)):
    médias.append(média(cols[col_index]))
print("Médias:\t\t\t", médias)

variância_S2 = []
for col_index in range(len(cols)):
    variância_S2.append(variance(cols[col_index]))
print("Variâncias S2:\t\t", variância_S2)

desvios_padrões = []
for col_index in range(len(variância_S2)):
    desvios_padrões.append(desvio_padrão(variância_S2[col_index]))
print("Desvios padrões (s):\t", desvios_padrões)

erros_padrões_de_média = []
for col_index in range(len(desvios_padrões)):
    erros_padrões_de_média.append(erro_padrão_da_média(
        desvios_padrões[col_index], len(cols[0])))
print("Erro padrão de média:\t", erros_padrões_de_média)

coefs_de_variação = []
for col_index in range(len(desvios_padrões)):
    coefs_de_variação.append(coef_de_variação(
        desvios_padrões[col_index], médias[col_index]))
print("Coefs de variação (%):\t", coefs_de_variação)


# %%
