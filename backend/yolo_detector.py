from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

vehicle_classes = [2, 3, 5, 7]  # car, bike, bus, truck

def count_vehicles(video_path):
    cap = cv2.VideoCapture(video_path)

    ret, frame = cap.read()
    if not ret:
        return 0

    results = model(frame)

    count = 0
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if cls in vehicle_classes:
                count += 1

    cap.release()
    return count


def get_lane_counts():
    lane1 = count_vehicles("video1.mp4")
    lane2 = count_vehicles("video2.mp4")

    return [lane1, lane2]