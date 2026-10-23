import streamlit as st

# Set layout to "wide" to use more screen space
st.set_page_config(page_title="Azwad's Portfolio", page_icon="👋", layout="wide")
st.markdown("""
    <style>
    /* Hide the Streamlit toolbar at the top right */
    div[data-testid="stToolbar"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)
# --- SIDEBAR ---
with st.sidebar:
    # st.image("profile_pic.jpg") #
    with st.sidebar:
        # 1. Inject CSS to make the sidebar image circular
        st.markdown("""
            <style>
            [data-testid="stSidebar"] img {
                border-radius: 50%;
                width: 200px; /* Adjust size as needed */
                height: 200px;
                object-fit: cover;
                display: block;
                margin-left: auto;
                margin-right: auto;
            }
            </style>
            """, unsafe_allow_html=True)

        # 2. Display the image
        st.image("profile_photo.jpg")
    st.title("Azwad Islam Sachcha")
    st.write("Software Engineer & M.Eng. Data Science Student")
    st.divider()
    st.write("📍 Munich, Germany")
    st.write("📧 [Email Me](mailto:azwad.sachcha@gmail.com)")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/azwad-islam/) | [GitHub](https://github.com/Azwad-Islam)")

    st.divider()
    # Resume download can live neatly in the sidebar
    # with open("resume.pdf", "rb") as pdf_file:
    #     st.download_button("📄 Download Resume", pdf_file.read(), "Azwad_Resume.pdf", "application/octet-stream")

# --- MAIN CONTENT TABS ---
tab_about, tab_projects, tab_experience = st.tabs(["👤 About Me", "🚀 Projects", "💼 Experience"])

# --- TAB 1: ABOUT ME ---
with tab_about:
    st.header("Bridging Software Engineering and AI")
    st.write("""
    I am a software engineer with enterprise experience in C# and Angular, currently pursuing my Master's in Data Science and Artificial Intelligence at Munich University of Digital Technologies and Applied Sciences. 
    I specialize in Software engineering and honing my skills in AI and Data Science.
    """)

    st.subheader("🛠️ Technical Stack")
    col1, col2, col3 = st.columns(3)

    # Using bordered containers to create a "card" effect
    with col1:
        with st.container(border=True):
            st.write("**Data Science & AI**")
            st.write("Python, pandas, NumPy, PyTorch")
    with col2:
        with st.container(border=True):
            st.write("**Full-Stack Engineering**")
            st.write("C#, .NET, Angular, JavaScript")
    with col3:
        with st.container(border=True):
            st.write("**Tools & Architecture**")
            st.write("Git, Streamlit, REST APIs")

# --- TAB 2: PROJECTS ---
with tab_projects:
    st.header("Featured Work")

    # Expanders keep the UI clean while holding lots of detail
    with st.expander("🎧 Audio Emotion Detection Model", expanded=True):
        st.write("**Technologies:** Python, Transformers, Bi-LSTM")
        st.write("Developed a Transformer-based Hybrid Bidirectional LSTM model for emotion detection in audio.")
        st.success("Achieved a final evaluation accuracy of 79%.")  # .success gives it a nice green highlight

    with st.expander("📊 Sensor Data Processing"):
        st.write("**Technologies:** Python, pandas, NumPy")
        st.write(
            "Developed automated Python scripts for accelerometer calibration and raw sensor data processing as part of M.Eng coursework.")

# --- TAB 3: EXPERIENCE ---
with tab_experience:
    st.header("Professional Experience")

    st.subheader("Software Engineer | Threesquare")
    st.caption("Feb 2025 - Present")
    st.write("""
    * Promoted from Intern to full-time Junior Software Engineer in June 2025.
    * Engineered scalable enterprise applications utilizing C# and the .NET framework.
    * Developed dynamic frontend user interfaces with Angular and JavaScript.
    """)