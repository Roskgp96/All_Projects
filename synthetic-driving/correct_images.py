import cv2
import numpy as np 
import os

#a = open("label_train.txt", "w")

for path, subdirs, files in os.walk('data/train'):
	for filename in files:
		f = str(filename)
		
		if f[:2] == "Up" or if f[:2] == "Le" or if f[:2] == "Ri":
			im = cv2.imread("/home/somnath/synthetic_driving/data/train/"+filename)
			cv2.imwrite(im,"/home/somnath/synthetic_driving/data/train2/"+filename)