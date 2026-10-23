import streamlit as st

# Configure the page
st.set_page_config(page_title="Azwad's Portfolio", page_icon="👋", layout="centered")

# --- HERO SECTION ---
st.title("Azwad Islam Sachcha")
st.subheader("Software Engineer & M.Eng. Data Science/AI Student")
st.write("""
I am a software engineer with enterprise experience in C# and Angular, currently pursuing my Master's in Data Science and Artificial Intelligence in Munich. 
I specialize in bridging the gap between robust backend systems and advanced machine learning models.
""")

# Add a download button for your CV (ensure you put your PDF in the same folder)
# with open("resume.pdf", "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
# st.download_button(label="📄 Download Resume", data=PDFbyte, file_name="Azwad_Resume.pdf", mime="application/octet-stream")

st.divider()

# --- SKILLS SECTION ---
st.header("🛠️ Technical Stack")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Data Science**")
    st.write("- Python")
    st.write("- pandas & NumPy")
    st.write("- PyTorch / Bi-LSTMs")
with col2:
    st.write("**Software Engineering**")
    st.write("- C# & .NET")
    st.write("- Angular & JavaScript")
with col3:
    st.write("**Tools & Cloud**")
    st.write("- Git & GitHub")
    st.write("- Streamlit")

st.divider()

# --- PROJECTS & EXPERIENCE ---
st.header("🚀 Featured Work")

st.subheader("Audio Emotion Detection Model")
st.write("Developed a Transformer-based Hybrid Bidirectional LSTM model for emotion detection in audio. Achieved a final evaluation accuracy of 79%.")

st.subheader("Junior Software Engineer @ Threesquare")
st.write("Developed scalable enterprise applications utilizing C#, the .NET framework, and Angular. (Feb 2025 - Present)")

st.subheader("Sensor Data Processing")
st.write("Currently developing Python scripts for accelerometer calibration and sensor data processing using pandas and NumPy.")