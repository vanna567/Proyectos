import cv2


img = cv2.imread("butterfly.jpg")

#mostrar con color
cv2.imshow("mariposa", img)

#print(img)
gris = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("escala de grises", gris)
print(gris)

cv2.waitKey(0)