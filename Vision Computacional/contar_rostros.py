import cv2
import numpy
from matplotlib import pyplot as plt 

imagen_c = cv2.imread("Vision Computacional/Images/img3.jpg")
imagen = cv2.imread("Vision Computacional/Images/img3.jpg", cv2.IMREAD_GRAYSCALE)
bordes = cv2.Canny(imagen,100, 400)

contorno, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#[30, 255, 0] leda el color de los contornos 
cv2.drawContours(imagen_c, contorno, -1, [30, 255, 0],2)

print("numero de contornos encontrados : ", len(contorno))
texto = "contornos encontrados "+ str(len(contorno))

cv2.putText(imagen_c, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),1)
cv2.imshow("bordes", bordes)
cv2.imshow("Imagen gris", imagen)
cv2.imshow("Imagen color", imagen_c)
cv2.waitKey(0)
