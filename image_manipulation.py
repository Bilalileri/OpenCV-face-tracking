import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True :
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    img = cv2.line(frame, (0,0) , (width,height) , (0,0,255),3) 
    img = cv2.line(img, (0,height) , (width,0) , (0,255,0),3)
    img = cv2.rectangle(img , (height//3 , width//3) , (height//2 , width//2), (90 , 90, 90),3)
    img = cv2.circle(img , (height//2 , width//2) , 120 , (128,128,128), 3)
    font = cv2.FONT_ITALIC
    img = cv2.putText(img , 'Bilal is me', (200 , height-10), font , 2 , (0,0,0),3 , cv2.LINE_AA)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    