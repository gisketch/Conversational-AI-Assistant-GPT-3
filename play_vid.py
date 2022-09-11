# importing libraries
import cv2
import numpy as np
import screeninfo
import threading
import random
from clips import Clips

class Video_Player:
    
    def __init__(self, vid_path):
        self.vid_path = vid_path
        self.vid_thread = threading.Thread(target=self.play, args=(self.vid_path,))
        self.vid_thread.start()
        self.screen = screeninfo.get_monitors()[0]
        self.width, self.height = self.screen.width, self.screen.height
        self.is_color = False

    def play(self, vid_path):
        # Create a VideoCapture object and read from input file
        self.cap = cv2.VideoCapture(vid_path)
        
        # Check if camera opened successfully
        if (self.cap.isOpened()== False):
            print("Error opening video file")
        
        # Read until video is completed
        while(self.cap.isOpened()):
            
        # Capture frame-by-frame
            ret, frame = self.cap.read()
            if ret == True:
            # Display the resulting framewindow_name = window_name
                window_name = 'video'
                cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
                cv2.moveWindow(window_name, self.screen.x - 1, self.screen.y - 1)
                cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                                    cv2.WINDOW_FULLSCREEN)
                cv2.imshow(window_name, frame)
                
            # Press w on keyboard to exit
                if cv2.waitKey(int(25)) & 0xFF == ord('w'):
                    break
        
        # Break the loop
            else:
                if(self.vid_path == './clips/listen_transition.mp4'):
                    self.change(Clips.listening())
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
        
        # When everything done, release
        # the video capture object
        self.cap.release()
        
        # Closes all the frames
        cv2.destroyAllWindows()

    def change(self, vid_path):
        self.vid_path = vid_path
        self.cap = cv2.VideoCapture(vid_path) #Change the video
        
