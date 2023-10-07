from .Angle import ValidateAngle
from .Blur import ValidateBlur
from .Distance import ValidateDistance
from .Liviness import ValidateLiviness
from .Occlusion import ValidateOcclusion

class Validations:
    def __init__(self) -> None:
        self.angle_validator = ValidateAngle()
        self.blur_validator = ValidateBlur()
        self.distance_validator = ValidateDistance()
        self.liveness_validator = ValidateLiviness()
        self.occlusion_validator = ValidateOcclusion()