import streamlit as st
import joblib
import pandas as pd
import numpy as np
import time
from sklearn.preprocessing import LabelEncoder, StandardScaler # இதைப் புதிதாகச் சேர்த்துள்ளேன்

# Page Config
st.set_page_config(page_title="Smart Shield AI", layout="wide", page_icon="🛡️")

# Load Brain
try:
    model = joblib.load('smart_shield_model.pkl')
    scaler = joblib.load('scaler.pkl')
    le = joblib.load('label_encoder.pkl')
except:
    st.error("❌ Model files not found! Please run the training notebook first.")

st.title("🛡️ SMART SHIELD: AI-Powered Real-Time Threat Intelligence")
st.markdown("---")
st.sidebar.header("System Controls")

if st.sidebar.button("🚀 Start Live Monitoring"):
    st.subheader("Live Network Traffic Analysis")
    
    # Placeholders for dynamic UI
    status_indicator = st.empty()
    col1, col2 = st.columns([2, 1]) # Column விகிதத்தை மாற்றியுள்ளேன்
    
    with col1:
        st.write("📈 Traffic Volume")
        chart_placeholder = st.empty()
    with col2:
        st.write("📑 System Logs")
        logs_placeholder = st.empty()

    traffic_data = []
    log_messages = [] # பல லாக்சைச் சேமிக்க

    # Simulation Loop
    for i in range(50):
        # 1. Simulate "Incoming Packet" data (8 features)
        new_packet = np.random.rand(1, 8) 
        
        # Scaling
        scaled_packet = scaler.transform(new_packet)
        
        # 2. AI Prediction
        prediction = model.predict(scaled_packet)
        prob = model.predict_proba(scaled_packet).max()
        
        # Get Label
        result_label = le.inverse_transform(prediction)[0]

        # 3. UI Logic
        traffic_data.append(np.random.normal(10, 2)) 
        chart_placeholder.line_chart(traffic_data)

        # Log Message Formatting
        current_log = f"Packet {i}: Type: **{result_label}** | Confidence: {prob*100:.2f}%"
        log_messages.insert(0, current_log) # புதிய லாக் முதலில் வர
        logs_placeholder.write("\n".join(log_messages[:10])) # கடைசி 10 லாக்ஸ் மட்டும் காட்டும்

        if result_label == "Benign" or result_label == "Normal":
            status_indicator.success(f"🟢 System Secure: Monitoring Traffic...")
        else:
            # RED ALERT TRIGGER
            status_indicator.error(f"🚨 CRITICAL THREAT: {result_label} Detected!")
            st.toast(f"Blocking Threat: {result_label}", icon="🛡️")
            st.metric(label="Threat Severity", value="High", delta="Immediate Action Taken")
            st.warning(f"⚠️ Security Breach Attempted! IP Address has been blacklisted.")
            break 
            
        time.sleep(0.4)

st.sidebar.markdown("---")
st.sidebar.info("Designed for National Level Symposium - SKP Engineering College")
st.sidebar.caption("Developer: Aratika | CSE Dept")