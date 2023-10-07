from src.Validations.ValidationTechnique import ValidationTechnique
import cv2


class ValidateOcclusion(ValidationTechnique):
    def validate(self, face):
        try:
            face=cv2.resize(face, (250,250))
            input = cv2.dnn.blobFromImage(face, 1/255, (224, 224), swapRB=True, crop=False)
            self.occlusion_model.setInput(input) 

            out = self.occlusion_model.forward()
            
            out = out[0][0]

            return out < self.occlusion_thresh
        
        except Exception as e:
            print(str(e))
