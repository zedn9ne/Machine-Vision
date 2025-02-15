import cv2 as cv
from PIL import Image
from util import get_limits

yellow = [0,255,255]
cap = cv.VideoCapture(0)

while True:
    isTrue ,frame = cap.read()
    
    hsvImage = cv.cvtColor(frame , cv.COLOR_BGR2HSV)

    lowerLimit , upperLimit = get_limits(color=yellow)

    mask = cv.inRange(hsvImage, lowerLimit , upperLimit)
    
    mask_ = Image.fromarray(mask)
    
    bbox = mask_.getbbox()
    
    if bbox is not None :
        x1 , y1 , x2 , y2 = bbox
        frame = cv.rectangle(frame , (x1,y1),(x2,y2),(0,255,0),5)
    
    cv.imshow("Frame" , frame)

    if cv.waitKey(1) & 0xfff == ord('q'):
        break;
cap.release()
cv.destroyAllWindows()