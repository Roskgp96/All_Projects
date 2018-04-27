import cv2
import glob
import re

for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset/Exp1/Pati/short_test_images/*.jpg'):
	print(file)
	x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*/\w*/\w*_\w*_\w*/(.*)",file)
	p=str(x.group(1))
	print(p)
	img=cv2.imread(file)
	img=cv2.resize(img,(160,160))
	cv2.imwrite(str(p),img)
