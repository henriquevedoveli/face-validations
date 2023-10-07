from src.Camera.Camera import Camera
import threading
from typing import Optional, Tuple

class FrameServer:
    """
    A class representing a frame server that handles camera operations.
    """
    def __init__(self) -> None:
        """
        Initialize the FrameServer instance.

        Attributes:
            camera (Camera): The camera instance used for capturing frames.
            t (Optional[threading.Thread]): The thread for camera operations.
        """
        self.camera: Camera = Camera()
        self.t: Optional[threading.Thread] = None

    @property
    def frame(self) -> any:  # Update with the actual type of 'frame'
        """
        Property to access the current frame.

        Returns:
            any: The current frame captured by the camera.
        """
        return self.camera.frame

    def start(self) -> None:
        """
        Start capturing frames from the camera.

        If the camera is already running, it won't start another thread.
        """
        if self.t is None or not self.t.is_alive():
            self.t = threading.Thread(target=self.camera.run)
            self.t.start()
        else:
            print("Camera is already running.")

    def stop(self) -> None:
        """
        Stop capturing frames from the camera.

        If the camera is running, this method stops the camera and waits for
        the camera thread to finish before returning.
        """
        if self.camera.running:
            self.camera.running = False
            if self.t and self.t.is_alive():
                self.t.join()
            print("Camera stopped.")
        else:
            print("Camera is not running.")


