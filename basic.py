import cv2 as cv

img = cv.imread('images/design-pattern-observer.png')

cv.imshow('Diagram', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Dilating image
dilated = cv.dilate(img, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

# Eroding image
eroded = cv.erode(img, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
