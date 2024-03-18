import cv2
import numpy as np

cam = cv2.VideoCapture(0) # 0 is the index of webcam

while cam.isOpened():
    state, frame = cam.read() # frame is out image
    if not state:             # state check if camera works
        print("could not read from webcam 0")
        break
    
    cv2.imshow("webcam0", frame)
    if cv2.waitKey(1) == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
        break