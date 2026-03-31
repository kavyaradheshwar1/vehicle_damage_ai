import streamlit as st
from PIL import Image
from utils.ai_analyzer import analyze_image
from utils.cost_estimator import estimate_cost_inr
from utils.genai_report import generate_ai_report

st.set_page_config(page_title="🚗 Damage AI", layout="wide")

st.title("🚗 Vehicle Damage Assessment AI (GenAI Powered)")



uploaded_file = st.file_uploader("Upload Vehicle Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=500)

    if st.button("Analyze🔎"):
        with st.spinner("Analyzing damage..."):
            result = analyze_image(image)
        damage_type = result.get("damage_type", "Dent")
        severity = result.get("severity", "Moderate")
        result["estimated_cost"] = estimate_cost_inr(damage_type, severity)

       

        # =========================
        # 🎯 BEAUTIFUL OUTPUT UI
        # =========================

        st.subheader("🔍 Damage Analysis")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Damage Type", result.get("damage_type", "N/A"))

        with col2:
            st.metric("Severity", result.get("severity", "N/A"))

        with col3:
            st.metric("Estimated Cost", result.get("estimated_cost", "N/A"))

        st.subheader("📝 Explanation")
        st.info(result.get("explanation", "No explanation available"))

        # =========================
        # 🧠 AI REPORT
        # =========================

        st.subheader("🧠 AI Generated Report")

        ai_report = generate_ai_report(result)
        st.write(ai_report)

        st.download_button(
            label="📄 Download AI Report",
            data=ai_report,
            file_name="vehicle_damage_report.txt"
        )