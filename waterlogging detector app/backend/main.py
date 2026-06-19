from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from ultralytics import YOLO
import shutil
import os
import cv2

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained YOLO model
model = YOLO("../best.pt")


@app.get("/")
def home():
    return {
        "message": "YOLO Backend Running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Save uploaded image
    image_path = "temp.jpg"

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run YOLO prediction
    results = model(image_path)

    detections = []

    for result in results:
        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            detections.append(
                {
                    "class": model.names[class_id],
                    "confidence": round(confidence, 2),
                }
            )

    # Create image with bounding boxes
    annotated_image = results[0].plot()

    # Save annotated image
    cv2.imwrite("prediction.jpg", annotated_image)

    # Delete uploaded temporary image
    if os.path.exists(image_path):
        os.remove(image_path)

    return {
        "detections": detections,
        "annotated_image": "http://127.0.0.1:8000/prediction"
    }


@app.get("/prediction")
def get_prediction_image():

    return FileResponse(
        "prediction.jpg",
        media_type="image/jpeg",
        filename="prediction.jpg"
    )