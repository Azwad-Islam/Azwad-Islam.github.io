import streamlit as st

# Set layout to "wide" to use more screen space
st.set_page_config(page_title="Azwad's Portfolio", page_icon="👋", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    # 1. Inject CSS to make the sidebar image circular and control toolbar
    st.markdown("""
       <style>
        /* 1. Make ONLY the profile picture circular (ignores the logos) */
        [data-testid="stSidebar"] [data-testid="stImage"] img {
            border-radius: 50%;
            width: 200px;
            height: 200px;
            object-fit: cover;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }

        /* 2. Hide the right-side toolbar (Fork/Deploy/Menu) */
        [data-testid="stToolbar"] {
            display: none !important;
        }

        /* 3. Explicitly protect the sidebar toggle button so it never disappears */
        [data-testid="collapsedControl"] {
            display: block !important; 
            visibility: visible !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. Display the image
    st.image("azwad_profile_photo 3-4.png")

    st.title("Azwad Islam Sachcha")
    st.write("Software Engineer & M.Eng. Data Science Student")
    st.divider()
    st.markdown("""
            <div style="display: flex; flex-direction: column; gap: 14px; margin-top: 5px; margin-bottom: 5px;">
                <div style="display: flex; align-items: center;">
                    <span style="width: 28px; text-align: center; margin-right: 10px; font-size: 18px;">📍</span>
                    <span>Munich, Germany</span>
                </div>
                <!--
                <div style="display: flex; align-items: center;">
                    <span style="width: 28px; text-align: center; margin-right: 10px; font-size: 18px;">📞</span>
                    <span>(+49) 15511890842</span>
                </div>
                -->
                <div style="display: flex; align-items: center;">
                    <span style="width: 28px; text-align: center; margin-right: 10px; font-size: 18px;">📧</span>
                    <a href="mailto:azwad.sachcha@gmail.com">Email Me</a>
                </div>
                <div style="display: flex; align-items: center;">
                    <span style="width: 28px; display: flex; justify-content: center; margin-right: 10px;">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg" width="18" height="18" style="border-radius: 3px;">
                    </span>
                    <a href="https://www.linkedin.com/in/azwad-islam/" target="_blank">LinkedIn</a>
                </div>
                <div style="display: flex; align-items: center;">
                    <span style="width: 28px; display: flex; justify-content: center; margin-right: 10px;">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" width="18" height="18" style="filter: invert(100%);">
                    </span>
                    <a href="https://github.com/Azwad-Islam" target="_blank">GitHub</a>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.divider()
    # Resume download button in the sidebar
    with open("azwad_islam_cv.pdf", "rb") as pdf_file:
        st.download_button(
            label="📄 Download Resume",
            data=pdf_file.read(),
            file_name="Azwad_Islam_Sachcha_CV.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# --- MAIN CONTENT TABS ---
# Added a 4th tab specifically for Education
tab_about, tab_projects, tab_experience, tab_education = st.tabs(
    ["👤 About Me", "🚀 Projects", "💼 Experience", "🎓 Education"])

# --- TAB 1: ABOUT ME ---
with tab_about:
    st.header("Bridging Software Engineering and AI")
    st.write("""
    I am a software engineer with enterprise experience in C# and Angular, currently pursuing my Master's in Data Science and Artificial Intelligence at Munich University of Digital Technologies and Applied Sciences. 
    I specialize in Software engineering and honing my skills in AI and Data Science.
    """)

    st.subheader("🛠️ Technical Stack")
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.write("**Data Science & AI**")
            st.write("Python, PyTorch, TensorFlow, pandas, NumPy")
    with col2:
        with st.container(border=True):
            st.write("**Software Engineering**")
            st.write("C#, .NET/ASP.NET Core, Angular, JavaScript, Java, C++")
    with col3:
        with st.container(border=True):
            st.write("**Databases & Architecture**")
            st.write("PostgreSQL, MS SQL, Git, REST APIs")

    st.subheader("🌐 Languages")
    st.write("**English:** Proficient (C1/C2) | **German:** Basic (A1)")

# --- TAB 2: PROJECTS ---
with tab_projects:
    st.header("Featured Work")

    with st.expander("🎧 Audio Emotion Detection Model", expanded=True):
        st.write("**Technologies:** Python, Transformers, Bi-LSTM, PyTorch")
        st.write(
            "Developed a Hybrid BiLSTM-Transformer model for Speech Emotion Recognition using PyTorch, gaining hands-on experience with feature extraction and spectral analysis.")
        st.success("Achieved a final evaluation accuracy of 79%.")

    with st.expander("💻 Multi-Platform Restaurant POS System"):
        st.write("**Technologies:** C#, JavaScript, HTML, CSS, ASP.NET Core, PostgreSQL, Angular")
        st.write(
            "Engineered a multi-tenant Point of Sale system managing complex business logic and system architecture. Built scalable backend APIs and integrated PostgreSQL for secure data transactions.")

    with st.expander("📊 Sensor Data Processing"):
        st.write("**Technologies:** Python, pandas, NumPy")
        st.write(
            "Developed automated Python scripts for accelerometer calibration and raw sensor data processing as part of M.Eng coursework.")

# --- TAB 3: EXPERIENCE ---
with tab_experience:
    st.header("Professional Experience")

    st.subheader("Junior Software Engineer | Threesquare")
    st.caption("June 2025 - December 2025 | Dhaka, Bangladesh")
    st.write("""
    - Engineered scalable full-stack applications utilizing ASP.NET Core and Angular.
    - Built cross-platform applications using Blazor MAUI Hybrid, focusing on clean, maintainable code.
    - Integrated and managed backend data infrastructure utilizing PostgreSQL to ensure reliable data transactions.
    """)

    st.subheader("Software Engineering Intern | Threesquare")
    st.caption("Feb 2025 - June 2025 | Dhaka, Bangladesh")
    st.write("""
    - Assisted in developing a multi-tenant Point of Sale (POS) system for restaurant management.
    - Built scalable backend APIs with C# and the .NET Core Framework.
    - Implemented ASP.NET Identity Model for secure user authentication, registration, and role-based authorization.
    """)

    st.divider()

    st.header("Leadership & Volunteering")
    st.subheader("CEO & Tournament Admin | Sabertooth Wolves Gaming ORG")
    st.caption("Jan 2020 - Apr 2025")
    st.write(
        "Started as a player and advanced to CEO. Managed multiple esports teams across different countries and volunteered as a tournament administrator, coordinating events across South Asia.")

# --- TAB 4: EDUCATION ---
with tab_education:
    st.header("Academic Background")

    st.subheader("Master of Engineering: Data Science & Artificial Intelligence")
    st.write("**Munich University of Digital Technologies & Applied Sciences** | Munich, Germany")
    st.caption("Oct 2026 - Present")
    st.write("""
    - **Core Focus:** Generative AI, Large Language Models (LLMs), RAG, and autonomous agent architectures.
    - **Machine Learning:** Advanced predictive modeling, causal inference, and large-scale data processing.
    """)

    st.subheader("Bachelor of Science: Computer Science and Engineering")
    st.write("**American International University-Bangladesh (AIUB)** | Dhaka, Bangladesh")
    st.caption("Graduated: April 13, 2026")
    st.write("""
    - **Thesis:** Developed a Hybrid BiLSTM-Transformer model for Speech Emotion Recognition using PyTorch.
    - **Core Coursework:** Artificial Intelligence, Data Structures, Algorithms, Software Quality and Testing, and Object-Oriented Analysis.
    """)
st.divider()
st.caption("🚧 *This website is still under active development. Check back soon for live interactive models and updates.*")