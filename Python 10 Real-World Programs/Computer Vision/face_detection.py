import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread(
    "/Users/clcx/Documents/GitHub/My-Python-Learning/Python 10 Real-World Programs/Computer Vision/Pic/Us.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(type(gray_img))
print(gray_img)

faces = face_cascade.detectMultiScale(
    gray_img, scaleFactor=1.05, minNeighbors=10)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow("FACE DETECTION", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
