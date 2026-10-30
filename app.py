from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Azwad's Portfolio", page_icon="👋", layout="wide")

# The whole page (layout, styles and content) lives in site.html.
# The resume and photo are served from ./static (see .streamlit/config.toml).
# JavaScript is only used for smooth scrolling to sections from the nav links.
st.html(Path(__file__).parent / "site.html", unsafe_allow_javascript=True)
