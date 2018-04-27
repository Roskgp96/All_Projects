with open('test.txt','r') as file:
	with open('test_names.txt','w') as wfile:
		for line in file:
			s=line.split(' ')
			l=[s[0]]
			wfile.write(' '.join(l))
			wfile.write('\n')
