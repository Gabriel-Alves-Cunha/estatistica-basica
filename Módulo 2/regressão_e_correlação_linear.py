# %%


from beautifultable import BeautifulTable
from beautifultable.enums import STYLE_GRID
from math import sqrt
from numpy import sign


def handle_file(file):
    f = open(file)
    array = []
    for line in f:  # read lines
        array.append([float(x) for x in line.split()])
    f.close()
    # print("Números no arquivo: ", array, len(array))
    return array


def give_me_the_numbers_in_2_arrays(array):
    x_values = []
    y_values = []

    for line_array in array:
        x_values.append(line_array[0])
        y_values.append(line_array[1])

    # print(x_values)
    # print(y_values)

    return x_values, y_values


def my_table_with_x_and_y(x_values, y_values, x_name, y_name):
    table = BeautifulTable()

    table.columns.append(x_values, header=x_name)
    table.columns.append(y_values, header=y_name)

    table.set_style(STYLE_GRID)
    # print(table)
    return table


def table_with_x2_and_y2_and_xy(table, x_values, y_values):
    x2 = []
    for x in x_values:
        x2.append(x*x)

    y2 = []
    for y in y_values:
        y2.append(y*y)

    xy = []
    for i, x in enumerate(x_values):
        y = y_values[i]
        xy.append(x*y)

    table.columns.append(x2, header="x²")
    table.columns.append(y2, header="y²")
    table.columns.append(xy, header="x * y")

    print(table)


def table_of_sums(table):
    x = table.columns[0]
    y = table.columns[1]
    x2 = table.columns[2]
    y2 = table.columns[3]
    xy = table.columns[4]

    table_of_sums = BeautifulTable()
    table_of_sums.set_style(STYLE_GRID)

    table_of_sums.rows.append(["", "x", "y", "x²", "y²", "x * y"])
    table_of_sums.rows.append(
        ["Soma", sum(x), sum(y), sum(x2), sum(y2), sum(xy)])

    print(table_of_sums)

    return table_of_sums


def coeff_de_correlação(sums_table, size):
    soma_de_x = (sums_table.rows[1])[1]
    soma_de_y = (sums_table.rows[1])[2]
    soma_de_x2 = (sums_table.rows[1])[3]
    soma_de_y2 = (sums_table.rows[1])[4]
    soma_de_xy = (sums_table.rows[1])[5]

    soma_de_x_2 = soma_de_x*soma_de_x
    soma_de_y_2 = soma_de_y*soma_de_y

    numerador = soma_de_xy - ((soma_de_x * soma_de_y) / size)

    denominador_termo_1 = soma_de_x2 - (soma_de_x_2 / size)
    denominador_termo_2 = soma_de_y2 - (soma_de_y_2 / size)

    r = numerador / sqrt(denominador_termo_1 * denominador_termo_2)

    assert -1 < r < 1

    return r


def coeff_de_regressão(sums_table, size):
    soma_de_x = (sums_table.rows[1])[1]
    soma_de_y = (sums_table.rows[1])[2]
    soma_de_x2 = (sums_table.rows[1])[3]
    soma_de_xy = (sums_table.rows[1])[5]

    soma_de_x_2 = soma_de_x*soma_de_x

    numerador = soma_de_xy - ((soma_de_x * soma_de_y) / size)

    denominador = soma_de_x2 - (soma_de_x_2 / size)

    b = numerador / denominador

    a = (soma_de_y / size) - (b * (soma_de_x / size))

    sign_b = "+" if sign(b) > 0 else "-"

    print(f"Equação de regressão linear: y = {a} {sign_b} {abs(b)}x")


##############

file1 = "./exemplos/exemplo 1: Regressão e correlação linear.txt"
header_x_file_1 = "(Poluentes) ppm"
header_y_file_1 = "ID água (%)"

file2 = "./exemplos/exemplo 2: Regressão e correlação linear.txt"
header_x_file_2 = "Liga (%)"
header_y_file_2 = "Resistência (kg/f)"

file3 = "./exemplos/exemplo 3: Regressão e correlação linear.txt"
header_x_file_3 = "(Poluentes)ppm"
header_y_file_3 = "ID água (%)"

file4 = "./exemplos/exemplo 4: Regressão e correlação linear.txt"
header_x_file_4 = "Liga (%)"
header_y_file_4 = "Resistência (kg/f)"

file5 = "./exemplos/exemplo 5: Regressão e correlação linear.txt"
header_x_file_5 = "X"
header_y_file_5 = "Y"

file6 = "./exemplos/exemplo 6: Regressão e correlação linear.txt"
header_x_file_6 = "X"
header_y_file_6 = "Y"

array = handle_file(file4)
# print(array)

x_values, y_values = give_me_the_numbers_in_2_arrays(
    array)

table = my_table_with_x_and_y(
    x_values, y_values, header_x_file_4, header_y_file_4)

table_with_x2_and_y2_and_xy(table, x_values, y_values)

sums_table = table_of_sums(table)

r = coeff_de_correlação(sums_table, len(x_values))
print("r =", r)
print("r² =", r*r)

reg = coeff_de_regressão(sums_table, len(x_values))

# %%
