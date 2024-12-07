import cv2 as cv
import numpy as np
import time
import threading

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

# Set preferable backend and target for CPU
model.setPreferableBackend(cv.dnn.DNN_BACKEND_DEFAULT)
model.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

# Global variables
frame = None  # Current frame
output_frame = None  # Frame with detections
lock = threading.Lock()
stop_thread = False  # Thread stop signal


def object_detection_thread():
    """
    Perform object detection every 2nd frame to reduce processing load.
    """
    global frame, output_frame, stop_thread

    frame_counter = 0
    while not stop_thread:
        with lock:
            if frame is None:
                continue
            input_frame = frame.copy()

        frame_counter += 1
        if frame_counter % 3 != 0:  # Skip every 2nd frame
            continue

        # Resize and preprocess the frame for the model
        input_frame = cv.resize(input_frame, (200, 200))  # Resize to 200x200
        blob = cv.dnn.blobFromImage(input_frame, size=(200, 200), swapRB=True)
        model.setInput(blob)

        # Perform object detection
        detections = model.forward()

        # Process detections
        with lock:
            output_frame = frame.copy()  # Use cropped frame for drawing
            for detection in detections[0, 0, :, :]:
                confidence = detection[2]
                if confidence > 0.4:  # Confidence threshold
                    class_id = int(detection[1])
                    class_name = class_names[class_id - 1]
                    color = COLORS[class_id % len(COLORS)]

                    # Get bounding box coordinates
                    box_x = int(detection[3] * output_frame.shape[1])
                    box_y = int(detection[4] * output_frame.shape[0])
                    box_width = int(detection[5] * output_frame.shape[1])
                    box_height = int(detection[6] * output_frame.shape[0])

                    # Draw the bounding box and label
                    cv.rectangle(output_frame, (box_x, box_y), (box_width, box_height), color, thickness=2)
                    cv.putText(output_frame, f"{class_name}: {confidence:.2f}", (box_x, box_y - 10),
                               cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


def main():
    global frame, output_frame, stop_thread

    # Open the camera
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    # Set video resolution to 320x240
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

    # Start the object detection thread
    detection_thread = threading.Thread(target=object_detection_thread)
    detection_thread.start()

    try:
        while True:
            # Read a new frame
            ret, current_frame = cap.read()
            if not ret:
                print("Failed to capture frame. Exiting...")
                break

            # Flip the frame 180 degrees
            current_frame = cv.flip(current_frame, -1)

            # Crop the upper half of the frame
            h, w, _ = current_frame.shape
            crop_start = h // 2  # Crop from the middle
            crop_end = h  # Keep the lower half
            current_frame = current_frame[crop_start:crop_end, :]  # Crop the bottom half

            # Update the global frame variable
            with lock:
                frame = current_frame.copy()

            # Display the frame with detections if available
            with lock:
                display_frame = output_frame if output_frame is not None else current_frame
                cv.imshow('Real-Time Object Detection', display_frame)

            # Break the loop on 'q' key press
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        stop_thread = True
        detection_thread.join()
        cap.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    main()
