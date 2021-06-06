# %%

X = [70, 85, 70, 80, 90]
Y = [60, 90, 60, 90, 80]
C = [85, 80, 85, 90, 90]
W = [90, 60, 90, 80, 75]
peso = [10, 10, 25, 20, 15]


def pesado(peso, lista):
    lista_pesada = []
    for i, num in enumerate(lista):
        lista_pesada.append(num * peso[i])
    print("lista_pesada sum =", sum(lista_pesada))
    print("Média: ", sum(lista_pesada)/sum(peso))


print("Peso sum =", sum(peso))

print("\nX")
pesado(peso, X)

print("\nY")
pesado(peso, Y)

print("\nC")
pesado(peso, C)

print("\nW")
pesado(peso, W)


# %%
