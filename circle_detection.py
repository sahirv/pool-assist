import numpy as np
import cv2

def detectCircle():
    img = cv2.imread('training_sets/cue_ball/cb_green_1.png', 1)
    filename = 'img.png'
    cv2.imwrite(filename, img)
    return filename
