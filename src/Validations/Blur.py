from src.Validations.ValidationTechnique import ValidationTechnique
import cv2
import traceback
from typing import Union

class ValidateBlur(ValidationTechnique):
    """
    A validation technique to check for image blurriness.

    This class extends ValidationTechnique and implements the
    validate method to determine whether an image is blurry
    based on its Laplacian variance.

    Attributes:
        blur_thresh (float): The threshold value for blurriness.

    Methods:
        validate(image: Union[None, int]) -> bool:
        Validates the input image for blurriness.

    """

    def validate(self, image: Union[None, int]) -> bool:
        """
        Validate an image for blurriness.

        Args:
            image (Union[None, int]): The input image to be validated.

        Returns:
            bool: True if the image is not blurry, False otherwise.

        """
        gray: cv2.ndarray 
        variance: float
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            variance  = cv2.Laplacian(gray, cv2.CV_64F).var()
        except Exception as error:
            print("[CRITICAL] could not check blur on image ", str(error), " ", traceback.print_exc())
            return

        if variance < self.blur_thresh:
            return False
        else:
            return True
