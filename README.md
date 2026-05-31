# Purplle Store Intelligence System

## Overview

This project is an AI-powered Store Intelligence System developed for the Purplle Tech Challenge 2026.

The system processes CCTV footage, detects visitors using YOLOv8, tracks them using ByteTrack, generates visitor events, exposes analytics APIs through FastAPI, and visualizes insights using a Streamlit dashboard.

---

## Features

* Person Detection using YOLOv8
* Multi-object Tracking using ByteTrack
* Visitor Event Generation
* FastAPI REST APIs
* Store Metrics API
* Funnel Analytics API
* Heatmap API
* Anomaly Detection API
* Streamlit Dashboard
* Swagger API Documentation

---

## Architecture

CCTV Video → YOLOv8 → ByteTrack → Event Generation → FastAPI → Dashboard

---

## API Endpoints

### Health

GET /health

### Metrics

GET /stores/{store_id}/metrics

### Funnel

GET /stores/{store_id}/funnel

### Heatmap

GET /stores/{store_id}/heatmap

### Anomalies

GET /stores/{store_id}/anomalies

---

## Dashboard

The dashboard displays:

* Unique Visitors
* Total Events
* Entry Events
* Event Distribution
* Recent Events
* Store Summary

---

## Technologies Used

* Python
* YOLOv8
* ByteTrack
* OpenCV
* FastAPI
* Streamlit
* Pandas

---

## Results

* Unique Visitors Detected: 24
* Events Generated: 24
* APIs Functional
* Dashboard Operational

---

## Future Improvements

* Zone Analytics
* Shelf Engagement Tracking
* Queue Detection
* Conversion Funnel Analysis
* Real-time Kafka Streaming
* Multi-camera Correlation
