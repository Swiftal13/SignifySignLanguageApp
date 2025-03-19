import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def getFrame(self):
        ret, frame = self.cap.read() # Read the frame from the camera
        if not ret or frame is None:
            return None
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert the frame from BGR to RGB
        return frame
        
    def release(self):
        self.cap.release() 
        


        