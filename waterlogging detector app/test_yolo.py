from ultralytics import YOLO
import cv2
import os

model = YOLO(r"C:\Users\SARTHAK\OneDrive\Documents\SELF PROJECTS\yolo\best.pt")

folder = r"C:\Users\SARTHAK\OneDrive\Documents\SELF PROJECTS\yolo\testing images"

for image_name in os.listdir(folder):

    image_path = os.path.join(folder, image_name)

    # prediction
    results = model.predict(
        source=image_path,
        save=False
    )

    # get detected image
    annotated = results[0].plot()

    cv2.imshow("YOLO Detection - Press Q for next", annotated)

    print("Showing:", image_name)
    print("Press 'q' to go to next image")

    while True:
        key = cv2.waitKey(1)

        if key == ord('q'):
            break

cv2.destroyAllWindows()

print("Done")