import glob
import cv2



from process import process
l=['ac','an','av','cc','cl','cs','ct','da','dr','hm','mk','nn','ppd','pv','zs']

for (j,item) in enumerate(l):

    for (i,image_file) in enumerate(glob.glob('home/roshan/Documents/First_Project/btp/Training_ Dataset/Species_Samples/*.png')):
        #process(image_file,j,i)
	print("K")
	print(image_file)
	if (i>4):
		break
