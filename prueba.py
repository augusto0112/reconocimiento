import numpy as np
import cv2

##Primer tutorial
img = cv2.imread('/home/cristian/Escritorio/reconocimiento/imgs/rostro.jpg',0)
cv2.imshow('Rostro',img)

k = cv2.waitKey(0)

#Sale de la ventana
if k == ord('e'):
    cv2.destroyAllWindows()

#Convierte la imagen en grises
elif k == ord('s'):
    cv2.imwrite('/home/cristian/Escritorio/reconocimiento/imgs/rostrodos.png',img)
    cv2.destroyAllWindows()


##Segundo tutorial
cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()

    cv2.imshow('video1', frame)
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break

cap.release()
cv2.destroyAllWindows()
