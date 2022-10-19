import cv2
import numpy as np
from matplotlib import pyplot as plt


imagen = cv2.imread("Vision Computacional/Images/cartas.jpg")
escala_gris = cv2.imread("Images/cartas.jpg", cv2.IMREAD_GRAYSCALE)
histograma = cv2.calcHist([escala_gris], [0], None, [256], [0, 256])
color = ['r', 'b', 'g']

for i, c in enumerate(color):
    histograma = cv2.calcHist([imagen], [i], None, [256], [0, 256])
    plt.plot(histograma, color=c)
    plt.xlim([0, 256])
plt.show()