count1=0
count2=0
with open('testhalf.txt','w') as wfile:
	with open('test.txt','r') as file:
		
		for line in file:
			if (count1<500):
				count1=count1+1
				s=line.split(' ')
				s[1]=int(s[1])/2
				s[1]=str(s[1])
				s[2]=int(s[2])/2
				s[2]=str(s[2])
				s[3]=int(s[3])/2
				s[3]=str(s[3])
				s[4]=int(s[4])/2
				s[4]=str(s[4])
				line=' '.join(s)
				wfile.write(line)
				wfile.write('\n')

with open('trainhalf.txt','w') as wfile:
	with open('train.txt','r') as file:
		
		for line in file:
			if (count2<1500):
			
				count2=count2+1
				s=line.split(' ')
				s[1]=int(s[1])/2
				s[1]=str(s[1])
				s[2]=int(s[2])/2
				s[2]=str(s[2])
				s[3]=int(s[3])/2
				s[3]=str(s[3])
				s[4]=int(s[4])/2
				s[4]=str(s[4])
				line=' '.join(s)
				wfile.write(line)
				wfile.write('\n')
