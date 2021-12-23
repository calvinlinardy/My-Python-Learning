import cv2
import glob

images = [cv2.imread(file) for file in glob.glob(
    "/Users/clcx/Documents/GitHub/My-Python-Learning/Python 10 Real-World Programs/Computer Vision/Pic*.png")]

print(images)

for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imshow("100x100", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, re)
