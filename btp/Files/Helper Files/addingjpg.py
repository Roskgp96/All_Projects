import cv2
import re

with open('test.txt','r') as file:
	with open('test10.txt','w') as wfile:
		for line in file:
			s=line.split(' ')
			#print(len(s))
			#print(s)
			s[0]=s[0]+'.jpg'
			l=[s[0],s[1],s[3],s[7],s[9]]
			x=' '.join(l)
			wfile.write(x)
			if (len(s)==12):
				wfile.write('\n')



