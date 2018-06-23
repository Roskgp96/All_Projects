def test():
	with open('test.txt','r') as file:
		with open('testt.txt','w') as file1:
			for line in file:
				s=line.split(' ')
				s[1]=str(int(s[1])+40)
				file1.write(' '.join(s))
				#file1.write('\n')

def test1():
	with open('test1.txt','r') as file:
		with open('testt1.txt','w') as file1:
			for line in file:
				s=line.split(' ')
				s[1]=str(int(s[1])+40)
				file1.write(' '.join(s))
				file1.write('\n')

def train():
	with open('train.txt','r') as file:
		with open('trainn.txt','w') as file1:
			for line in file:
				s=line.split(' ')
				s[1]=str(int(s[1])+40)
				file1.write(' '.join(s))
				#file1.write('\n')

def train1():
	with open('train1.txt','r') as file:
		with open('trainn1.txt','w') as file1:
			for line in file:
				s=line.split(' ')
				s[1]=str(int(s[1])+40)
				file1.write(' '.join(s))
				file1.write('\n')

test()
train()
train1()
test1()
				
