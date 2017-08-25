import numpy as np
import cv2

def detectCircle():
    # read image - 0 is greyscale
    table_img = cv2.imread('training_sets/tables/example_table.png', 0)
    #table_img_color = cv2.imread('training_sets/tables/example_table.png', 1)
    # perform canny edge detection
    table_edges = cv2.Canny(table_img, 30, 90)

    #concatenate before+after images
    img = np.concatenate((table_img,table_edges), axis=0)

    filename = 'img.png'
    cv2.imwrite(filename, img)
    return filename
