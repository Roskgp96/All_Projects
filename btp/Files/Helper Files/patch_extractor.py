import numpy as np
import cv2 as cv
def extract(file):
	img=cv.imread(file)
	patch_size=6
	count=0
	for i in 0:patch_size:img.shape[0]:
		for j in 0:patch_size:img.shape[1]:
			patch_image=img[i:i+patch_size,j:j+patch_size]
			cv2.imwrite('patch{}.jpg'.format(count),patch_image
			count=count+1
def main():
	file='image.jpg'
	exract(file)

for __name__=="__main__""
	main()
			
    
    

