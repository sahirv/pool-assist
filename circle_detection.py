import numpy as np
import cv2

from ball_classifier import classifyBall

def createGraph():
    # read image - 0 is greyscale, 1 - color
    table_img = cv2.imread('training_sets/tables/example_table.png', 1)
    table_img_col = table_img.copy()
    table_img_grey = cv2.cvtColor(table_img, cv2.COLOR_BGR2GRAY)
    table_orig = table_img_grey.copy()

    # smooth
    table_img_grey = cv2.blur(table_img_grey, (3,3))

    # perform canny edge detection
    table_canny = cv2.Canny(table_img_grey, 15, 30)
    t_c_copy = table_canny.copy();

    # Perform Hough circle transform
    circles = cv2.HoughCircles(table_canny, cv2.HOUGH_GRADIENT, 1, 25, param1=90, param2=30, maxRadius=50, minRadius=14)

    avgRadius = 0;
    stripes = []
    solids = []
    cueBall = (0,0)
    pockets = []
    if circles is not None:
        print("Found circles")
        circles = np.round(circles[0, :]).astype("int")
        tempRadius = 0;
        for x, y, r in circles:
            if r <= 30:
                # do hue analysis here for cue ball
                tempRadius += r;
        avgRadius = tempRadius // 14


        for x, y, r in circles:
            if r > 30:
                pockets.append([x, y, r])
                cv2.circle(table_img, (x, y), r, (0, 210, 30), 3)
            else:
                # store pixels within circle below
                ball = []
                ballType = classifyBall(ball)
                if ballType == "stripe":
                    stripes.append((x, y))
                elif ballType == "solid":
                    solids.append((x, y))
                elif ballType == "cue":
                    cueBall = (x, y)
                else:
                    raise Exception("Ball can not be classified. X= " + x + " Y= " + y)
                cv2.circle(table_img, (x, y), avgRadius, (250, 0, 30), 3)

    #concatenate before+after images

    img = np.concatenate((table_img_col, cv2.cvtColor(t_c_copy, cv2.COLOR_GRAY2BGR), table_img), axis=0)

    filename = 'img.png'
    cv2.imwrite(filename, img)
    return filename