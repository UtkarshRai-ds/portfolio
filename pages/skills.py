import streamlit as st


SKILL_GROUPS = [
    {
        "category": "Machine Learning & Data Science",
        "icon": "🧠",
        "skills": [
            ("scikit-learn", 90),
            ("pandas / NumPy", 92),
            ("Optuna (HPO)", 85),
            ("MLflow", 80),
            ("YOLOv8 / ResNet50", 75),
            ("Feature Engineering", 88),
        ],
    },
    {
        "category": "Data Engineering",
        "icon": "⚙️",
        "skills": [
            ("SQL / ETL Pipelines", 85),
            ("Data Quality Frameworks", 82),
            ("Docker", 78),
            ("GitHub Actions (CI/CD)", 75),
            ("pytest", 78),
        ],
    },
    {
        "category": "Analytics & Visualisation",
        "icon": "📊",
        "skills": [
            ("Power BI / DAX", 85),
            ("Streamlit", 90),
            ("matplotlib / seaborn", 88),
            ("EDA", 92),
        ],
    },
    {
        "category": "Languages & Tools",
        "icon": "🛠️",
        "skills": [
            ("Python", 92),
            ("SQL", 85),
            ("Git / GitHub", 88),
            ("German (A2 → B2)", 30),
        ],
    },
]

TECH_BADGES = [
    "Python", "SQL", "scikit-learn", "pandas", "NumPy", "MLflow", "Optuna",
    "Streamlit", "Docker", "GitHub Actions", "Power BI", "DAX",
    "PyTorch", "Ultralytics YOLOv8", "ResNet50", "pytest", "ruff", "Git",
    "AWS Cloud", "matplotlib", "seaborn", "Jupyter",
    "Weights & Biases", "HuggingFace Spaces", "OpenCV", "Plotly",
]

CERTS = [
    ("AWS Cloud Practitioner", "Amazon Web Services", "2023"),
    ("MSc Data Analytics", "Berlin School of Business and Innovation", "2024"),
    ("MBA — Business Analytics & Marketing", "Dual Specialisation", "2023"),
]


def skill_bar(name, level):
    color = "#388bfd" if level >= 80 else "#1f6feb" if level >= 60 else "#8b949e"
    return f"""
    <div style="margin-bottom:14px;">
        <div style="display:flex;justify-content:space-between;margin-bottom:5px;">
            <span style="font-size:13px;color:#c9d1d9;">{name}</span>
            <span style="font-size:12px;font-family:'Space Mono',monospace;color:#8b949e;">{level}%</span>
        </div>
        <div class="skill-bar-bg">
            <div class="skill-bar-fill" style="width:{level}%;background:{color};"></div>
        </div>
    </div>
    """


def render():
    st.markdown('<div class="section-label">// tech stack & expertise</div>', unsafe_allow_html=True)
    st.markdown("# Skills")
    st.markdown(
        '<p style="font-size:15px;color:#8b949e;margin-top:-8px;margin-bottom:24px;">'
        "Technical toolkit built through academic work, internships, and personal projects.</p>",
        unsafe_allow_html=True,
    )

    # Skill bar groups
    cols = st.columns(2)
    for i, group in enumerate(SKILL_GROUPS):
        with cols[i % 2]:
            bars_html = "".join(skill_bar(s, l) for s, l in group["skills"])
            st.markdown(f"""
            <div class="card" style="margin-bottom:20px;">
                <div style="font-size:20px;margin-bottom:6px;">{group["icon"]}</div>
                <div style="font-family:'Space Mono',monospace;font-size:14px;color:#f0f6fc;
                            font-weight:700;margin-bottom:16px;">{group["category"]}</div>
                {bars_html}
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">// full tech radar</div>', unsafe_allow_html=True)

    badges_html = "".join(
        f'<span style="display:inline-block;background:#1f2d3d;color:#79c0ff;border:1px solid #1f6feb;'
        f'border-radius:12px;padding:4px 14px;font-size:13px;margin:4px;'
        f'font-family:\'Space Mono\',monospace;">{b}</span>'
        for b in TECH_BADGES
    )
    st.markdown(f'<div style="margin-bottom:28px;">{badges_html}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">// certifications & credentials</div>', unsafe_allow_html=True)

    cert_cols = st.columns(3)
    for col, (cert, org, year) in zip(cert_cols, CERTS):
        with col:
            st.markdown(f"""
            <div class="card" style="min-height:110px;">
                <div style="font-size:22px;margin-bottom:8px;">🏅</div>
                <div style="font-family:'Space Mono',monospace;font-size:13px;color:#f0f6fc;
                            font-weight:700;margin-bottom:6px;">{cert}</div>
                <div style="font-size:12px;color:#8b949e;">{org}</div>
                <div style="font-size:11px;color:#58a6ff;margin-top:4px;
                            font-family:'Space Mono',monospace;">{year}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">// research & publications</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div style="display:flex;align-items:flex-start;gap:14px;">
            <div style="font-size:24px;">📄</div>
            <div>
                <div style="font-family:'Space Mono',monospace;font-size:14px;color:#f0f6fc;
                            font-weight:700;margin-bottom:6px;">Published Academic Work</div>
                <div style="font-size:13px;color:#8b949e;line-height:1.7;">
                    Book chapter and conference paper on computer vision and object detection 
                    (ResNet50, YOLOv8 on DIOR dataset). Contributes to reproducible ML research 
                    in remote sensing applications.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
