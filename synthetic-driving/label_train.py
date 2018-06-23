import os

a = open("label_train.txt", "w")

for path, subdirs, files in os.walk('data/train'):
	for filename in files:
		f = str(filename)
		#a.write(f[:-9] + os.linesep)
		
		if f[:2] == "Up":
			a.write(f + ";1,0,0" + os.linesep)
		if f[:2] == "Le":
			a.write(f + ";0,1,0" + os.linesep)
		if f[:2] == "Ri":
			a.write(f + ";0,0,1" + os.linesep)
			'''
		if f[:9] == "n01560419":
			a.write(f + ";0,0,1,0,0" + os.linesep)
		if f[:9] == "n01580077":
			a.write(f + ";0,0,0,1,0" + os.linesep)
		if f[:9] == "n01582220":
			a.write(f + ";0,0,0,0,1" + os.linesep)
			'''
		