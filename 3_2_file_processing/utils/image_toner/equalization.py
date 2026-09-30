import cv2 as cv

def processing(image):
    if image.ndim == 3:
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(image)
    return dst