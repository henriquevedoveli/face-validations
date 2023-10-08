# FacialGuard: Real-time Facial Validation Toolkit

---

## Description
_**Face Validations**_ is a Python project that utilizes computer vision techniques to analyze webcam images, detect faces, and perform various validations based on facial features. It leverages OpenCV and MediaPipe frameworks for face detection and keypoint extraction. The project provides visual feedback by outlining the face in green or red bounding boxes based on whether it passes or fails validations.

## Directory Structure
```
FaceValidations/
    .gitignore
    .pre-commit-config.yaml
    Dockerfile
    requirements.txt
    run.sh
    Models/
        deploy.prototxt
        detector.tflite
        face_landmarker_v2_with_blendshapes.task
        res10_300x300_ssd_iter_140000_fp16.caffemodel
        resnet18_occlusion_v02.onnx
    src/
        Camera/
            Camera.py
            frameServer.py
        Config/
            config.py
        Detector/
            Detection.py
            Detector.py
        Renderer/
            Render.py
        Validations/
            Angle.py
            Blur.py
            Distance.py
            Liviness.py
            Occlusion.py
            utils.py
            ValidationTechnique.py
            Validation.py
        main.py
        run.py
```
- **.gitignore**: Specifies files and directories to be ignored by version control.
- **.pre-commit-config.yaml**: Configuration file for pre-commit hooks.
- **Dockerfile**: Docker configuration file to build the project environment.
- **requirements.txt**: A list of Python packages required for the project.
- **run.sh**: Bash script to run the Docker container with necessary configurations.
- **Models/**: Directory containing pretrained models and necessary files for validation techniques.
- **src/**: Directory containing the source code of the application.

---

## Validation Techniques

The Face Validations project employs various techniques to validate and analyze the detected faces. These techniques assess different aspects such as angles, blur, distance, liveliness, and occlusions to provide a comprehensive evaluation of the face in the webcam feed.

1. **Face Detection:**
   - Utilizes the trained model from MediaPipe for face detection, which provides bounding box coordinates and facial keypoints.
   - The detected face is outlined using a bounding box, which turns green if the face passes validations and red otherwise.

2. **Angle Validation:**
   - Determines if the face is within an acceptable angle by calculating yaw and roll angles.
   - Yaw angle is calculated based on the distances between facial keypoints and eye points, allowing assessment of left-right orientation.
   - Roll angle is determined using the distance along the x-axis between the top and bottom points of the face, helping identify tilting or rotation.

3. **Blur Validation:**
   - Evaluates image blur by calculating the Laplacian variance of the image.
   - Higher variance indicates a sharper image, while lower variance suggests blurriness.

4. **Distance Validation:**
   - Aims to estimate the distance of the face from the camera using facial keypoints.
   - Despite the limitation of estimated distances from facial keypoints, this validation attempts to gauge the proximity of the face.

5. **Liveliness Validation:**
   - Planned, but not yet implemented.
   - Aims to determine the liveliness of the detected face, potentially involving analysis of facial movements and expressions.

6. **Occlusion Validation:**
   - Utilizes a pre-trained ResNet-18 model to classify occlusions on the face.
   - The model has been trained to identify whether certain portions of the face are occluded, aiding in evaluating visibility and obstruction.

---

## Features
- Real-time face detection and validation using a webcam feed.
- Utilizes the MediaPipe library for accurate face detection and keypoint extraction.
- Performs validations such as angle checking, blur detection, and occlusion analysis.
- Provides visual feedback by outlining the detected face in green or red bounding boxes.
- Dockerized environment for easy setup and execution.

---

## Instructions for Use:
1. Clone the repository and navigate to the project directory.
2. Build the Docker image using the provided Dockerfile:
```docker build -t face_validations .```
3. Run the Docker container, passing the image name and any necessary environment settings:
```bash run.sh face_validations```
This script (run.sh) simplifies the container execution process.

**Note**: Before running the project, ensure that Docker is installed on your system and you have granted necessary permissions for webcam access. Additionally, you might need to adjust environment settings or install required dependencies within the Docker container to ensure proper functionality.
