import cv2
import numpy as np


img = cv2.imread("bottle.jpg")
cv2.imshow("orig", img)
img = cv2.blur(img,(2,2))
canny = cv2.Canny(img, 0, 50)

cv2.imshow("outline", canny)

cv2.waitKey(0)


## find the non-zero min-max coords of canny
pts = np.argwhere(canny>0)
y1,x1 = pts.min(axis=0)
y2,x2 = pts.max(axis=0)

## crop the region
cropped = img[y1:y2, x1:x2]
cv2.imwrite("cropped.png", cropped)

tagged = cv2.rectangle(img.copy(), (x1,y1), (x2,y2), (0,255,0), 3, cv2.LINE_AA)
cv2.imshow("tagged", tagged)
cv2.waitKey()