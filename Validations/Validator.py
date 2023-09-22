import Validations

class Validator:
    #TODO ver se é possivel imprlementar a validacao de distancia
    #TODO implementar a validacao de liviness
    def __init__(self) -> None:
        self.validations = Validations.Validations()

    def validate_face(self, frame, face, keypoints):
        if not self.validations.blur_validator.validate(frame):
            return False, "BLUR"

        if not self.validations.angle_validator.validate(keypoints):
            return False, 'ANGLE'
        
        # if not self.validations.occlusion_validator.validate(face=face):
        #     return False, "OCCLUSION"
        
        return True, 'OK'
        
