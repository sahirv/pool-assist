import numpy as np
import cv2

img = cv2.imread('training_sets/cue_ball/cb_green_1.png', 1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()