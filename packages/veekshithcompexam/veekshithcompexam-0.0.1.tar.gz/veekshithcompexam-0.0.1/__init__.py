import cv2 as cv
import numpy as np


def read(img_path, vid_path):
    img = cv.imread(img_path)
    cv.imshow('Img', img)

    cv.waitKey(0)

    # Reading Videos
    capture = cv.VideoCapture(vid_path)

    while True:
        isTrue, frame = capture.read() 
        if isTrue:    
            cv.imshow('Video', frame)
            if cv.waitKey(20) & 0xFF==ord('d'):
                break            
        else:
            break

    capture.release()
    cv.destroyAllWindows()


def rescale(img_path, vid_path):
    def rescaleFrame(frame, scale=0.75):
        # Images, Videos and Live Video
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)

        dimensions = (width,height)

        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    img = cv.imread(img_path)
    reimg = rescaleFrame(img, scale=.2)
    cv.imshow('img', img)
    cv.imshow('Rescaled_img', reimg)
    cv.waitKey(0)    
    # Reading Videos
    capture = cv.VideoCapture(vid_path)

    while True:
        isTrue, frame = capture.read()

        frame_resized = rescaleFrame(frame, scale=.2)
    
        cv.imshow('Video', frame)
        cv.imshow('Video Resized', frame_resized)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()

def draw(name):
    blank = np.zeros((500,500,3), dtype='uint8')
    cv.imshow('Blank', blank)

    # 1. Paint the image a certain colour
    blank[200:300, 300:400] = 0,0,255
    cv.imshow('Green', blank)

    # 2. Draw a Rectangle
    cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
    cv.imshow('Rectangle', blank)

    # 3. Draw A circle
    cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
    cv.imshow('Circle', blank)

    # 4. Draw a line
    cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
    cv.imshow('Line', blank)

    # 5. Write text
    cv.putText(blank, 'Hello, im '+str(name), (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), 2)
    cv.imshow('Text', blank)

    cv.waitKey(0)