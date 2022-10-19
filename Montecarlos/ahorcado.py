import random

def imprimir(listaActual):
    print(' '.join(listaActual))

max_intentos = 5
listaPalabras = ['amor', 'boda', 'adivinanza', 'amarillo', 'silla', 'telefono', 'ballena', 'radio', 'automovil']

palabraEscogida = random.choice(listaPalabras)
listaLetras = list(palabraEscogida)
longLista = len(listaLetras) # longitud de la palabra
lista_ = ['_' for j in range(longLista)] # Lista de guiones bajos [_, _, _, ...]

imprimir(lista_)
ganador = False
contador = 0
while max_intentos > 0:
    letra = input(f"Intentos [{max_intentos}] - Introduce una letra: ")
    acierto = False
    for i in range(longLista):
        if listaLetras[i] == letra:
            lista_[i] = letra # reemplaza _ por la letra actual
            contador += 1
            acierto = True
    if not acierto: # La letra no está
        max_intentos -= 1
    imprimir(lista_)
    if contador == longLista: # Se adivinaron todas la letras
        ganador = True
        break
        
if ganador:
    print(" *** Ganaste el juego ***")
else:
    print(f"[!] Perdiste el juego, la palabra era: {palabraEscogida}")