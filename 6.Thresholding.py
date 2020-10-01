import numpy as np
import cv2

bw = cv2.imread('./images/Geneva_Emotion_Wheel_-_English.png', 0)
height, width = bw.shape
cv2.imshow("Black & White", bw)

thresh = 250 # Guess

# binary = np.ones([height, width, 1], 'uint8')
# for row in range(0, height):
#     for col in range(0, width):
#         if bw[row][col] > thresh:
#             binary[row][col] = 255
# cv2.imshow("Slow binary", binary)

ret, threshold = cv2.threshold(bw, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow("CV Threshold", threshold)

#This is a simple approach which will fail with various lightning.

cv2.waitKey(0)
cv2.destroyAllWindows()