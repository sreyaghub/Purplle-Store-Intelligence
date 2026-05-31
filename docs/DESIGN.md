# System Design

## High Level Architecture

1. CCTV footage is ingested from store cameras.
2. YOLOv8 detects customers in each frame.
3. ByteTrack assigns unique tracking IDs.
4. Tracking IDs are converted into visitor events.
5. Events are stored in JSONL format.
6. FastAPI exposes analytics APIs.
7. Streamlit dashboard visualizes metrics.

## Processing Pipeline

Video Input
↓
YOLOv8 Detection
↓
ByteTrack Tracking
↓
Visitor Event Generation
↓
events.jsonl
↓
FastAPI
↓
Dashboard

## Components

### Detection Layer

YOLOv8 is used for person detection.

### Tracking Layer

ByteTrack maintains persistent visitor identities.

### Event Layer

ENTRY events are generated whenever a new visitor appears.

### Analytics Layer

Metrics, Funnel, Heatmap and Anomaly APIs are exposed through FastAPI.

### Visualization Layer

Streamlit dashboard displays store intelligence metrics.
