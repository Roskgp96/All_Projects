'''This program is used to sample the video into image frames at a certain fps'''
import numpy as np
import cv2
#import skvideo.io
import sys
import glob
def vid2fr(file,i):

	#cv2.namedWindow("lll")
	cap = cv2.VideoCapture(file)
	#'1bff883d55ca0bbb67351f8169f76914#201011150930_0.flv'
	print('K')

	# Define the codec and create VideoWriter object
	fourcc = cv2.cv.CV_FOURCC('F','L','V','1')
	#fourcc = cv2.VideoWriter_fourcc('F','L','V','1')
	out = cv2.VideoWriter('output.avi',fourcc, 25.0, (640,480))
	print('L')
	count=0

	while(True):
	    ret, frame = cap.read()
	    print('M')
	    print(ret)
	    if ret==True:
	        #frame = cv2.flip(frame,0)
	
	        # write the flipped frame
	        out.write(frame)
	
	        #cv2.imshow('lll',frame)
	        #if cv2.waitKey(1) & 0xFF == ord('q'):
	        #    break
	        count=count+1
		cv2.imwrite("frame%d_%d.jpg" % i % count, frame) 
	    else:
	        break
	print(count)
	# Release everything if job is finished
	cap.release()
	out.release()
	#cv2.destroyAllWindows()	
