import numpy as np
import cv2

img = cv2.imread('./images/tomatoes.jpg', 1)
edges = cv2.Canny(img, 100, 70)
cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()