import cv2 as cv
#function to rescale
def rescaleFrame(frame, scale= 0.75):
    width= int(frame.shape[1]*scale)    
    height= int(frame.shape[0]*scale)    

    #shape[1] is width of the frame and shape[0] is height of the frame
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

# read video
capture=cv.VideoCapture(0)
#read frames from video stored in variable capture. works for videos, images, live videos
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame) #original
    cv.imshow('video', frame_resized) #resized

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows
