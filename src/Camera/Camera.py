import src.Config.config as config
import cv2

class Camera:
    def __init__(self) -> None:
        camera_index = config.camera_idx
        self.cap = cv2.VideoCapture(camera_index)
        self.running = False
        self._frame = None
        
    def run(self):
        self.running = True
        while self.running:
            ret, self._frame = self.cap.read()
            self.running = ret

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        self._frame = value
    
    
