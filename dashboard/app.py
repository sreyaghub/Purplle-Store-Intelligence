import streamlit as st
import pandas as pd
import json

st.set_page_config(
    page_title="Purplle Store Intelligence",
    page_icon="🛍️",
    layout="wide"
)

# Load Events
events = []

try:
    with open("events.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            events.append(json.loads(line))

    df = pd.DataFrame(events)

except Exception:
    df = pd.DataFrame()

# Title
st.title("🛍️ Purplle Store Intelligence Dashboard")

st.markdown("---")

# Metrics
col1, col2, col3 = st.columns(3)

if not df.empty:

    unique_visitors = df["visitor_id"].nunique()

    total_events = len(df)

    entry_count = len(
        df[df["event_type"] == "ENTRY"]
    )

else:

    unique_visitors = 0
    total_events = 0
    entry_count = 0

col1.metric(
    "👥 Unique Visitors",
    unique_visitors
)

col2.metric(
    "📊 Total Events",
    total_events
)

col3.metric(
    "🚪 Entry Events",
    entry_count
)

st.markdown("---")

# Event Distribution
st.subheader("📈 Event Distribution")

if not df.empty:

    event_counts = (
        df["event_type"]
        .value_counts()
    )

    st.bar_chart(event_counts)

else:
    st.warning("No events found.")

st.markdown("---")

# Recent Events
st.subheader("📋 Recent Events")

if not df.empty:

    st.dataframe(
        df.tail(20),
        use_container_width=True
    )

else:
    st.warning("events.jsonl is empty")

st.markdown("---")

# Store Summary
st.subheader("🏪 Store Summary")

if not df.empty:

    st.json(
        {
            "Store ID": "STORE_001",
            "Unique Visitors": unique_visitors,
            "Total Events": total_events,
            "Entry Count": entry_count
        }
    )