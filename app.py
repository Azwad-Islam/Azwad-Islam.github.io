import re
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Azwad's Portfolio", page_icon="👋", layout="wide")

# The site is hosted on GitHub Pages from index.html. This app shows the same page
# on azwad-islam.streamlit.app so old links keep working.
page = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
style = re.search(r"<style>.*?</style>", page, re.S).group(0)
body = re.search(r"<body>(.*)</body>", page, re.S).group(1)

# Hide Streamlit's own header and padding so the page fills the window.
streamlit_css = """<style>
  [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
  .stApp { background: #0B0D12; }
  .block-container, [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: none !important; }
  [data-testid="stVerticalBlock"] { gap: 0 !important; }
</style>"""

# Streamlit serves ./static at app/static/ (see .streamlit/config.toml).
body = body.replace('"static/', '"app/static/')

# JavaScript handles smooth scrolling and adds the live demo iframes.
st.html(streamlit_css + style + body, unsafe_allow_javascript=True)
