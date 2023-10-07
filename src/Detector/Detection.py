import math
import numpy as np
from typing import List, Dict, Tuple
from mediapipe.framework.formats import landmark_pb2

class BoundingBox:
    """
    BoundingBox class for processing bounding box coordinates and extracting faces from frames.

    Args:
        resize_factor (float, optional): The factor by which to resize the bounding box. Defaults to 1.1.
    """

    def __init__(self, resize_factor: float = 1.1) -> None:
        """
        Initialize the BoundingBox object.

        Args:
            resize_factor (float, optional): The factor by which to resize the bounding box. Defaults to 1.1.
        """
        self._resize_factor: float = resize_factor

    def _calculate_resized_coords(
        self, x: int, y: int, w: int, h: int
    ) -> Tuple[int, int, int, int]:
        """
        Calculate the resized coordinates of a bounding box.

        Args:
            x (int): x-coordinate of the bounding box.
            y (int): y-coordinate of the bounding box.
            w (int): Width of the bounding box.
            h (int): Height of the bounding box.

        Returns:
            tuple[int, int, int, int]: Resized bounding box coordinates (x, y, width, height).
        """
        new_w: float = w * self._resize_factor
        new_h: float = h * self._resize_factor
        new_x: float = x - (new_w - w) / 2
        new_y: float = y - (new_h - h) / 2
        return int(new_x), int(new_y), int(new_w), int(new_h)

    def get_face(
        self, frame: np.ndarray, detections: Tuple[int, int, int, int]
    ) -> Tuple[np.ndarray, Tuple[int, int, int, int]]:
        """
        Extract a face from a frame using bounding box coordinates.

        Args:
            frame (np.ndarray): The input image frame.
            detections (tuple[int, int, int, int]): Bounding box coordinates (x, y, width, height).

        Returns:
            tuple[np.ndarray, tuple[int, int, int, int]]: Cropped face image and new bounding box coordinates.
        """
        if detections is not None:
            x, y, w, h = detections
            new_x, new_y, new_w, new_h = self._calculate_resized_coords(x, y, w, h)
            cropped_image = frame[new_y : new_y + new_h, new_x : new_x + new_w]
            new_coords = new_x, new_y, new_w, new_h
            return cropped_image, new_coords
            
class Keypoints:
    def __init__(self):
        self.landmarks = {
            'l_eye': {'left': 33, 'right': 133, 'top': 159, 'bottom': 145},
            'r_eye': {'left': 362, 'right': 359, 'top': 386, 'bottom': 374},
            'face': {'left': 127, 'right': 356, 'top': 10, 'bottom': 152}
        }

    @staticmethod
    def _normalized_to_pixel_coordinates(normalized_x, normalized_y, image_width, image_height):
        def is_valid_normalized_value(value):
            return 0 <= value <= 1 or math.isclose(value, 0) or math.isclose(value, 1)

        if not (is_valid_normalized_value(normalized_x) and is_valid_normalized_value(normalized_y)):
            return None

        x_px = min(math.floor(normalized_x * image_width), image_width - 1)
        y_px = min(math.floor(normalized_y * image_height), image_height - 1)
        return x_px, y_px

    @staticmethod
    def _normalize_keypoints(landmarks_proto, indices):
        normalized_landmarks = landmark_pb2.NormalizedLandmarkList()
        for idx in indices:
            normalized_landmarks.landmark.extend([
                landmark_pb2.NormalizedLandmark(
                    x=landmarks_proto[idx].x,
                    y=landmarks_proto[idx].y,
                    z=landmarks_proto[idx].z
                )
            ])
        return normalized_landmarks

    def _get_landmark_coord(self, landmarks_proto, landmark_dict):
        landmark_coord = {}

        for idx, landmark in enumerate(landmarks_proto.landmark):
            landmark_px = self._normalized_to_pixel_coordinates(
                landmark.x, landmark.y, self.image_cols, self.image_rows
            )
            if landmark_px:
                landmark_coord[list(landmark_dict)[idx]] = landmark_px

        return landmark_coord

    def process_keypoints(self, frame, keypoints):
        self.image_rows, self.image_cols, _ = frame.shape
        face_landmarks_list = keypoints.face_landmarks
        for idx in range(len(face_landmarks_list)):
            face_landmarks = face_landmarks_list[idx]

            face_indices = self.landmarks['face'].values()
            r_eye_indices = self.landmarks['r_eye'].values()
            l_eye_indices = self.landmarks['l_eye'].values()

            face_landmarks_proto = self._normalize_keypoints(face_landmarks, face_indices)
            r_eyes_landmarks_proto = self._normalize_keypoints(face_landmarks, r_eye_indices)
            l_eyes_landmarks_proto = self._normalize_keypoints(face_landmarks, l_eye_indices)

            facial_coord = self._get_landmark_coord(face_landmarks_proto, self.landmarks['face'])
            l_eye_coord = self._get_landmark_coord(l_eyes_landmarks_proto, self.landmarks['l_eye'])
            r_eye_coord = self._get_landmark_coord(r_eyes_landmarks_proto, self.landmarks['r_eye'])

            return [facial_coord, l_eye_coord, r_eye_coord]
