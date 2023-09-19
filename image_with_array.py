import numpy as np
import cv2

#crear variable donde se va a guardar
black = np.zeros([600, 600])
#print(black)

#p_fila = black[1:2]
#print(p_fila)

#f_col  = black[:,1:2]
#print(f_col)

black[200:400, 200:400] = 255
print(black)


cv2.imshow("en negro", black)
cv2.waitKey(0)