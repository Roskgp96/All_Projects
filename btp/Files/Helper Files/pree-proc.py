import glob
import cv2
import os
import



#l=['ac','an','av','cc','cl','cs','ct','da','dr','hm','mk','nn','ppd','pv','zs']

try:
	#print os.environ['PATH']
	i=1
	for file in os.listdir('/home/roshan/Documents/First_Project/btp/Training_Dataset/Ground Truth XML'):

    	    print(file)
    	    vid2fr(file,i)
    	    i=i+1
except:
	pass
