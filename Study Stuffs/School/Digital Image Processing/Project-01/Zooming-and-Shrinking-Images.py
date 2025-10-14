import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("rose.jpeg")

bil_int = cv2.resize(img,None,fx=100,fy=100,interpolation=cv2.INTER_LINEAR)

cv2.imshow(bil_int)