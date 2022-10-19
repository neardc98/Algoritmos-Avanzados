from operator import itemgetter

#Paquetes: "Nombre del paquete", Kilos, Precio
PAQUETES = (
    ("Paquete 1", 9, 150), ("Paquete 2", 9, 160), ("Paquete 3", 153, 200), ("Paquete 4", 50, 160),
    ("Paquete 5", 15, 60), ("Paquete 6", 66, 45), ("Paquete 7", 27, 60), ("Paquete 8", 39, 40),
    ("Paquete 9", 230, 591), ("Paquete 10", 520, 10), ("Paquete 11", 110, 70), ("Paquete 12", 32, 30))

#carga máxima del camión
PESOMAXIMO = 230

# Útiles para acceso al peso y valores (irían mejor definiendo una clase)
get_peso = itemgetter(1)
get_valor = itemgetter(2)

def total_peso(paquetes):
    return sum(get_peso(x) for x in paquetes)

def total_valor(paquetes):
    return sum(get_valor(x) for x in paquetes)

# Obtención de todas las combinaciones posibles
# Función recursiva
def combinaciones(paquetes, peso_maximo):
    paqs = [ p for p in paquetes if get_peso(p) <= peso_maximo ]
    resultado = []
    for p in paqs:
        res = combinaciones([x for x in paqs if x!=p], peso_maximo - get_peso(p))
        if len(res) == 0:
            resultado.append([p])
        else:
            resultado.extend([[p]+x for x in res])
    return resultado

# solución
print (max(combinaciones(PAQUETES, PESOMAXIMO), key=total_valor))