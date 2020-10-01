#!/usr/bin/env python
# coding: utf-8

import numpy as np
import cv2

point = (0, 0)
pressed = False
color = (0, 255, 0) #Green
radius = 3

def click(event, x, y, flags, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        cv2.circle(canvas, (x, y), radius, color, -1)
    elif event == cv2.EVENT_MOUSEMOVE and pressed:
        cv2.circle(canvas, (x, y), radius, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        pressed = False


canvas = np.ones([500, 500, 3], 'uint8') * 255

cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas', click)

while True:
    cv2.imshow('canvas', canvas)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('b'):
        color = (255, 0, 0)
    elif ch & 0xFF == ord('g'):
        color = (0, 255, 0)
    elif ch & 0xFF == ord('r'):
        color = (0, 0, 255)
    elif ch & 0xFF == ord('w'):
        color = (0, 0, 0)

cv2.destroyAllWindows()


