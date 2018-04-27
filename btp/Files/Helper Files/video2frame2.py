import cv

capture = cv.CaptureFromFile("sub_0a38e6a322d62fbff33d614c17d8547c#201108200950_2.flv")
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
