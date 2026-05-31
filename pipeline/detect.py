from ultralytics import YOLO
import supervision as sv
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# ByteTrack Tracker
tracker = sv.ByteTrack()

# Video path
video_path = r"C:\Users\hp\Downloads\CCTV Footage-20260529T160731Z-3-00144614ea\CCTV Footage\CAM 1.mp4"

cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # YOLO detection
    results = model(frame, classes=[0], verbose=False)[0]

    detections = sv.Detections.from_ultralytics(results)

    # Tracking
    detections = tracker.update_with_detections(detections)

    visitor_count = len(detections)

    # Draw tracked people
    for tracker_id, box in zip(
        detections.tracker_id,
        detections.xyxy
    ):
        x1, y1, x2, y2 = map(int, box)

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"ID {tracker_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f"Tracked Visitors: {visitor_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        3
    )

    cv2.imshow("Purplle Visitor Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()