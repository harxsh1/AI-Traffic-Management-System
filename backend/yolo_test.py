from ultralytics import YOLO
import cv2

# Loading YOLOv8 model for object detection
model = YOLO("yolov8n.pt")

# Starting webcam for real-time detection
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # If frame is not captured, break the loop
    if not ret:
        break

    # Running YOLO detection on current frame
    results = model(frame)

    # Drawing bounding boxes on detected objects
    annotated_frame = results[0].plot()

    # Displaying output window
    cv2.imshow("YOLO Detection", annotated_frame)

    # Press 'q' to exit the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releasing camera and closing all windows
cap.release()
cv2.destroyAllWindows()