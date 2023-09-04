import cv2
import numpy as np

class Render:
    def __init__(self):
        #TODO Documentar essa desgraca
        #TODO Colocar as cores no construtor
        self.rectangle_opacity = 0.3
        self.green = (0, 255, 0)
        self.red = (0, 0, 255)
        self.blue = (255, 0, 0)
        self.rectangle_thickness = 1

    def render_all(self, frame, bb_detection, keypoints_coords, status, is_validated, render_keypoints):
        if render_keypoints:
            frame = self._draw_keypoints(image = frame, keypoints_list=keypoints_coords)
        frame = self._draw_bounding_box(image=frame, face_coords=bb_detection, is_ok=is_validated)
        return frame

    def _draw_keypoints(self, image, keypoints_list):
        if keypoints_list is not None:
            for keypoints in keypoints_list:
                points_to_draw = ['left', 'right', 'top', 'bottom']
                for point_key in points_to_draw:
                    try:
                        image = cv2.circle(image, keypoints[point_key], 2, self.blue , 2)
                    except:
                        pass
        return image


    def _draw_bounding_box(self, image, face_coords, is_ok):
        frame = image
        x, y, w, h = face_coords
        color = self.green if is_ok else self.red
        return cv2.rectangle(frame, (x, y), (w, h), color, 3)

    def _write_status(self, image, status):
        status_texts = {
            "Distance": "Too far or too close",
            "ANGLE": "Readjust the angle of the face",
            "OCCLUSION": "Remove occlusion from face",
            "Liviness": "",
            "BLUR": "",
            "default": "",
            "OK": "OK"
        }
        
        text = status_texts[status]
        x, y = 100, 100

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 255, 255)
        font_thickness = 2

        return cv2.putText(image, text, (x, y), font, font_scale, font_color, font_thickness)
