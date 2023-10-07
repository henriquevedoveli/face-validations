from Validations.ValidationTechnique import ValidationTechnique
from Validations.utils import calculate_distance, calculate_x_distance

class ValidateAngle(ValidationTechnique):    
    def validate(self, keypoints):
        if keypoints is not None:
            yawl_left, yawl_right = self.calculate_yawl(keypoints)
            roll = self.calculate_roll(keypoints)

            return all([yawl_left > self.left_yawl_thresh, yawl_right > self.right_yawl_thresh, roll<self.roll_thresh])
        return False
    
    def calculate_yawl(self, keypoints):
        """Calculate the distance between the leftist point of the face with the lefistis point of the eye. 
        Calculate the distante between the rightist point of the face with the rightist point of the eye. 
        """
        if keypoints is not None:
            first_left = keypoints[0]['left']
            second_left = keypoints[1]['left']

            first_right = keypoints[0]['right']
            second_right = keypoints[2]['right']

            distance_left = calculate_distance(first_left, second_left)
            distance_right = calculate_distance(first_right, second_right)
            return distance_left, distance_right
        
    def calculate_roll(self, keypoints):
        if keypoints is not None:
            return calculate_x_distance(keypoints[0]['top'], keypoints[0]['bottom'])
