def train():
	with open('train.txt','r') as file:
		with open('train1.txt','w') as file1:
			with open('train2.txt','w') as file2:
				with open('train3.txt','w') as file3:
					with open('train4.txt','w') as file4:
						for line in file:
							s=line.split(' ')
							l1=[s[0],s[1]]
							l2=[s[0],s[2]]
							l3=[s[0],s[3]]
							l4=[s[0],s[4]]
							file1.write(' '.join(l1))
							file1.write('\n')
							file2.write(' '.join(l2))
							file2.write('\n')
							file3.write(' '.join(l3))
							file3.write('\n')
							file4.write(' '.join(l4))
							#file4.write('\n')
					
def test():
	with open('test.txt','r') as file:
		with open('test1.txt','w') as file1:
			with open('test2.txt','w') as file2:
				with open('test3.txt','w') as file3:
					with open('test4.txt','w') as file4:
						for line in file:
							s=line.split(' ')
							l1=[s[0],s[1]]
							l2=[s[0],s[2]]
							l3=[s[0],s[3]]
							l4=[s[0],s[4]]
							file1.write(' '.join(l1))
							file1.write('\n')
							file2.write(' '.join(l2))
							file2.write('\n')
							file3.write(' '.join(l3))
							file3.write('\n')
							file4.write(' '.join(l4))
							#file4.write('\n')

train()
test()
