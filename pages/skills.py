import streamlit as st


SKILL_CATEGORIES = [
    {
        "category": "Machine Learning & Data Science",
        "icon": "🧠",
        "skills": ["scikit-learn", "pandas", "NumPy", "Optuna", "MLflow", "Feature Engineering", "YOLOv8", "ResNet50", "TensorFlow", "Keras"],
    },
    {
        "category": "Data Engineering",
        "icon": "⚙️",
        "skills": ["SQL", "ETL Pipelines", "Data Quality Frameworks", "Docker", "GitHub Actions", "pytest"],
    },
    {
        "category": "Analytics & Visualisation",
        "icon": "📊",
        "skills": ["Power BI", "DAX", "Tableau", "Streamlit", "matplotlib", "seaborn", "Plotly", "EDA"],
    },
    {
        "category": "Languages & Tools",
        "icon": "🛠️",
        "skills": ["Python", "Git / GitHub", "Jupyter", "OpenCV", "Weights & Biases", "HuggingFace Spaces"],
    },
    {
        "category": "Business & Domain Knowledge",
        "icon": "🎯",
        "skills": ["Marketing Analytics", "Customer Segmentation", "Time Series Forecasting", "Operations Research", "A/B Testing", "Business Intelligence"],
    },
]

TECH_RADAR = [
    "Python", "SQL", "scikit-learn", "pandas", "NumPy", "MLflow", "Optuna",
    "Streamlit", "Docker", "GitHub Actions", "Power BI", "DAX", "Tableau",
    "PyTorch", "TensorFlow", "Keras", "Ultralytics YOLOv8", "ResNet50",
    "pytest", "Git", "matplotlib", "seaborn", "Jupyter",
    "Weights & Biases", "HuggingFace Spaces", "OpenCV", "Plotly",
]

CERTS = [
    ("Generative AI for Data Scientists", "2024"),
    ("Introduction to Statistics", "Stanford · Coursera · 2023"),
    ("Power BI for Business Intelligence", "Microsoft · Coursera · 2023"),
    ("Data Science Professional Certificate", "IBM · Coursera · 2023"),
]

TAG_COLORS = {
    "Machine Learning & Data Science": ("background:#1f2d3d;color:#79c0ff;border:1px solid #1f6feb;"),
    "Data Engineering":                ("background:#2d1f0e;color:#ffa657;border:1px solid #9e6a03;"),
    "Analytics & Visualisation":       ("background:#0d2d1f;color:#3fb950;border:1px solid #238636;"),
    "Languages & Tools":               ("background:#2d1a2d;color:#d2a8ff;border:1px solid #8957e5;"),
    "Business & Domain Knowledge":     ("background:#1f2d3d;color:#58a6ff;border:1px solid #388bfd;"),
}


def render():
    st.markdown('<div class="section-label">// tech stack & expertise</div>', unsafe_allow_html=True)
    st.markdown("# Skills")
    st.markdown(
        '<p style="font-size:15px;color:#8b949e;margin-top:-8px;margin-bottom:28px;">'
        "Technical toolkit built through academic work, internships, and personal projects.</p>",
        unsafe_allow_html=True,
    )

    # Category badge groups
    for group in SKILL_CATEGORIES:
        tag_css = TAG_COLORS.get(group["category"], "background:#1f2d3d;color:#79c0ff;border:1px solid #1f6feb;")
        badges_html = "".join(
            f'<span style="display:inline-block;{tag_css}border-radius:12px;'
            f'padding:4px 14px;font-size:13px;margin:4px;font-family:\'Space Mono\',monospace;">{s}</span>'
            for s in group["skills"]
        )
        st.markdown(
            f'<div class="card" style="margin-bottom:16px;">'
            f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">'
            f'<span style="font-size:22px;">{group["icon"]}</span>'
            f'<div style="font-family:\'Space Mono\',monospace;font-size:14px;color:#f0f6fc;font-weight:700;">{group["category"]}</div>'
            f'</div>'
            f'<div>{badges_html}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">// full tech radar</div>', unsafe_allow_html=True)

    radar_html = "".join(
        f'<span style="display:inline-block;background:#1f2d3d;color:#79c0ff;border:1px solid #1f6feb;'
        f'border-radius:12px;padding:4px 14px;font-size:13px;margin:4px;'
        f'font-family:\'Space Mono\',monospace;">{b}</span>'
        for b in TECH_RADAR
    )
    st.markdown(f'<div style="margin-bottom:28px;">{radar_html}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">// certifications</div>', unsafe_allow_html=True)

    for cert, year in CERTS:
        st.markdown(
            f'<div class="card" style="margin-bottom:10px;padding:14px 20px;display:flex;'
            f'justify-content:space-between;align-items:center;">'
            f'<div style="display:flex;align-items:center;gap:12px;">'
            f'<span style="font-size:18px;">🏅</span>'
            f'<div style="font-family:\'Space Mono\',monospace;font-size:13px;color:#f0f6fc;">{cert}</div>'
            f'</div>'
            f'<div style="font-size:11px;color:#58a6ff;font-family:\'Space Mono\',monospace;white-space:nowrap;">{year}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
