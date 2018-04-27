import xml.etree.ElementTree as ET
import glob
import cv2
import os
import re

def parse(file,i):
	try:
		outfile='output_location'+str(i)+'.txt'
		outfile1='output_species'+str(i)+'.txt'
		with open(outfile1,'w') as wfile1:
			with open(outfile,'w') as wfile:
				tree=ET.parse(file)
				root=tree.getroot()
				for item in root:
					print (item,item.attrib)
					#wfile.write(str(item))
					x=str(item.attrib)
					y=re.match(r"{'id': '(\d*)'}",x)
					item.attrib=y.group(1)
					wfile.write(str(item.attrib))
					wfile1.write(str(item.attrib))
					wfile.write('\t')
					wfile1.write('\t')
					for obj in item:
						print(obj,obj.attrib)
						#wfile.write(str(obj))
						x=str(obj.attrib)
						z=re.match(r"{'y': '(\d*)', 'h': '(\d*)', 'fish_species': '(\w* \w*)', 'w': '(\d*)', 'x': '(\d*)'}",x)
						y=z.group(1)
						h=z.group(2)
						species=z.group(3)
						w=z.group(4)
						x=z.group(5)
						wfile.write(str(y))
						wfile.write('\t')
						wfile.write(str(h))
						wfile.write('\t')
						wfile.write(str(w))
						wfile.write('\t')
						wfile.write(str(x))
						wfile.write('\t')
						wfile.write('\n')
						wfile1.write(species)
						wfile1.write('\n')
	except:
		pass
def parse2(file,i):
	outfile='output_locationn'+str(i)+'.txt'
	#outfile1='output_species'+str(i)+'.txt'
	
	with open(outfile,'w') as wfile:
		tree=ET.parse(file)
		root=tree.getroot()
		for item in root:
			print (item,item.attrib)
			#wfile.write(str(item))
			#x=str(item.attrib)
			#y=re.match(r"{'id': '(\d*)'}",x)
			#item.attrib=y.group(1)
			wfile.write(str(item.attrib))
			#wfile1.write(str(item.attrib))
			wfile.write('\t')
			#wfile1.write('\t')
			for obj in item:
				print(obj,obj.attrib)
				#wfile.write(str(obj))
				#x=str(obj.attrib)
				#z=re.match(r"{'y': '(\d*)', 'h': '(\d*)', 'fish_species': '(\w* \w*)', 'w': '(\d*)', 'x': '(\d*)'}",x)
				#y=z.group(1)
				#h=z.group(2)
				#species=z.group(3)
				#w=z.group(4)
				#x=z.group(5)
				wfile.write(str(obj.attrib))
				#wfile1.write('\n')
				#wfile.write('\t')
				#wfile1.write(species)
				wfile.write('\n')
				#wfile.write('\t')
def pre_proc():	
	#print os.environ['PATH']
	
	for file in glob.iglob('/home/roshan/Documents/btp/Training_Dataset/Ground Truth XML/*.xml'):

    		print(file)
		x=re.match(r"/\w*/\w*/\w*/\w*/\w*_\w*/\w* \w* \w*/(\d*).xml",file)
		i=x.group(1)
		print(i)
    		parse2(file,i)
    		#i=i+1
def trial():
	x={'id': '23'}
	
	y=re.match(r"{'id': '(\d*)'}",str(x))
	print(str(y.group(1)))
	x={'y': '105', 'h': '70', 'fish_species': 'Dascyllus Aruanus', 'w': '71', 'x': '33'}
	z=re.match(r"{'y': '(\d*)', 'h': '(\d*)', 'fish_species': '(\w* \w*)', 'w': '(\d*)', 'x': '(\d*)'}",str(x))
	y=z.group(1)
	h=z.group(2)
	species=z.group(3)
	w=z.group(4)
	x=z.group(5)
	print(int(y),int(h),int(w),int(x),species)
#trial()	
#pre_proc()
parse2('1.xml',1)
	
