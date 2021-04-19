# %%

import numpy as np
from collections import Counter, defaultdict
from itertools import chain

###########

f = open('./ex.txt')
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
print("Quantos números há:\t\t", sum(fi))

###########

def Fi(fi):
	acc = 0
	soma = []
	for num in fi:
		acc += num
		soma.append(acc)
	return soma


Fi = Fi(fi)
print("Frequência acumulada do número:\t", Fi)

###########



# %%
