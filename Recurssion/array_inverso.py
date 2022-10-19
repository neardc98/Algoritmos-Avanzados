# Funcion recursiva para imprimir un array 
# funcion que toma dos argumentos: el array y donde tiene que comenzar
# si se pone -1 lo imprime de forma inversa, por defecto se imprime de forma normal
def Recorrer(array, i = 0):
    if i == len(array): #caso base cuando se quiere el array impreso de forma no inversa
        return 1
    elif i < -len(array): # caso base cuando se quiere el array impreso de forma inversa
        return 0
    else:
        print(array[i], end = '-')
        if i < 0: # cuando se quiere imprimir forma inversa
            return Recorrer(array, i-1)
        else: 
            
            return Recorrer(array, i+1) # cuando se quiere imprimir de forma normal
array = [1,2,5,6,3,9,8,7]
print ('Array normal\n',array)

print('Impreso de forma normal')
Recorrer(array)

print('\nImpreso de forma inversa')
Recorrer(array,-1)