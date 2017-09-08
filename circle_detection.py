import numpy as np
import cv2
import scipy.spatial

from ball_classifier import classifyBall

def findCircles():
    # read image - 0 is greyscale, 1 - color
    table_img = cv2.imread('training_sets/tables/extable6.png', 1)
    table_img_col = table_img.copy()
    table_img_grey = cv2.cvtColor(table_img, cv2.COLOR_BGR2GRAY)
    table_orig = table_img_grey.copy()

    # smooth
    table_img_grey = cv2.blur(table_img_grey, (3,3))

    # perform canny edge detection
    table_canny = cv2.Canny(table_img_grey, 15, 30)
    t_c_copy = table_canny.copy()

    # Perform Hough circle transform
    circles = cv2.HoughCircles(table_canny, cv2.HOUGH_GRADIENT, 1, 25, param1=90, param2=30, maxRadius=50, minRadius=14)

    avgObjRadius = 0
    stripes = []
    solids = []
    cueBall = (0,0)
    pockets = []
    if circles is not None:
        print("Found circles")
        circles = np.round(circles[0, :]).astype("int")
        totAvgRadius = sum(i[2] for i in circles) // len(circles)
        objBallCounter = 0
        for x, y, r in circles:
            if r <= totAvgRadius:
                objBallCounter += 1
                avgObjRadius += r
        avgObjRadius = avgObjRadius // objBallCounter
        for x, y, r in circles:
            if r > 30:
                pockets.append([x, y, r])
                cv2.circle(table_img, (x, y), r, (0, 210, 30), 3)
            else:
                # store pixels within circle below
                ball = isolateBall(x, y, avgObjRadius, table_img)
                ballType = classifyBall(ball)
                if ballType == "stripe":
                    stripes.append((x, y))
                elif ballType == "solid":
                    solids.append((x, y))
                elif ballType == "cue":
                    cueBall = (x, y)
                else:
                    raise Exception("Ball can not be classified. X= " + x + " Y= " + y)
                cv2.circle(table_img, (x, y), avgObjRadius, (150, 100, 255), 4)

    #concatenate before+after images

    img = np.concatenate((table_img_col, cv2.cvtColor(t_c_copy, cv2.COLOR_GRAY2BGR), table_img), axis=0)

    filename = 'img.png'
    cv2.imwrite(filename, img)
    return filename

def isolateBall(x, y, r, img):
    height, width = img.shape[:2]
    mask = np.zeros((height, width, 3), np.uint8)
    height1, width1 = mask.shape[:2]
    ball = []
    for i in range(x - r, x + r): # columns (width)
        for j in range(y - r, y + r): # rows (height)
            if (scipy.spatial.distance.euclidean([x,y], [i,j]) < r):
                mask[j][i] = img[j][i]
    return mask
