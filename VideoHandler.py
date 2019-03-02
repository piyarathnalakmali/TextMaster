import cv2
import numpy as np
import os
import math


class VideoHandler:
    def __init__(self):
        return None
    def splitVideo(self,video):

        images= []
        # Playing video from file:
        cap = cv2.VideoCapture(video.path)

        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except OSError:
            print ('Error: Creating directory of data')

        frameRate = cap.get(5) #frame rate
        currentFrame = 0
        while(True):
            frameId = cap.get(1) #current frame number
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Saves image of the current frame in jpg file
            if (frameId % math.floor(frameRate) == 0):
                name = './data/frame' + str(currentFrame) + '.jpg'
                print ('Creating...' + name)
                cv2.imwrite(name, frame)
                images.append('frame'+str(currentFrame) + '.jpg')

                # To stop duplicate images
                currentFrame += 1
                print (images)

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        print ("done")

    def splitVideo2(self,video):

        images =[]
        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except OSError:
            print ('Error: Creating directory of data')

        cap = cv2.VideoCapture(video.path)
        frameRate = cap.get(5) #frame rate
        x=1
        while(cap.isOpened()):
            frameId = cap.get(1) #current frame number
            ret, frame = cap.read()
            if (ret != True):
                break
            if (frameId % math.floor(frameRate) == 0):
                filename = './data/frame' +  str(int(x)) + ".jpg";
                images.append('frame'+str(int(x)) + '.jpg')
                x+=1
                cv2.imwrite(filename, frame)

        cap.release()
        print ("Done!")
        print (images)

    def playVideo(self,video):

        cap = cv2.VideoCapture(video.path)
        '''
        Make sure your_video is in the same dir, else mention the full path.
        '''
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',frame)
            cv2.imshow('grayF',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                 break

        cap.release()
        cv2.destroyAllWindows()
