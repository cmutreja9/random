import numpy as np
import cv2

cap = cv2.VideoCapture(0)


fourcc = cv2.cv.CV_FOURCC('M','P','4','2')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print "exiting.."
            break
    else:
        break
 


cap.release()
out.release()
cv2.destroyAllWindows()
