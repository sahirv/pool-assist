import numpy as np
import cv2

def createGraph():
    # read image - 0 is greyscale, 1 - color
    table_img = cv2.imread('training_sets/tables/example_table.png', 1)
    table_img_col = table_img.copy()
    table_img_grey = cv2.cvtColor(table_img, cv2.COLOR_BGR2GRAY)
    table_orig = table_img_grey.copy()

    # smooth
    table_img_grey = cv2.blur(table_img_grey, (5,5))

    # perform canny edge detection
    table_canny = cv2.Canny(table_img_grey, 20, 40)
    t_c_copy = table_canny.copy();

    # Perform Hough circle transform
    circles = cv2.HoughCircles(table_canny, cv2.HOUGH_GRADIENT, 1, 25, param1=90, param2=30, maxRadius=50, minRadius=8)

    if circles is not None:
        print("Found circles")
        circles = np.round(circles[0, :]).astype("int")
        for x, y, r in circles:
            if r > 30:
                cv2.circle(table_img, (x, y), r, (0, 210, 30), 4)
            else:
                cv2.circle(table_img, (x, y), r, (250, 0, 30), 4)


    #
    # #generate contours
    # table_canny, contours, hierarchy = cv2.findContours(table_canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # #find contour with max area
    # maxArea = 0
    # maxAreaIndex = -1;
    # contourShapes = []
    # for i in range(len(contours) - 1):
    #     cnt = contours[i]
    #     epsilon = 0.01*cv2.arcLength(cnt, True)
    #     approx = cv2.approxPolyDP(cnt, epsilon, True)
    #     contourShapes.append(approx)
    #     area = cv2.contourArea(approx)
    #     if area > maxArea:
    #         maxArea = area
    #         maxAreaIndex = i
    #
    # #draw contours
    # table_contours = cv2.drawContours(table_img, contourShapes, -1, (255,255,255), 3)

    #concatenate before+after images
    img = np.concatenate((table_img_col, table_img), axis=0)

    filename = 'img.png'
    cv2.imwrite(filename, img)
    return filename
