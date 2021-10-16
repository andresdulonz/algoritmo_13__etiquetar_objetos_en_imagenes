import cv2
import numpy as np

img = cv2.imread("halloween.png")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask0 = cv2.inRange(hsv,(0,0,25),(0,0,75))

mask = mask0.copy()
cv2.floodFill(mask0,None,(80,300),255)
neg = cv2.bitwise_not(mask0)
im2 = cv2.bitwise_or(neg, mask)

imtype = im2.astype(np.int32)
h,w = imtype.shape

Etiqueta = 0
i = 0
j = 0
for i in range(h):
    for j in range(w):
        if imtype[i,j] == 255:
            Etiqueta = Etiqueta + 1                        
            cv2.floodFill(imtype,None,(j,i),Etiqueta)
               
mask = imtype == 66
im3 = im2.copy()
im3[~mask] = 0

cv2.imwrite('Objeto_2_5.png', im3)
cv2.imshow('Imagen objeto etiquetado',im3)     
cv2.waitKey(0)