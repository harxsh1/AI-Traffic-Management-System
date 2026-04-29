import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def count_vehicles(video_path):
    cap = cv2.VideoCapture(video_path)
    vehicle_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]

                if label in ["car", "truck", "bus", "motorbike"]:
                    vehicle_count += 1

        break  # only one frame for simplicity

    cap.release()
    return vehicle_count


def get_lane_counts():
    lane1 = count_vehicles("video1.mp4")
    lane2 = count_vehicles("video2.mp4")

    return [lane1, lane2]