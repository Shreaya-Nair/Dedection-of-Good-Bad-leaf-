import cv2
import numpy as np
video = cv2.VideoCapture(0)
while True:
    (grabbed,frame)= video.read()
    if not grabbed:
        break
    blur = cv2.GaussianBlur(frame,(21,21),0)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    lower =[18,50,50]
    upper=[35,255,255]
    lower=np.array(lower,dtype="uint8")
    upper=np.array(upper,dtype="uint8")
    mask=cv2.inRange(hsv,lower, upper)

    output=cv2.bitwise_and(frame,hsv,mask=mask)
    no_red=cv2.countNonZero(mask)
    cv2.imshow("output", output)
    cv2.imshow('original image',frame)

    if(no_red>10 and no_red<100):
        print("good leaf")
    if(no_red>5000 and no_red<100000):
        print("leaf diseas")
    print(int(no_red))
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cv2.destroyAllWindows()
video.release()
