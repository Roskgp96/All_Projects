


import xml.etree.ElementTree as ET
import glob
import cv2
import os
import re

def half(file,p):
	#out='outputrr_'+str(p)+'.txt'
	with open(file,'r') as file:
		with open('out_half.txt','w') as wfile:
			for line in file:
				s=line.split(' ')
				#s[0]='frame'+str(p)+'_'+str(int(s[1])+1)+'.jpg'
				s[2]=str(int(s[2])/2)
				s[4]=str(int(s[4])/2)
				s[8]=str(int(s[8])/2)
				s[10]=str(int(s[10])/2)
				l=[s[0],s[2],s[4],s[8],s[10]]
				wfile.write(' '.join(l))
				wfile.write('\n')
				#print(s)


def combine(file):
	with open('outfile.txt','a') as rfile:
		with open(file,'r') as file:
			for line in file:
				rfile.write(line)




def pre_proc():	
	#print os.environ['PATH']
	
	for file in os.listdir('/home/roshan/Documents/btp/Training_Dataset2/Ground Truth XML/large'):

    		
		if (file[0]=='o'):
			print(file)
			x=re.match(r"(\w*)_(\d*).txt",file)
			p=x.group(2)
			#print(p)
			#pickk(file,p)
			#half(file,p)
			combine(file)
half('outfile.txt',0)
#pre_proc()
