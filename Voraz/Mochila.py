def mochila(maximo_peso, peso_objeto, valores_objeto, n):
    if n == 0 or maximo_peso == 0:
        return 0
    if (peso_objeto[n-1] > maximo_peso):
        return mochila(maximo_peso, peso_objeto, valores_objeto, n-1)
    else:
        return max(
            valores_objeto[n-1] + mochila(
                maximo_peso-peso_objeto[n-1], peso_objeto, valores_objeto, n-1),
            mochila(maximo_peso, peso_objeto, valores_objeto, n-1))


valores_objeto = [1, 2, 1, 2, 2.50, 5, 3, 2, 3, 5, 3]
peso_objeto =    [1, 2, 1, 4, 4, 4, 2, 2, 3, 1, 2]
maximo_peso = 6
n = len(valores_objeto)
print("El costo es de: ", mochila(maximo_peso, peso_objeto,
      valores_objeto, n), "Si puede llevar solo 50")
