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

# Demo POS Analytics
orders = 8
revenue = 12500
conversion_rate = round(
    (orders / max(unique_visitors, 1)) * 100,
    2
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "👥 Visitors",
    unique_visitors
)

col2.metric(
    "📊 Events",
    total_events
)

col3.metric(
    "🚪 Entries",
    entry_count
)

col4.metric(
    "🛒 Conversion",
    f"{conversion_rate}%"
)

st.markdown("---")

sales1, sales2 = st.columns(2)

sales1.metric(
    "💰 Revenue",
    f"₹{revenue:,}"
)

sales2.metric(
    "🧾 Orders",
    orders
)

st.markdown("---")

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

st.subheader("📋 Recent Events")

if not df.empty:

    st.dataframe(
        df.tail(20),
        use_container_width=True
    )

else:
    st.warning("No events available.")

st.markdown("---")

st.subheader("🏪 Store Summary")

st.json(
    {
        "Store ID": "STORE_001",
        "Unique Visitors": unique_visitors,
        "Orders": orders,
        "Revenue": revenue,
        "Conversion Rate": f"{conversion_rate}%"
    }
)