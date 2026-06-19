# Water Logging Detection & UAV Vision Dataset Development

## Overview

This project focuses on developing a UAV-based computer vision pipeline for **water logging detection and land cover analysis** using deep learning models.

The project includes custom dataset creation, annotation, preprocessing, YOLO model training, and deployment of an inference pipeline using **FastAPI**. The system demonstrates an end-to-end workflow starting from UAV/image dataset preparation to real-time object detection and visualization.

The objective of this project was to explore the application of **AI-based vision systems for smart city monitoring, environmental analysis, and UAV-assisted inspection**.

---

# Features

* Custom-trained YOLOv8 model for water logging detection
* UAV vision dataset development and annotation
* Land cover classification dataset preparation using YOLO format
* Image preprocessing and dataset validation
* Model training using Google Colab GPU environment
* FastAPI backend for AI inference
* Image upload and real-time prediction pipeline
* Bounding box detection with confidence scores
* Testing on custom images and video frames

---

# Dataset Development

## YOLOv8 Dataset — Water Logging Detection

A custom dataset was prepared for detecting water logging regions.

Workflow:

* Image collection
* Data cleaning and preprocessing
* Annotation using Roboflow
* Dataset version management
* YOLOv8 format export
* Model training and evaluation

---

## YOLOv12 Dataset — UAV Land Cover Detection

A custom UAV vision dataset was prepared and annotated for environmental scene understanding.

Classes included:

* Vegetation
* Water Body
* Dry Area
* Footpath

The dataset was developed for UAV-based land monitoring and future computer vision model development.

---

# Project Workflow

```
Image Collection
        │
        ▼
Dataset Annotation (Roboflow)
        │
        ▼
Data Preprocessing & Validation
        │
        ▼
YOLO Model Training (Google Colab)
        │
        ▼
best.pt Model Generation
        │
        ▼
FastAPI Deployment
        │
        ▼
Image Upload
        │
        ▼
Object Detection & Visualization
```

---

# Tech Stack

### Programming & AI

* Python
* YOLOv8
* YOLOv12
* OpenCV

### Dataset Tools

* Roboflow
* Custom UAV Image Dataset

### Deployment

* FastAPI
* Uvicorn

### Training Environment

* Google Colab

---

# Project Structure

```
project/

│
├── backend/
│   └── FastAPI inference server
│
├── frontend/
│
├── model/
│   └── best.pt
│
├── datasets/
│
├── frame_generation/
│
├── images/
│
├── videos/
│
├── test_yolo.py
│
└── README.md
```

---

# Model Training

Training pipeline:

* Custom dataset prepared using Roboflow
* Images annotated in YOLO format
* Dataset trained using YOLOv8
* Training performed on Google Colab
* Best performing weights saved as:

```
best.pt
```

The trained model was tested on multiple custom images and UAV-based visual data.

---

# Inference Pipeline

1. Start FastAPI backend server using Uvicorn

2. Load trained YOLO model:

```
best.pt
```

3. Upload input image

4. Perform object detection

5. Generate predictions:

* Detected objects
* Bounding boxes
* Confidence scores

6. Display detection results

---

# Applications

* Smart City Monitoring
* Flood and Water Logging Detection
* UAV Environmental Analysis
* Land Cover Monitoring
* Infrastructure Inspection
* AI-based Remote Sensing Applications

---

# Learning Outcomes

This project provided practical experience in:

* Computer Vision Development
* Object Detection using YOLO
* UAV Image Dataset Creation
* Image Annotation and Dataset Management
* Roboflow Workflow
* OpenCV Image Processing
* Deep Learning Model Training
* FastAPI Deployment
* AI Application Integration

---

# Future Improvements

* Live UAV camera inference
* Real-time video stream detection
* Edge deployment on embedded devices
* Cloud-based AI inference
* GIS-based visualization
* Automated UAV monitoring system

---

# Project Status

Completed ✔️

This project demonstrates a complete AI computer vision workflow, covering:

**Dataset Development → Model Training → Backend Deployment → Real-Time Detection**

for UAV-based water logging detection and environmental monitoring applications.
