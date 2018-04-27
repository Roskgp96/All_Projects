import glob
import cv2
import re
import sys
'''Some changes are done to the annotated_test.txt as well as to the annotated_train.txt files'''
'''eg: ChaetodonSpeculum :Chaetodon Speculum  etc)'''

with open('annotated_train.txt','r') as file1:
	#flag=0
	s=[]
	#with open('train.txt','r') as test:
	for line in file1:
		#print(line)
		flag=0
		s=line.split(' ')
		#print(s)
		if s:
			q=str(s[0])[:-4]
			p=q+'.txt'
			#print(p)
			if (s[6]=="Abudefduf"):
				s[6]='1'
			elif (s[6]=="Acanthurus" or s[6]=="Acanturus"):
				s[6]='2'
			elif (s[6]=="Amphiprion" or s[6]=="Ampiprion"):
				s[6]='3'
			elif (s[6]=="Chaetodon"and s[7]=="Lununatus"):
				s[6]='4'
			elif (s[6]=="Chaetodon" and s[7]=="Speculum"):
				s[6]='5'
			elif (s[6]=="Chaetodon" and s[7]=="Trifascialis"):
				s[6]='6'
			elif (s[6]=="Chromis" or s[6]=="Cromis"):
				s[6]='7'
			elif (s[6]=="Dascyllus" and s[7]=="Aruanus"):
				s[6]='8'
			elif (s[6]=="Dascyllus" and s[7]=="Reticulatus"):
				s[6]='9'
			elif (s[6]=="Hemigymnus"):
				s[6]='10'
			elif (s[6]=="Myripristis" or s[6]=="Mripristis"):
				s[6]='11'
			elif (s[6]=="Neoglyphidodon"):
				s[6]='12'
			elif (s[6]=="Pempheris" or s[6]=="Pemperis"):
				s[6]='13'
			elif (s[6]=="Zebrasoma"):
				s[6]='15'
			elif (s[6]=="Plectrogl-Pidodon"):
				s[6]='14'
			else:
				print(s[6])
			
			
			with open('train.txt',"a") as file:
				#file2.write('sos')
				#l=str(s[6]+' '+s[2]+' '+s[4]+' '+s[9]+' '+s[11])
				#print(l)
				file.write(q)
				file.write('\n')
			
		#if flag==2:
			#break;
	#print(s)
		'''for file in glob.iglob('/home/roshan/Documents/btp_spring/All_Images/*.jpg'):
			x=re.match(r"/\w*/\w*/\w*/\w*_\w*/\w*_\w*/(.*)",file)
		
			z=x.group(1)
			if (z==s[0]):
				#image=cv2.imread(file)
				#cv2.imwrite(s[0],image)
				flag=1
				
		if (flag==0):
			print(s[0])
				
				
	#print(flag)
		
		
		
	
	for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset2/All_Images/*.jpg'):
		x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w*_\w*/(.*)",file)
		
		z=x.group(1)
		#print(z)
		if(z==s[0]):
			flag=1
			image=cv2.imread(file)
			#print(image.shape)
			if image.shape==(240,320,3):
				resiz(file,image)
				countt=countt+1
				
					
			if image.shape==(480,640,3):
				wfile.write(s[0])
				wfile.write('\n')
				
				count=count+1
				#print(count)
			else:
				print(s[0])
	if (flag==0):
		print(s[0])
print(count)
print(countt)'''
