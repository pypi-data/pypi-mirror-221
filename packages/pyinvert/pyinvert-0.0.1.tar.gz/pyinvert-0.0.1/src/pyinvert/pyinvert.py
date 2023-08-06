
import numpy as np
import cv2
def invert(image):
    edit = image.copy()
    height, width, channels = edit.shape
    for y in range(0, width):
        for x in range(0, width):
            b, g, r = (edit[x, y])
            invert = [255 - b, 255 - g, 255 - r]
            edit[x,y] = invert
    return edit