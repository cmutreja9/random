
import cv2
import numpy 

def show_result():
    cap = cv2.VideoCapture('video1') # Give path of video 1
    cap1=cv2.VideoCapture('video2') # Give path of video 2
    x=0
    while(cap.isOpened()):
        num_frames=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
        ret, frame = cap.read()
        ret1,frame1=cap1.read()
        frame.resize(frame1.shape)
        
        
        if x<=num_frames-2:
            both=numpy.hstack((frame,frame1))
            
            cv2.imshow("Result",both)
            
        else:
            break
        
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        x=x+1
    cap.release()
    cap1.release()
    cv2.destroyAllWindows()

show_result()
