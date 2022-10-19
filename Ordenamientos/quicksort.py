def particionado(lista):
    pivote = lista[0]
    mayor = []
    menor = []
    for i in range(1, len(lista)):
        if lista[i] > pivote:
            mayor.append(lista[i])
        else:
            menor.append(lista[i])
    return menor, pivote, mayor


def quicksort(lista):
    if len(lista) < 2:
        return lista

    menor, pivote, mayor = particionado(lista)
    print("Iteracion: ", lista)
    return quicksort(menor)+[pivote]+quicksort(mayor)


lista = [7, 5, 3, 12, 9, 12, 10, 4, 3, 8]
print("Desordenada: ", lista)
print("Ordenada: ", quicksort(lista))
