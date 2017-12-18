"""
@Author: Xiaochen (leavebody) Li 
"""
import cv2


def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def crop_by_limit(img, y, h, x, w):
    return img[y: y + h, x: x + w]