import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    """Image and video resizing function
        You can use with images, video and live video

    Args:
        frame ([type]): Image or video read
        scale (float, optional): Scale to video or image resize. Defaults to 0.75.

    Returns:
        [type]: Resized image or video
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions  = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

def changeRes(width, height):
    #Only use from live video
    capture.set(3, width)
    capture.set(4, height)

img = cv.imread('images/design-pattern-observer.png')
cv.imshow('Diagram', img)

resized_image = rescaleFrame(img)
cv.imshow('Image_resized', resized_image)

cv.waitKey(0)

# Read a video
capture = cv.VideoCapture('Videos/SampleVideo_1280x720_1mb.mp4')

while True :

    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()