from Validations.Angle import ValidateAngle
from Validations.Blur import ValidateBlur
from Validations.Distance import ValidateDistance
from Validations.Liviness import ValidateLiviness
from Validations.Occlusion import ValidateOcclusion

class Validations:
    def __init__(self) -> None:
        self.angle_validator = ValidateAngle()
        self.blur_validator = ValidateBlur()
        self.distance_validator = ValidateDistance()
        self.liveness_validator = ValidateLiviness()
        self.occlusion_validator = ValidateOcclusion()