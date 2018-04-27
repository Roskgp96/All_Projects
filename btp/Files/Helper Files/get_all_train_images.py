import glob
import cv2
import re

with open('annotated_test.txt','r') as file:
	#flag=0
	s=[]
	#with open('train.txt','r') as test:
	for line in file:
		#print(line)
		flag=0
		s=line.split(' ')
		#if flag==2:
			#break;
	#print(s)
		for file in glob.iglob('/home/roshan/Documents/btp_spring/All_Images/*.jpg'):
			x=re.match(r"/\w*/\w*/\w*/\w*_\w*/\w*_\w*/(.*)",file)
		
			z=x.group(1)
			if (z==s[0]):
				#image=cv2.imread(file)
				#cv2.imwrite(s[0],image)
				flag=1
				
		if (flag==0):
			print(s[0])
				
				
	#print(flag)
		
		
		
	
	'''for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset2/All_Images/*.jpg'):
		x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*_\w*/(.*)",file)
		
		z=x.group(1)
		#print(z)
		if(z==s[0]):
			flag=1
			image=cv2.imread(file)
			#print(image.shape)
			if image.shape==(240,320,3):
				resiz(file,image)
				countt=countt+1
				
					
			if image.shape==(480,640,3):
				wfile.write(s[0])
				wfile.write('\n')
				
				count=count+1
				#print(count)
			else:
				print(s[0])
	if (flag==0):
		print(s[0])
print(count)
print(countt)'''
