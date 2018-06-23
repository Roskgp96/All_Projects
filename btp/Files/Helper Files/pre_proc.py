import glob
import cv2
import os


from video2frames import vid2fr
#l=['ac','an','av','cc','cl','cs','ct','da','dr','hm','mk','nn','ppd','pv','zs']

try:
	#print os.environ['PATH']
	print('LOL')
	for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset/Videos2/*.flv'):
	    x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*/(/d*).flv",file)
	    i=x.group(1)	
    	    print(file)
    	    vid2fr(file,i)
    	    #i=i+1
except:
	pass
