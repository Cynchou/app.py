import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# --- Page Configuration ---
st.set_page_config(page_title="Immersive Event Report", layout="wide")

# --- Custom CSS Styles ---
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; font-weight: bold; color: #1a1a1a; text-align: center;}
    .sub-header {font-size: 1.2rem; color: #666; text-align: center; margin-bottom: 2rem;}
    .metric-card {background-color: #f8f9fa; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #C5A065;}
    .quote-box {background-color: #fff; padding: 1.5rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); font-style: italic;}
</style>
""", unsafe_allow_html=True)

# --- 1. Top Section: The Hook ---
st.markdown('<div class="main-header">LVMH Brand Immersive Experience Report</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">From Sensory Touch to Brand Identity | July 2026</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.info("💡 **Key Insight:** Visitors are no longer just 'watchers', but 'co-creators' of the brand story. **NPS: 78**")

st.divider()

# --- 2. Middle Section: The Journey ---
st.header("Immersive Journey Highlights")

# Mock Data
journey_stages = ["Sensory Awakening", "Deep Interaction", "Emotional Resonance"]
avg_stay = [8, 15, 12]
satisfaction = [4.5, 4.9, 4.8]

# Create Plotly Chart
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Bar(
    x=journey_stages,
    y=avg_stay,
    name="Avg Stay (min)",
    marker_color="# 1a1a1a",
    opacity=0.8
), secondary_y=False)

fig.add_trace(go.Scatter(
    x=journey_stages,
    y=satisfaction,
    name="Satisfaction Score",
    marker_color="# C5A065",
    line=dict(width=4),
    mode="lines+markers"
), secondary_y=True)

fig.update_layout(
    title_text="Visitor Engagement & Satisfaction Across Journey Nodes",
    xaxis_title="Journey Stages",
    yaxis_title="Average Stay (Minutes)",
    yaxis2_title="Satisfaction Score (out of 5)",
    height=400,
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# --- 3. Bottom Section: The Impact ---
st.header("Impact & Voices")
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("📈 Business Impact")
c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label="Leads Generated", value="120+", delta="+15%")
with c2:
    st.metric(label="Social Mentions", value="300+", delta="+200%")
with c3:
    st.metric(label="Conversion Lift", value="15%", delta="+5%")
with col_right:
    st.markdown("💬 Visitor Voices")
st.markdown("""
<div class="quote-box">
"I finally understood why it's worth the price. It's about respect."<br>
<small>- Ms. Li, First-time Visitor</small>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="quote-box" style="margin-top: 10px;">
"The VR part was shocking. I couldn't help but share it."<br>
<small>- Mr. Zhang, KOL</small>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="quote-box" style="margin-top: 10px;">
"The VR part was shocking. I couldn't help but share it."<br>
<small>- Mr. Zhang, KOL</small>
</div>
""", unsafe_allow_html=True)
