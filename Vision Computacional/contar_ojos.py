import cv2

def detec_eyes(eyes):
    '''Dibuja un rectángulo alrededor de los ojos'''
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#  Cargar cascade
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

#  Leer la imagen de entrada
img = cv2.imread('Vision Computacional/Images/Friends.jpg')

#  Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#  Detectar los ojos
eyes = eye_cascade.detectMultiScale(gray, 1.3, 4)

#  Llamar a la funcion dectec_eyes
detec_eyes(eyes)

#  Visualizar el resultado
cv2.imshow('Imgen', img)
cv2.waitKey()