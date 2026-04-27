from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Vehicle classes (COCO dataset)
vehicle_classes = [2, 3, 5, 7]  # car, bike, bus, truck

# Load your videos
videos = ["video1.mp4", "video2.mp4"]  # low + high congestion

for video_path in videos:
    cap = cv2.VideoCapture(video_path)

    print(f"\nProcessing: {video_path}")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w, _ = frame.shape

        # Focus only on bottom half (important for accuracy)
        roi = frame[int(h/2):h, 0:w]

        # Run YOLO on ROI
        results = model(roi)

        vehicle_count = 0

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                if cls in vehicle_classes:
                    vehicle_count += 1

        #  Congestion Logic
        if vehicle_count < 5:
            level = "LOW"
            color = (0, 255, 0)
        elif vehicle_count < 15:
            level = "MEDIUM"
            color = (0, 255, 255)
        else:
            level = "HIGH"
            color = (0, 0, 255)

        # Draw ROI box
        cv2.rectangle(frame, (0, int(h/2)), (w, h), (255, 0, 0), 2)

        # Display vehicle count
        cv2.putText(frame, f"Vehicles: {vehicle_count}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Display congestion level
        cv2.putText(frame, f"Traffic: {level}", (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

        # Draw detection boxes on ROI
        annotated_roi = results[0].plot()

        # Replace ROI back into frame
        frame[int(h/2):h, 0:w] = annotated_roi

        # Show output
        cv2.imshow(f"Traffic Detection - {video_path}", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

cv2.destroyAllWindows()