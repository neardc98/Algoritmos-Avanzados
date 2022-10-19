import cv2
import numpy as np
from matplotlib import pyplot as plt
 
 
imagen = cv2.imread("Vision Computacional/Images/imagencv.jpg")
imagen_modificada = cv2.resize(imagen,(500,500))

color = ['r','b','g']
#enumera los indices
for i,c in enumerate(color):
    histograma =cv2.calcHist([imagen], [i], None,[256], [0,256])
    plt.plot(histograma,color=c)
    plt.xlim([0,256])
    plt.xlabel("intensidad de iluminacion")
    plt.ylabel("cantidad de pixeles")
print(histograma)
plt.show()
print(histograma)