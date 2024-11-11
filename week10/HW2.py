import cv2
import numpy as np

cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    
    frame= cv2.flip(frame,0)
    frame= cv2.flip(frame,1)
    
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([15, 150, 150])   
    upper_yellow = np.array([35, 255, 255])  
    lower_white = np.array([0, 0, 180])     
    upper_white = np.array([180, 25, 255])   

    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_white = cv2.inRange(hsv, lower_white, upper_white)

    mask = cv2.bitwise_or(mask_yellow, mask_white)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    result = np.zeros_like(frame)
    result[mask > 0] = frame[mask > 0]

    cv2.imshow('Result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
