import cv2
import traceback
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import os

class BoundingBoxDetector:
    """
    A class for detecting bounding boxes around faces in images using a pre-trained deep learning model.
    """

    def __init__(self) -> None:
        """
        Initializes the BoundingBoxDetector object and loads the pre-trained model.

        Returns:
            None
        """
        self.net: cv2.dnn_Net = cv2.dnn.readNet('Models/deploy.prototxt', 'Models/res10_300x300_ssd_iter_140000_fp16.caffemodel')
    
    def detect_faces(self, frame: cv2.UMat) -> cv2.UMat:
        """
        Detects faces in the given frame and returns the frame with bounding boxes drawn around the detected faces.

        Args:
            frame (cv2.UMat): The input frame containing the image to detect faces from.

        Returns:
            cv2.UMat: The input frame with bounding boxes drawn around the detected faces.
        """
        
        blob:cv2.UMat
        detections:cv2.UMat

        try:
            blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
            self.net.setInput(blob)
            detections = self.net.forward()

            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.7:
                    box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                    x, y, w, h = box.astype(int)
                    return x, y, w, h
        
        except Exception as error:
            print('[CRITICAL] could not predict the faces ', str(error), ' ', traceback.print_exc())
    


class KeypointsDetector:
    """
    A class for detecting facial keypoints and blendshapes in images using a pre-trained Mediapipe model.
    """

    def __init__(self) -> None:
        """
        Initializes the KeypointsDetector object and loads the pre-trained model.

        Returns:
            None
        """
        self.model_path: str = 'Models/face_landmarker_v2_with_blendshapes.task'
        base_options: python.BaseOptions = python.BaseOptions(model_asset_path=self.model_path)
        options: vision.FaceLandmarkerOptions = vision.FaceLandmarkerOptions(
            base_options=base_options,
            output_face_blendshapes=True,
            output_facial_transformation_matrixes=True,
            num_faces=1
        )
        self.detector: vision.FaceLandmarker = vision.FaceLandmarker.create_from_options(options)

    def detect_keypoints(self, frame: bytes) -> vision.FaceLandmarker:
        """
        Detects facial keypoints and blendshapes in the given frame.

        Args:
            frame (bytes): The input frame containing the image to detect keypoints from.

        Returns:
            vision.FaceLandmarks: A data structure containing detected facial keypoints and blendshapes.
        """
        mp_image:mp.Image
        detection_result:vision.FaceLandmarker
        try:
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            detection_result = self.detector.detect(mp_image)
            return detection_result
        except Exception as error:
            print('[CRITICAL] could not predict the keypoints ', str(error), ' ', traceback.print_exc())
