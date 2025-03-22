import cv2 as cv

#image

# img= cv.imread('img/largee.jpg')
# cv.imshow('Dog',img)
# cv.waitKey(0)
 
#video

capture=cv.VideoCapture(0) #here 0 is for camera
#video frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    #if d is pressed them break out of the loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release() #release capture device ie the camera here
cv.destroyAllWindows #destroy all windows we dont need them
#error -215 assertion failed meaning no more frames or wrong address.