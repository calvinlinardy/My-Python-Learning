import cv2
import glob

images = glob.glob(
    "/Users/clcx/Documents/GitHub/My-Python-Learning/Python 10 Real-World Programs/Computer Vision/Pic/*.jpg")

print(images)
print(type(images))

for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imshow("100x100", re)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #cv2.imwrite("resized_"+image, re)
