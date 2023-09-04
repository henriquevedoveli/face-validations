import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def calculate_x_distance(point1, point2):
    x1, _ = point1
    x2, _ = point2
    distance = abs(x2 - x1)
    return distance