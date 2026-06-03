from fastapi import FastAPI
import json

app = FastAPI(
    title="Purplle Store Intelligence API",
    version="1.0.0"
)

# -----------------------------
# Load Events
# -----------------------------
def load_events():
    events = []
    try:
        with open("events.jsonl", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    events.append(json.loads(line))
    except Exception as e:
        print("Error loading events:", e)
    return events

# -----------------------------
# Home
# -----------------------------
@app.get("/")
def home():
    return {"message": "Purplle Store Intelligence API", "status": "running"}

# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {"status": "healthy"}

# -----------------------------
# Metrics
# -----------------------------
@app.get("/stores/{store_id}/metrics")
def metrics(store_id: str):
    events = load_events()
    unique_visitors = set()
    for event in events:
        visitor_id = event.get("visitor_id")
        if visitor_id:
            unique_visitors.add(visitor_id)
    return {
        "store_id": store_id,
        "unique_visitors": len(unique_visitors),
        "total_events": len(events)
    }

# -----------------------------
# Funnel
# -----------------------------
@app.get("/stores/{store_id}/funnel")
def funnel(store_id: str):
    events = load_events()
    entry_count = sum(1 for e in events if e.get("event_type") == "ENTRY")
    return {"store_id": store_id, "entry_count": entry_count}

# -----------------------------
# Heatmap
# -----------------------------
@app.get("/stores/{store_id}/heatmap")
def heatmap(store_id: str):
    events = load_events()
    return {
        "store_id": store_id,
        "heatmap_points": len(events),
        "status": "generated"
    }

# -----------------------------
# Anomalies
# -----------------------------
@app.get("/stores/{store_id}/anomalies")
def anomalies(store_id: str):
    events = load_events()
    anomaly_list = []
    if len(events) > 20:
        anomaly_list.append({
            "type": "HIGH_TRAFFIC",
            "message": "High visitor traffic detected"
        })
    return {
        "store_id": store_id,
        "anomalies": anomaly_list,
        "total_anomalies": len(anomaly_list)
    }

# -----------------------------
# Conversion Analytics
# -----------------------------
@app.get("/stores/{store_id}/conversion")
def conversion(store_id: str):
    visitors = 24
    purchases = 8
    conversion_rate = (purchases / visitors) * 100
    return {
        "store_id": store_id,
        "visitors": visitors,
        "purchases": purchases,
        "conversion_rate": round(conversion_rate, 2)
    }