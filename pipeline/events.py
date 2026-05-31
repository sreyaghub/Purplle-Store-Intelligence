import cv2
import json
import uuid
from datetime import datetime, UTC

from ultralytics import YOLO
import supervision as sv

# Load YOLO model
model = YOLO("yolov8n.pt")

# Tracker
tracker = sv.ByteTrack()

# Video Path
video_path = r"C:\Users\hp\Downloads\CCTV Footage-20260529T160731Z-3-00144614ea\CCTV Footage\CAM 1.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

# Event File
event_file = open("events.jsonl", "w", encoding="utf-8")

seen_visitors = set()
frame_number = 0

print("Processing Video...")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1

    # Skip some frames for speed
    if frame_number % 5 != 0:
        continue

    # YOLO Detection
    results = model(
        frame,
        classes=[0],  # Person class only
        verbose=False
    )[0]

    detections = sv.Detections.from_ultralytics(results)

    if len(detections) == 0:
        continue

    # Tracking
    detections = tracker.update_with_detections(detections)

    print(
        f"Frame {frame_number} | "
        f"People: {len(detections)}"
    )

    # Generate Events
    if detections.tracker_id is not None:

        for tracker_id in detections.tracker_id:

            if tracker_id is None:
                continue

            visitor_id = f"VIS_{tracker_id}"

            if visitor_id not in seen_visitors:

                seen_visitors.add(visitor_id)

                event = {
                    "event_id": str(uuid.uuid4()),
                    "store_id": "STORE_001",
                    "camera_id": "CAM_1",
                    "visitor_id": visitor_id,
                    "event_type": "ENTRY",
                    "timestamp": datetime.now(UTC).isoformat(),
                    "zone_id": None,
                    "dwell_ms": 0,
                    "is_staff": False,
                    "confidence": 0.90,
                    "metadata": {
                        "frame_number": frame_number
                    }
                }

                event_file.write(
                    json.dumps(event) + "\n"
                )

                print(
                    f"ENTRY EVENT -> {visitor_id}"
                )

event_file.close()

cap.release()

print("\n" + "=" * 50)
print("Processing Completed")
print(
    f"Unique Visitors: "
    f"{len(seen_visitors)}"
)
print(
    "Events saved to events.jsonl"
)
print("=" * 50)