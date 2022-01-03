import cv2 as cv

img = cv.imread('images/design-pattern-observer.png')
cv.imshow('Diagram', img)
cv.waitKey(0)

# Read a video
""" capture = cv.VideoCapture('Videos/SampleVideo_1280x720_1mb.mp4')

while True :

    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release() """