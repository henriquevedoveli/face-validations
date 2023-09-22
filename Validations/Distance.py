from Validations.ValidationTechnique import ValidationTechnique

class ValidateDistance(ValidationTechnique):
    
    def validate(self, image):
        return self.distance_min <= self.calculate_distance() <= self.distance_max

    def calculate_distance(self):
        dist = 50
        return dist 
