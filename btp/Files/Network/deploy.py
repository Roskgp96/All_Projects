import numpy as np
import cv2
import caffe

def encoder():
	#To set gpu mode
	caffe.set_device(0)
	caffe.set_mode_gpu()


	net = caffe.Net('network.prototxt', caffe.TEST)
	#printing input layers
	print(net.inputs)
	#net.blobs['data'] and net.blobs['conv']-->to get input and outputs
	#net.params['layer_name'][0]-->weights net.params['layer_name'][1]-->biases
	#Drawing the network
	#python python/draw_net.py examples/net_surgery/conv.prototxt my_net.png
        #open my_net.png
	#Adding an image
	#im = caffe.io.load_image('examples/images/cat.jpg')
	#im = np.array(Image.open('examples/images/cat_gray.jpg'))
	#im_input = im[np.newaxis, np.newaxis, :, :]
	#net.blobs['data'].reshape(*im_input.shape)
	#net.blobs['data'].data[...] = im_input
	#net.forward()
	#net.save('model_name.caffemodel')
	#loading the solver
	solver = caffe.get_solver('solver.prototxt')

	solver.net.forward()  # train net
	#solver.test_nets[0].forward()  # test net (there can be more than one)
	
	solver.net.backward()

	#solver.step(1)

	#solver.solve()
		
	

	




