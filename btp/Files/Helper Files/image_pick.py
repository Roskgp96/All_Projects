import cv2
import glob
import re

lis=[]
def image_pick():
	count=0
	count2=0
	count3=0	
	with open('outfile3.txt','r') as file:
		for line in file:
			s=line.split(' ')
			count=count+1
			s[0]=s[0].replace('\t','')
			#print(s[0],s[1])
			item=str(s[0])+'.jpg'
			item=str(item)
			#lis.append(s)
			print(item)
			flag=0
			for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset/Videos1/square_frames/*.jpg'):
				x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*\d/\w*_\w*/(.*)",file)
				name=x.group(1)
			#	#print(item)
				if name==item:
					count2=count2+1
					flag=1
					#print(count2)
					img=cv2.imread(file)
					cv2.imwrite(str(item),img)
				else:
					count3=count3+1
					
			if (flag==0):
				print(item)
				lis.append(item)		
					
		print(count)
		#print(count3)
	with open('newfile.txt','w') as file:
		for item in lis:
			file.write(item)
def imag(lis):
	
	count2=0
	count3=0
	for item in lis:
		for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset/Videos1/square_frames/*.jpg'):
			x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*\d/\w*_\w*/(.*)",file)
			name=x.group(1)
			print(item)
			if name==item:
				count2=count2+1
				print(count2)
				img=cv2.imread(file)
				cv2.imwrite(str(item),img)
			else:
				count3=count3+1
				print(count3)
def trial():
	item='framer7_5.jpg'
	for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset/Videos1/square_frames/*.jpg'):
		x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*\d/\w*_\w*/(.*)",file)
		name=x.group(1)
		if name==item:
			print('match')
			img=cv2.imread(file)
			cv2.imwrite(str(item),img)
def prl(lis):
	newlis=[]
	for item in lis:
		if item not in newlis:
			newlis.append(item)
	for item in newlis:
		print(item)
		
	
image_pick()
#prl(lis)
#imag(lis)
#trial()
