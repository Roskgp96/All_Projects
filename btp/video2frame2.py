import cv

capture = cv.CaptureFromFile("0b21f0579d247c855e05405d3ed805c1#201205251240.flv")
while True:
    # Need a frame to get the output video dimensions
    frame = cv.RetrieveFrame(capture) # Will return None if there are no frames
    print(frame)
    # New video file
    video_out = cv.CreateVideoWriter('frame.jpg', cv.CV_FOURCC('M','J','P','G'), 25, (640,480), 1)
    # Write the frames
    cv.WriteFrame(video_out, frame)
    while False:
        frame = cv.RetrieveFrame(capture) # Will return None if there are no frames
        cv.WriteFrame(video_out, frame)
