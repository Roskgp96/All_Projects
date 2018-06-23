import glob
import cv2
import re
def resiz(file,image):

	BLUE=[0,0,0]
	#print(file)
	img=cv2.imread(file)
	#dim=(320,240)
	#file2=cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
	x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*_\w*/[a-z]*(\d*)_(\d*).*",file)
	i=int(x.group(1))
	j=int(x.group(2))
	#cons= cv2.copyMakeBorder(img,40,40,0,0,cv2.BORDER_CONSTANT,value=BLUE)
	#cv2.imwrite('img2.jpg',constant)
	#cv2.imshow('img',img)
	#cv2.imshow('img',cons)
	img=cv2.resize(image,(240,320))
	cons= cv2.copyMakeBorder(img,40,40,0,0,cv2.BORDER_CONSTANT,value=BLUE)
	small = cv2.resize(cons,(320,320)) 
	cv2.imwrite("framer{}_{}.jpg".format(i,j),small)

	#print(count)

count=0
countt=0

with open('abnormal.txt','w') as wfile:
	with open('test.txt','r') as test:
		for line in test:
			flag=0
			s=line.split(' ')
			
		
	
			for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset2/All_Images/*.jpg'):
				x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*_\w*/(.*)",file)
				
				z=x.group(1)
				#print(z)
				if(z==s[0]):
					flag=1
					image=cv2.imread(file)
					#print(image.shape)
					if image.shape==(240,320,3):
						countt=countt+1
						wfile.write(s[0])
						wfile.write('\n')
						
					if image.shape==(480,640,3):
						#resiz(file,image)
						count=count+1
						#print(count)
					else:
						print(s[0])
			if (flag==0):
				print(s[0])
print(count)
print(countt)
