import numpy as np
import cv2
import random

img = cv2.imread('./images/fuzzy.png', 1)
# cv2.imshow("Original", img)

#1. Turn to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)

thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
# cv2. imshow("Binary", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

filtered = []

for c in contours:
    if cv2.contourArea(c) < 1000: continue
    filtered.append(c)
print(len(filtered))


objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')
for f in filtered:
    col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(objects, [f], -1, col, -1)
    area = cv2.contourArea(f)
    perimeter = cv2.arcLength(f, True)
    print(f"Area: {area}, Perimeter: {perimeter}")

cv2.imshow("Contours", objects)
cv2.waitKey(0)
cv2.destroyAllWindows()