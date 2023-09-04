import cv2
import streamlit as st

from Detector.Detector import BoundingBoxDetector, KeypointsDetector
from Detector.Detection import Keypoints, BoundingBox
from Validations.Validator import Validator
from Renderer.Render import Render

# Initialize objects for various components
bounding_box_detector = BoundingBoxDetector()
bounding_box_detection = BoundingBox()
keypoints_detector = KeypointsDetector()
keypoints_detection = Keypoints()
render = Render()
validator = Validator()

# Set up Streamlit UI
st.title("Facial Validations")

def process_frame(frame):
    """
    Process a video frame to perform facial validations.

    Args:
        frame (numpy.ndarray): The input video frame.

    Returns:
        numpy.ndarray: The processed video frame with annotations.
        str: Processing status message.
        str: 'True' if the face is valid, 'False' otherwise.
    """
    detected_bounding_box = bounding_box_detector.detect_faces(frame)

    if detected_bounding_box is not None:
        detected_face, face_coords = bounding_box_detection.get_face(frame, detected_bounding_box)
        detected_keypoints = keypoints_detector.detect_keypoints(frame)
        keypoints_coordinates = keypoints_detection.process_keypoints(frame=frame, keypoints=detected_keypoints)

        is_valid, processing_status = validator.validate_face(frame=frame, face=detected_face, keypoints=keypoints_coordinates)
        processed_frame = render.render_all(frame, face_coords, keypoints_coordinates, processing_status, is_valid, False)

        return processed_frame, processing_status, str(is_valid)

    return frame, 'Default', 'False'

if __name__ == "__main__":
    st.write("Welcome to the Facial Validations project, a real-time facial validation tool.")
    st.write("This project uses computer vision techniques to perform various facial validations, including face angle, image blur, and facial occlusions.")
    st.write("You can specify the camera index to access the live camera stream and see the facial validations in action.")

    camera_index = st.number_input("Enter Camera Index", min_value=0, step=1, value=0)

    # Streamlit element to display the processed video frame
    FRAME_WINDOW = st.image([])

    # Open the camera stream
    camera = cv2.VideoCapture(camera_index)

    # Create empty Streamlit elements to hold status and is_valid values
    status_element = st.empty()
    is_valid_element = st.empty()

    while True:
        _, frame = camera.read()
        frame, processing_status, is_valid = process_frame(frame)
        FRAME_WINDOW.image(frame[:, :, ::-1])

        # Update the status and is_valid elements with new values
        status_element.text(f"Processing Status: {processing_status}")
        is_valid_element.text(f"Is Valid: {is_valid}")
