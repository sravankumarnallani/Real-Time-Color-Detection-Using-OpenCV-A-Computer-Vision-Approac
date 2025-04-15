import cv2
import numpy as np

cap = cv2.VideoCapture(0)
boundaries = [([45, 100, 50], [75, 255, 255]), ([94, 80, 2], [126, 255, 255]), ([170, 70, 50], [180, 255, 255])]
while (True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array(boundaries[0][0])
    upper_green = np.array(boundaries[0][1])
    lower_red = np.array(boundaries[1][0])
    upper_red = np.array(boundaries[1][1])
    lower_red2 = np.array(boundaries[2][0])
    upper_red2 = np.array(boundaries[2][1])
    mask1 = cv2.inRange(hsv, lower_green, upper_green)
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask3 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 | mask2 | mask3
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    # cv2.imshow("mask",mask)
    cv2.imshow("res", res)
    k = cv2.waitKey(60) & 0xFF
    if k == 27:
        cap.release()
        cv2.destroyAllWindows()
        break



