# FacialGuard: Real-time Facial Validation Toolkit

## I tried to run this project in a web page using streamlit, but it was not possible to run the code on the web due to lack of processing capacity

```
.
├── app.py
├── Camera
│   ├── Camera.py
│   └── frameServer.py
├── Config
│   ├── config.py
│   └── config.yaml
├── Detector
│   ├── Detection.py
│   └── Detector.py
├── main.py
├── Models
│   ├── deploy.prototxt
│   ├── detector.tflite
│   ├── face_landmarker_v2_with_blendshapes.task
│   ├── res10_300x300_ssd_iter_140000_fp16.caffemodel
│   └── resnet18_occlusion_v02.onnx
├── README.md
├── Renderer
│   └── Render.py
├── run.py
└── Validations
    ├── Angle.py
    ├── Blur.py
    ├── Distance.py
    ├── __init__.py
    ├── Liviness.py
    ├── Occlusion.py
    ├── utils.py
    ├── ValidationTechnique.py
    └── Validator.py
```