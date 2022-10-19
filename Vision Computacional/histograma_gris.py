import cv2
import numpy as np

from matplotlib import pyplot as plt
imagen = cv2.imread('Vision Computacional/Images/images.jpg')

imagen = cv2.resize(imagen,(450,450))
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

cv2.imshow("ima", gris)
cv2.waitKey(0)
#gris = cv2.imread("images.jpg", cv2.IMREAD_GRAYSCALE)
histograma =cv2.calcHist([gris], [0], None,[256], [0,256])

plt.plot(histograma,color='gray')

plt.xlabel("intensidad de iluminacion")

plt.ylabel("cantidad de pixeles")

plt.show()

print((np.mean(histograma))/100)
