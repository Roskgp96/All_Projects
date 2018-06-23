import os
import cv2

#To check what the groundtruth means--Testing purpose
#for file in os.listdir('/home/roshan/Documents/btp/Training_Dataset2/All_Images/'):
#	print(file)
#	if (file=="frame5_3.jpg"):
#		img=cv2.imread(file)
#		cv2.imwrite('img1.jpg',img)
#		img[81:98,206:228]=(0,0,0)
#		cv2.imwrite('img2.jpg',img)

#To check shapes of images
count1=0
count2=0
count3=0

for file in os.listdir('/home/roshan/Documents/btp/Training_Dataset2/All_Images/'):
	print(file)
	if(file=='test.py'):
		continue
	img=cv2.imread(file)
	if(img.shape==(240,320,3)):
		count1=count1+1
		print("1:",count1)
	elif(img.shape==(480,640,3)):
		count2=count2+1
		print("2:",count2)
	else:
		count3=count3+1
		print("3:",count3)
	#img[81:98,206:228]=(0,0,0)
	#cv2.imwrite('img2.jpg',img)

print(count1)
print(count2)
