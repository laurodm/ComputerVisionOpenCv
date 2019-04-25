import cv2
from calculateArea import CalculateArea
from distance import Distance

cam = cv2.VideoCapture(0)
cv2.namedWindow("Cam")

while True:
    ret, frame = cam.read()
    cv2.imshow("Cam", frame)
    if not ret:
        break
    
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    
    elif k%256 == 32:
        # SPACE pressed
        # get distance
        dist = Distance()
        objDistance = dist.getDistance()
        print(objDistance)
        # take picture
        img_name = "to_meansure.png"
        cv2.imwrite(img_name, frame)
        cv2.destroyWindow('Cam')
        # start calc
        calc = CalculateArea()
        calc.measure(objDistance)
        break

cam.release()
