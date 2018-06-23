import glob
import cv2
import re



with open('test.txt','r') as file:
	for line in file:
		s=line.split(' ')
		#print(s)
		for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset2/Ground Truth XML/test_images/*.jpg'):
			x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w* \w* \w*/\w*_\w*/(.*)",file)
			p=x.group(1)
			print(s[0],p)
			if (s[0]==p):
				img=cv2.imread(file)
				s[1]=int(s[1])
				s[2]=int(s[2])
				s[3]=int(s[3])
				s[4]=int(s[4])
				img[s[1]:s[1]+s[2],s[4]:s[4]+s[3]]=(255,255,255)
				cv2.imwrite(p,img)

	
