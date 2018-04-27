import re
def start1():
	with open('outfile2.txt','r') as file:
		with open('outfile3.txt','w') as rfile:
			for line in file:
				s=line.split(' ')
				p=str(s[0])
				x=re.match(r'framer(\d*)_(\d*)',p)
				#print(x.group(1),x.group(2))
				r=int(x.group(2))
				r=r+1
				p='framer'+str(x.group(1))+'_'+str(r)
				s[0]=p
				print(s)
				line=' '.join(s)
				rfile.write(line)

start1()	
#8 230 68 87 319
