from abc import ABC, abstractmethod
import src.Config.config as config
import cv2

class ValidationTechnique(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.blur_thresh = config.blur_thresh
        self.occlusion_thresh = config.occlusion_thresh
        self.occlusion_model = cv2.dnn.readNet(config.occlusion_model)
        self.left_yawl_thresh = config.left_yawl_max
        self.right_yawl_thresh = config.right_yawl_max
        self.roll_thresh = config.roll_max

    @abstractmethod
    def validate(self, image):
        pass
