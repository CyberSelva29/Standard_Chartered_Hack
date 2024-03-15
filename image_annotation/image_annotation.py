import matplotlib
from ultralytics import YOLO
import cv2
matplotlib.use('Agg')
import subprocess

def preprocess(input_path, output_path):
    try:
        img = cv2.imread(input_path)
        # Resize the image using interpolation for quality preservation
        resized_img = cv2.resize(img, (640, 640), interpolation=cv2.INTER_AREA)

        # Save the resized image in the specified format
        cv2.imwrite(output_path, resized_img)

        print(f"Image resized successfully and saved to: {output_path}")

    except (ValueError, IOError) as e:
        print(f"Error: {e}")



model_location = "trained_models/cheque_yolov8.pt"
image_loc = "other files/TrainSet/X/X_052.jpeg"

preprocess(image_loc, "fin.jpg")
# model = YOLO(model_location)
# print("model loaded")
# results = model.predict(source=image_loc, conf=0.5)
# print(results)
yolo_command = "yolo task=obb mode=predict model= trained_models/cheque_yolov8.pt conf=0.5 source = fin.jpg save_crop=True"
home_path = "D:\hackathon\standard chatered - cheque"

# Build the full command
full_command = f"cd {home_path} && {yolo_command}"

# Run YOLO command using subprocess
try:
    subprocess.run(full_command, shell=True, check=True)
    print("YOLO command executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing YOLO command: {e}")
