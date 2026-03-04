import streamlit as st
import requests

FLASK_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Crop Recommendation AI",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 Crop Recommendation System")
st.caption("AI-powered crop suggestion based on soil and climate data")

st.divider()

# -------- Input Form --------
with st.form("crop_form"):
    st.subheader("🌾 Soil Nutrients (ppm)")
    col1, col2, col3 = st.columns(3)

    with col1:
        nitrogen = st.number_input("Nitrogen (N)", 0, 150, 80)
    with col2:
        phosphorus = st.number_input("Phosphorus (P)", 0, 150, 50)
    with col3:
        potassium = st.number_input("Potassium (K)", 0, 150, 60)

    st.subheader("🌦 Climate Conditions")
    col4, col5, col6 = st.columns(3)

    with col4:
        temperature = st.number_input("Temperature (°C)", 5.0, 45.0, 30.0)
    with col5:
        humidity = st.number_input("Humidity (%)", 20.0, 100.0, 75.0)
    with col6:
        rainfall = st.number_input("Rainfall (mm)", 0.0, 400.0, 180.0)

    st.subheader("🧪 Soil Property")
    ph = st.number_input("Soil pH", 3.5, 9.0, 6.5)

    st.subheader("📝 Additional Context (Optional)")
    extra_notes = st.text_area(
        "Anything else? (season, location, irrigation, experience, issues)",
        placeholder="Example: This field is in eastern India, Kharif season, limited irrigation."
    )

    submitted = st.form_submit_button("🌱 Recommend Crop")

# -------- Prediction --------
if submitted:
    prompt = f"""
You are an expert agricultural advisor.

Your task:
1. Identify the MOST suitable crop based on the data.
2. Explain the reasoning in detail (at least 3 sentences).
3. Provide 3 practical farming recommendations.

IMPORTANT RULES:
- Be specific to the given soil and climate values.
- Do NOT answer in one line.
- Use simple, farmer-friendly language.

Soil and climate data:
Nitrogen: {nitrogen} ppm
Phosphorus: {phosphorus} ppm
Potassium: {potassium} ppm
Temperature: {temperature}°C
Humidity: {humidity}%
Rainfall: {rainfall} mm
Soil pH: {ph}

Farmer context:
{extra_notes if extra_notes.strip() else "No additional context provided."}

Respond strictly in this format:

Crop:
<crop name>

Why this crop is suitable:
<detailed explanation, minimum 3 sentences>

Farming tips:
- Tip 1
- Tip 2
- Tip 3
"""

    with st.spinner("Analyzing soil and climate data..."):
        response = requests.post(
            FLASK_URL,
            json={"text": prompt}
        )

    if response.status_code == 200:
        result = response.json()["crop"]

        st.success("✅ Recommendation Generated")

        # Flexible display (works even if model outputs only crop name)
        if "Crop:" in result:
            st.markdown(result)
        else:
            st.markdown(f"""
### 🌾 Recommended Crop
**{result.upper()}**

_(Explanation support will improve with further fine-tuning.)_
""")
    else:
        st.error("❌ Unable to get prediction. Check server status.")