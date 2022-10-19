num = int(input("Ingrese el numero de filas:"))
  
for n in range(num):
    print(' '*(num-n), end='')

    print(' '.join(map(str, str(11**n))))