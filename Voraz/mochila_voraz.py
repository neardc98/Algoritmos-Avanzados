def mochila(peso_maximo, peso_objeto, valores, n):
    K = [[0 for x in range(peso_maximo + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for peso_maximo in range(peso_maximo + 1):
            if i == 0 or peso_maximo == 0:
                K[i][peso_maximo] = 0
            elif peso_objeto[i-1] <= peso_maximo:
                K[i][peso_maximo] = max(valores[i-1]
                                        + K[i-1][peso_maximo-peso_objeto[i-1]],
                                        K[i-1][peso_maximo])
            else:
                K[i][peso_maximo] = K[i-1][peso_maximo]

    return K[n][peso_maximo]


valores = [1, 2, 1, 2, 2.50, 5, 3, 2, 3, 5, 3]
peso_objeto = [1, 2, 1, 4, 4, 4, 2, 2,3, 1, 2]
peso_maximo = 6
n = len(valores)
print('El valor maximo en un peso de 6kg es de: ',
      mochila(peso_maximo, peso_objeto, valores, n))
