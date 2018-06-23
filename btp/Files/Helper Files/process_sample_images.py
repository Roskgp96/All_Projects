import cv2 as cv
def process(filename,key,k):
    try:
        img=cv.imread(filename)
    #print img.shape
        img2=cv.resize(img,(32,32))
        cv.imweite('image{}{}.jpg'.format(key,k),img2)
        print(key)
    except:
        pass
    #print img2.shape
    #cv.imshow("xyz",img2)
    #cv.waitKey(0)
