import yaml

import os

print(os.path.abspath('.'))

with open('Config/config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

app_name = config['app_name']
version = config['version']
author = config['author']

min_dist = config['Distance']['Min']
max_dist = config['Distance']['Max']

left_yawl_max = config['Angle']['LeftYawlMax']
right_yawl_max = config['Angle']['RightYawlMax']
roll_max = config['Angle']['RollMax']

facial_expression = config['FacialExpression']

occlusion_thresh = config['Occlusion']['Threshold']

occlusion_model = config['Occlusion']["ModelPath"]

blur_thresh = config['Blur']['Threshold']

liviness_thresh = config['Liviness']['Threshold']

camera_idx = config['Camera']['CameraIdx']



