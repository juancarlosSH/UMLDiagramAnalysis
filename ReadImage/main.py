import cv2 as cv

img = cv.imread('images/design-pattern-observer.png')
cv.imshow('Diagram', img)
cv.waitKey(0)

""" capture = cv.VideoCapture(0)
while True :
    isTrue, frame = capture.read()
    cv.imshow('WebCam', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows() """