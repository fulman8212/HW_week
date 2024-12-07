import cv2 as cv
import numpy as np
import time

# Load class names
class_names = []
with open('/home/pavlov/Project/python/week13/object_detection_classes_coco.txt', 'r') as f:
    class_names = f.read().strip().split('\n')

# Generate random colors for each class
COLORS = np.random.uniform(0, 255, size=(len(class_names), 3))

# Load the pre-trained model
model = cv.dnn.readNetFromTensorflow(
    model='/home/pavlov/Project/python/week13/frozen_inference_graph.pb',
    config='/home/pavlov/Project/python/week13/ssd_mobilenet_v2_coco_2018_03_29.pbtxt'
)

# Open the camera
cap = cv.VideoCapture(0)

# Set desired FPS
desired_fps = 10  # Adjust this value to your needs
cap.set(cv.CAP_PROP_FPS, desired_fps)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

print("Starting real-time object detection...")

# Skip frame counter for sampling
frame_skip = 2  # Process every 2nd frame
frame_counter = 0

while True:
    start_time = time.time()  # Start time for frame processing

    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Skip frames for efficiency
    frame_counter += 1
    if frame_counter % frame_skip != 0:
        continue

    # Flip the frame 180 degrees
    frame = cv.flip(frame, -1)

    frame_height, frame_width, _ = frame.shape

    # Create a blob from the frame
    blob = cv.dnn.blobFromImage(frame, size=(300, 300), swapRB=True)

    # Set the blob as input to the model
    model.setInput(blob)

    # Perform forward pass to get detections
    detections = model.forward()

    # Process detections
    for detection in detections[0, 0, :, :]:
        confidence = detection[2]
        if confidence > 0.4:  # Confidence threshold
            class_id = int(detection[1])
            class_name = class_names[class_id - 1]
            color = COLORS[class_id % len(COLORS)]

            # Bounding box coordinates
            box_x = int(detection[3] * frame_width)
            box_y = int(detection[4] * frame_height)
            box_width = int(detection[5] * frame_width)
            box_height = int(detection[6] * frame_height)

            # Draw bounding box and label
            cv.rectangle(frame, (box_x, box_y), (box_width, box_height), color, thickness=2)
            cv.putText(frame, f"{class_name}: {confidence:.2f}", (box_x, box_y - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Calculate and display FPS
    end_time = time.time()
    fps = 1 / (end_time - start_time)
    cv.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the resulting frame
    cv.imshow('Real-Time Object Detection', frame)

    # Break the loop on 'q' key press
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all OpenCV windows
cap.release()
cv.destroyAllWindows()
