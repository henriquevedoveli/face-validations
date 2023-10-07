from Detector.Detector import BoundingBoxDetector, KeypointsDetector
from Detector.Detection import Keypoints, BoundingBox

from Camera.frameServer import FrameServer
from Validations.Validator import Validator
from Renderer.Render import Render

import numpy as np
import time
import cv2
import traceback
from typing import List, Tuple, Optional


class VideoProcessor:
    """
    VideoProcessor: A class for processing video frames with face detection and validation.
    """

    def __init__(self, render_keypoints: bool):
        """
        Initialize VideoProcessor instance with required detectors, validators, and renderers.

        Args:
            render_keypoints (bool): Whether to render keypoints on the frames.
        """
        self.bounding_box_detector: BoundingBoxDetector = BoundingBoxDetector()
        self.keypoints_detector: KeypointsDetector = KeypointsDetector()
        self.keypoints_detection: Keypoints = Keypoints()
        self.bounding_box_detection: BoundingBox = BoundingBox()
        self.validator: Validator = Validator()
        self.frame_server: FrameServer = FrameServer()
        self.render: Render = Render()
        self.render_keypoints: bool = render_keypoints

    def process_frame(self, input_frame: np.ndarray) -> np.ndarray:
        """
        Process a single video frame.
        
        Args:
            input_frame (numpy.ndarray): Input video frame to be processed.

        Returns:
            numpy.ndarray: Processed frame with rendered results.
        """
        is_valid: bool
        processing_status: str
        detected_face: np.ndarray
        detected_keypoints: List[Keypoints]
        keypoints_coordinates: List[Tuple[float, float]]
        detected_bounding_box: Optional[BoundingBox]
        
        detected_bounding_box = self.bounding_box_detector.detect_faces(input_frame)

        if detected_bounding_box is not None:
            detected_face, face_coords = self.bounding_box_detection.get_face(input_frame, detected_bounding_box)
            detected_keypoints = self.keypoints_detector.detect_keypoints(input_frame)
            keypoints_coordinates = self.keypoints_detection.process_keypoints(frame=input_frame, keypoints=detected_keypoints)

            is_valid, processing_status = self.validator.validate_face(frame=input_frame, face=detected_face, keypoints=keypoints_coordinates)
            processed_frame = self.render.render_all(input_frame, face_coords, keypoints_coordinates, processing_status, is_valid, self.render_keypoints)

            return processed_frame
        return input_frame

    def run(self) -> None:
        """
        Run the video processing loop.
        """
        self.frame_server.start()

        time.sleep(5)
        try:
            while True:
                img: np.ndarray = self.frame_server.frame
                if img is not None:
                    processed_frame: np.ndarray = self.process_frame(img)
                    show_frame(processed_frame)
                else:
                    show_frame(self.frame_server.frame)

        except Exception as error:
            print("[CRITICAL] Could not capture frame ", str(error), ' ', traceback.print_exc())
            self.frame_server.stop()


def show_frame(frame_array: np.ndarray) -> None:
    """
    Display a frame in a window and allow quitting with 'q' key.

    Args:
        frame_array (numpy.ndarray): Frame to be displayed.
    """
    cv2.imshow('Video Frame', frame_array)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
