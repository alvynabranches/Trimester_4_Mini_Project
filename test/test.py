import cv2
import numpy as np

def canny(image):
    _gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _blur = cv2.GaussianBlur(_gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    del _gray, _blur
    return canny

def region_of_interest(image):
    height = image.shape[0]
    triangle = np.array([[(200, height), (1100, height), (550, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, triangle, 255)
    print(f'{height=}\t{triangle.shape=}\t{mask.shape=}')
    del height, triangle
    return mask

image = cv2.imread('./data/test_image.jpg')
lane_image = np.copy(image)
print(f'{image.shape=}\t{lane_image.shape=}')
cv2.imshow("result", region_of_interest(lane_image))
cv2.waitKey(0)