import xml.etree.ElementTree as ET
import glob
import cv2
import os
import re



def pick(file,i):
	outfile='oneeach'+str(i)+".txt"
	with open(outfile,'w') as outfile:
		with open (file,'r') as file:
			for line in file:
				if (line[0]=='f'):
					outfile.write(line)
			 

def combine(file):
	with open('outfile.txt','a') as rfile:
		with open(file,'r') as file:
			for line in file:
				rfile.write(line)


def pre_proc():	
	#print os.environ['PATH']
	
	for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset/final_data/*.txt'):

    		print(file)
		#x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*_\w*/output_location(\d*).txt",file)
		#i=x.group(1)
		#print(i)
    		#pick(file,i)
		combine(file)
    		#i=i+1

pre_proc()
