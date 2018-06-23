import glob
import cv2
import os


from video2frames import vid2fr
#l=['ac','an','av','cc','cl','cs','ct','da','dr','hm','mk','nn','ppd','pv','zs']

try:
	#print os.environ['PATH']
	i=1
	for file in os.listdir('/home/roshan/Documents/First_Project/btp/Training_Dataset/Videos'):

    	    print(file)
    	    vid2fr(file,i)
    	    i=i+1
except:
	pass
