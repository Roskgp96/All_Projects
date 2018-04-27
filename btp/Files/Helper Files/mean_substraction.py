import cv2
import glob
import re
import numpy as np

for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset/Exp1/Pati/train_images2/*.jpg'):
	print(file)
	x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*/\w*/\w*_\w*/(.*)",file)
	p=str(x.group(1))
	print(p)
	img=cv2.imread(file)
	img=img-np.mean(img)
	cv2.imwrite(str(p),img)
