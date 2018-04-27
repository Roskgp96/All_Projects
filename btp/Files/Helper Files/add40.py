with open('test-40.txt','r') as file:
	with open('test.txt','w') as wfile:
		for line in file:
			s=line.split(' ')
			print(s)
			s[1]=str(int(s[1])+40)
		
			x=' '.join(s)
			wfile.write(x)
