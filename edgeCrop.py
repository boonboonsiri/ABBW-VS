import cv2
import numpy as np
import os


def cropper(filename,a):
	#resizing images


	resize = cv2.imread('filename', cv2.IMREAD_UNCHANGED)
	 
	 
	scale_percent = 5 # percent of original size
	width = int(resize.shape[1] * scale_percent / 100)
	height = int(resize.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	img = cv2.resize(resize, dim, interpolation = cv2.INTER_AREA)

	#cv2.imshow("img", img)
	#cv2.waitKey()

	# BSetting up blur
	#img = cv2.imread("glass9.jpg") # don't need this anymore
	#cv2.imshow("orig", img)
	toBlur = img
	toBlur = cv2.blur(img,(5,5))
	canny = cv2.Canny(toBlur, 0, 50)

	#cv2.imshow("outline", canny)

	#cv2.waitKey(0)


	## find the non-zero min-max coords of canny
	pts = np.argwhere(canny>0)
	y1,x1 = pts.min(axis=0)
	y2,x2 = pts.max(axis=0)

	## crop the region
	cropped = img[y1:y2, x1:x2]
	cv2.imwrite("cropped_"+a+".png", cropped)

	tagged = cv2.rectangle(img.copy(), (x1,y1), (x2,y2), (0,255,0), 3, cv2.LINE_AA)
	#cv2.imshow("tagged", tagged)
	#cv2.waitKey()

	a = 0
	for f in os.listdir(folder)
		cropper(f,folder)
