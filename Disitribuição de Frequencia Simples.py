# %%

from collections import Counter, defaultdict
from itertools import chain

###########

f = open('./exemplo: Disitribuição de Frequencia Simples.txt')
array = []
for line in f:  # read lines
    array.append([int(x) for x in line.split()])
f.close()

###########

all_numbers = list(chain(*array))
num_counted = Counter(all_numbers)
#print(num_counted)
num_sorted = sorted(num_counted.items())
print("Collection:\t\t\t", num_sorted)
num_individuais = sorted([key for key, value in num_sorted])

print("\nNúmeros únicos:\t\t\t", num_individuais)

###########

fi = [value for key, value in num_sorted]
print("Frequência do número (fi):\t", fi)
soma_de_fi = sum(fi)
print("Quantos números há:\t\t", soma_de_fi)

###########

def Fi(fi):
	acc = 0
	soma = []
	for num in fi:
		acc += num
		soma.append(acc)
	return soma


Fi = Fi(fi)
print("Freq acumulada do número (Fi):\t", Fi)

###########

def fri(fi):
	ret = []
	for i in fi:
		ret.append(round(i/soma_de_fi * 100, 2))
	return ret

fri = fri(fi)
print("Freq relativa do num (fri %):\t", fri)
print("Soma da fri tem que dar 100:\t", sum(fri), "%")

############

def Fri(Fi):
	ret = []
	for i in Fi:
		ret.append(round(i/soma_de_fi * 100, 2))
	return ret

Fri = Fri(Fi)
print("Freq rel acum do num (Fri %):\t", Fri)

############

def fiX(num_individuais, fi):
	ret = []
	for index, num in enumerate(num_individuais):
		ret.append(num * fi[index])
	return ret

fiX = fiX(num_individuais, fi)
print("fiX:\t\t\t\t", fiX)
print("Soma de todos os números:\t", sum(fiX))

#############

média = sum(fiX) / sum(fi)
print("Média:\t\t\t\t", round(média, 6))

# %%
