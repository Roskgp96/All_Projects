import glob
import cv2
import re
def resiz(file):

	BLUE=[0,0,0]
	print(file)
	img=cv2.imread(file)
	#dim=(320,240)
	#file2=cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
	x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*/\w*_\w*/[a-z]*(\d*)_(\d*).*",file)
	i=int(x.group(1))
	j=int(x.group(2))
	cons= cv2.copyMakeBorder(img,40,40,0,0,cv2.BORDER_CONSTANT,value=BLUE)
	#cv2.imwrite('img2.jpg',constant)
	#cv2.imshow('img',img)
	#cv2.imshow('img',cons)
	small = cv2.resize(cons,(320,320)) 
	cv2.imwrite("framer{}_{}.jpg".format(i,j),small)

	print(count)

count=0
countt=0
for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset/Exp1/train_images/*.jpg'):
	image=cv2.imread(file)
	print(image.shape)
	if image.shape==(320,320,3):
		countt=countt+1

	if image.shape==(560,640,3):
		#resiz(file)
		count=count+1
		
print(count)
print(countt)
