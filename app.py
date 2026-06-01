import streamlit as st

st.set_page_config(
    page_title="Utkarsh Rai | Data Scientist",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Global CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #0d1117;
    border-right: 1px solid #21262d;
}

[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stMarkdown {
    color: #8b949e;
}

[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #f0f6fc;
    font-family: 'Space Mono', monospace;
}

/* Main content */
.main {
    background: #0d1117;
    color: #c9d1d9;
}

.stApp {
    background: #0d1117;
}

/* Headings */
h1, h2, h3 {
    font-family: 'Space Mono', monospace !important;
    color: #f0f6fc !important;
}

/* Nav pills */
.nav-pill {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 500;
    margin: 4px;
    cursor: pointer;
    border: 1px solid #30363d;
    color: #8b949e;
    text-decoration: none;
    transition: all 0.2s;
}

/* Cards */
.card {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 10px;
    padding: 24px;
    margin-bottom: 16px;
    transition: border-color 0.2s;
}

.card:hover {
    border-color: #388bfd;
}

.tag {
    display: inline-block;
    background: #1f2d3d;
    color: #79c0ff;
    border: 1px solid #1f6feb;
    border-radius: 12px;
    padding: 2px 10px;
    font-size: 12px;
    margin: 2px;
    font-family: 'Space Mono', monospace;
}

.tag-orange {
    background: #2d1f0e;
    color: #ffa657;
    border-color: #9e6a03;
}

.tag-green {
    background: #0d2d1f;
    color: #3fb950;
    border-color: #238636;
}

.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #388bfd;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.metric-box {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 8px;
    padding: 16px;
    text-align: center;
}

.metric-value {
    font-family: 'Space Mono', monospace;
    font-size: 28px;
    font-weight: 700;
    color: #58a6ff;
}

.metric-label {
    font-size: 12px;
    color: #8b949e;
    margin-top: 4px;
}

.highlight-text {
    color: #58a6ff;
    font-family: 'Space Mono', monospace;
}

.divider {
    border: none;
    border-top: 1px solid #21262d;
    margin: 24px 0;
}

/* Skill bars */
.skill-bar-bg {
    background: #21262d;
    border-radius: 4px;
    height: 6px;
    margin: 6px 0 12px;
}

.skill-bar-fill {
    height: 6px;
    border-radius: 4px;
    background: linear-gradient(90deg, #1f6feb, #388bfd);
}

/* Timeline */
.timeline-item {
    border-left: 2px solid #21262d;
    padding-left: 20px;
    margin-bottom: 24px;
    position: relative;
}

.timeline-dot {
    width: 10px;
    height: 10px;
    background: #388bfd;
    border-radius: 50%;
    position: absolute;
    left: -6px;
    top: 4px;
}

/* Buttons */
.stButton > button {
    background: #161b22;
    color: #58a6ff;
    border: 1px solid #1f6feb;
    border-radius: 6px;
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    padding: 8px 20px;
    transition: all 0.2s;
}

.stButton > button:hover {
    background: #1f6feb20;
    border-color: #388bfd;
    color: #79c0ff;
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Photo
    import os
    from PIL import Image
    photo_path = os.path.join(os.path.dirname(__file__), "assets", "photo.jpg")
    if not os.path.exists(photo_path):
        photo_path = os.path.join(os.path.dirname(__file__), "assets", "photo.png")
    if os.path.exists(photo_path):
        img = Image.open(photo_path)
        st.markdown('<div style="text-align:center; padding: 20px 0 0;">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True, output_format="JPEG")
        st.markdown("""
        <div style="text-align:center; padding: 8px 0 10px;">
            <div style="font-family:'Space Mono',monospace; font-size:16px; color:#f0f6fc; font-weight:700;">Utkarsh Rai</div>
            <div style="font-size:13px; color:#8b949e; margin-top:4px;">Data Scientist · Berlin</div>
        </div>
        <hr style="border:none; border-top:1px solid #21262d; margin:12px 0;">
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="text-align:center; padding: 20px 0 10px;">
            <div style="width:72px; height:72px; background:#1f6feb; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 12px; font-family:'Space Mono',monospace; font-size:22px; font-weight:700; color:#f0f6fc;">UR</div>
            <div style="font-family:'Space Mono',monospace; font-size:16px; color:#f0f6fc; font-weight:700;">Utkarsh Rai</div>
            <div style="font-size:13px; color:#8b949e; margin-top:4px;">Data Scientist · Berlin</div>
        </div>
        <hr style="border:none; border-top:1px solid #21262d; margin:12px 0;">
        """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["🏠 About Me", "🚀 Projects", "🛠️ Skills", "📄 Resume", "✉️ Contact"],
        label_visibility="collapsed"
    )

    st.markdown("""
    <hr style="border:none; border-top:1px solid #21262d; margin:12px 0;">
    <div style="font-size:12px; color:#8b949e; text-align:center; padding-bottom:10px;">
        <a href="https://github.com/UtkarshRai-ds" target="_blank" style="color:#58a6ff; text-decoration:none; margin:0 6px;">GitHub</a> ·
        <a href="https://www.linkedin.com/in/utkarshrai-ds" target="_blank" style="color:#58a6ff; text-decoration:none; margin:0 6px;">LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)

# Route pages
if page == "🏠 About Me":
    from pages import about
    about.render()
elif page == "🚀 Projects":
    from pages import projects
    projects.render()
elif page == "🛠️ Skills":
    from pages import skills
    skills.render()
elif page == "📄 Resume":
    from pages import resume
    resume.render()
elif page == "✉️ Contact":
    from pages import contact
    contact.render()
