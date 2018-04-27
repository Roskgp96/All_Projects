import glob
import re
import cv2
count=0
def train():
	with open('train1.txt','r') as file:
		for line in file:
			s=line.split(' ')
			p=str(s[0])
			if (count<1500):
				for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset/Exp1/Pati/train_images/*.jpg'):
					x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*/\w*/\w*_\w*/(.*)",file)
					name=x.group(1)
				#	#print(item)
					if name==p:
						count=count+1
						#flag=1
						print(count)
						img=cv2.imread(file)
						cv2.imwrite(str(p),img)

def test():
	count=0
	with open('test1.txt','r') as file:
		for line in file:
			s=line.split(' ')
			p=str(s[0])
			if (count<500):
				for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset/Exp1/Pati/test_images/*.jpg'):
					x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*/\w*/\w*_\w*/(.*)",file)
					name=x.group(1)
				#	#print(item)
					if name==p:
						count=count+1
						#flag=1
						#print(count2)
						img=cv2.imread(file)
						cv2.imwrite(str(p),img)
test()
