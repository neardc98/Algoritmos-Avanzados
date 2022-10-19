import cv2
import random


def Agregar_Ruido(imagen):
    fila, columna = imagen.shape
    numero_pixeles = random.randint(300, 10000)
    for i in range(numero_pixeles):
        y_coord = random.randint(0, fila-1)
        x_coord = random.randint(0, columna-1)
        imagen[y_coord][x_coord] = 255

    numero_pixeles = random.randint(300, 10000)
    for i in range(numero_pixeles):
        y_coord = random.randint(0, fila-1)
        x_coord = random.randint(0, columna-1)
        imagen[y_coord][x_coord] = 0

    return imagen


imagen = cv2.imread("Vision Computacional/Images/img1.jpg", cv2.IMREAD_GRAYSCALE)
imagen_ruido = Agregar_Ruido(imagen)
cv2.imshow("", imagen)
cv2.waitKey(0)
