import numpy as np
import cv2


image = cv2.imread("cccc.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)



cv2.imshow("Color Circles", image)
cv2.imshow("Result Imgae",filt)
cv2.imshow("Filtered Image", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
