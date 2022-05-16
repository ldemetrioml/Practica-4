import cv2
import numpy as np
import matplotlib.pyplot as plt

fondo = cv2.imread('fondo.png', cv2.IMREAD_COLOR)

altura_roi = int(fondo.shape[0]/2)
ancho_roi  = int(fondo.shape[1]/2)

cv2.rectangle(fondo, (10, 10), (altura_roi-10, ancho_roi-10), (255,0,0), 3)
cv2.rectangle(fondo, (20, 20), (altura_roi-20, ancho_roi-20), (0,255,0), 3)
cv2.rectangle(fondo, (30, 30), (altura_roi-30, ancho_roi-30), (0,0,255), 3)
cv2.circle(fondo,(200,23), 10, (255,0,0), -1)
cv2.circle(fondo,(175,23), 10, (255,255,255), -1)


cv2.putText(fondo, 'Ya salio ;)', (45,int(ancho_roi/2)), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)


cv2.imshow('Imagen 1', fondo)

#roi-regionof interest
roi = fondo[0:ancho_roi, 0:altura_roi]
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
