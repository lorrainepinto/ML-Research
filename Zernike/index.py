# import the necessary packages
from Zernike import ZernikeMoments
from imutils.paths import list_images
import numpy as np
import argparse
import pickle
import imutils
import cv2
desc = ZernikeMoments(10)
index = {}
path1 = "C:\\Users\\pinto\\Desktop\\DTlabz\\ML\\DHCD\\test\\36\\2365.png"
path3 = "C:\\Users\\pinto\\Desktop\\DTlabz\\ML\\DHCD\\test\\36\\2367.png"
path2 = "C:\\Users\\pinto\\Desktop\\DTlabz\\ML\\DHCD\\test\\38\\2631.png"
# img_path = "C:\\Users\\pinto\\Desktop\\DTlabz\\ML\\DHCD\\test\\36\\"
for i in [path1,path2,path3]:
    # img_paths = img_path + str(i) + ".png"
    print(i)
    image = cv2.imread(i)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # pad the image with extra white pixels to ensure the
    # edges of the pokemon are not up against the borders
    # of the image
    image = cv2.copyMakeBorder(image, 15, 15, 15, 15,cv2.BORDER_CONSTANT, value = 255)
    # invert the image and threshold it
    thresh = cv2.bitwise_not(image)
    # thresh[thresh > 0] = 255
    # cv2.imshow("LOlo",thresh)
    # cv2.waitKey(0)

    # initialize the outline image, find the outermost
    # contours (the outline) of the pokemone, then draw
    # it

    # outline = np.zeros(image.shape, dtype = "uint8")
    # cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    # cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
    # cv2.drawContours(outline, [cnts], -1, 255, -1)
    # cv2.imshow("lol",outline)
    # cv2.waitKey(0)
    #
    moments = desc.describe(thresh)
    print(moments)

