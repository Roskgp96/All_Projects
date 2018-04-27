import cv2
#import caffe

def check():
	file='framer5_1.jpg'
	img=cv2.imread(file)
	print(img[161,156])
	img[161:195,156:199]=(0,255,0)
	#img[160:180,0:20]=(255,0,0)
	cv2.imwrite('image.jpg',img)

check()
