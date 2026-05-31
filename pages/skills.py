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
            ("German (B1 level)", 45),
        ],
    },
]

TECH_BADGES = [
    "Python", "SQL", "scikit-learn", "pandas", "NumPy", "MLflow", "Optuna",
    "Streamlit", "Docker", "GitHub Actions", "Power BI", "DAX", "Tableau",
    "PyTorch", "TensorFlow", "Keras", "Ultralytics YOLOv8", "ResNet50",
    "pytest", "ruff", "Git", "matplotlib", "seaborn", "Jupyter",
    "Weights & Biases", "HuggingFace Spaces", "OpenCV", "Plotly",
]

CERTS = [
    ("Generative AI for Data Scientists", "2024"),
    ("AWS Cloud Practitioner", "2023"),
    ("Introduction to Statistics", "Stanford · Coursera · 2023"),
    ("Power BI for Business Intelligence", "Microsoft · Coursera · 2023"),
    ("Data Science Professional Certificate", "IBM · Coursera · 2023"),
]

PUBLICATIONS = [
    {
        "type": "Conference Paper",
        "title": "Presented at International Marketing Conference",
        "venue": "Indian Institute of Management Shillong",
        "topic": "MetaVerse: The New Shape of Marketing",
        "date": "November 2022",
    },
    {
        "type": "Book Chapter",
        "title": "Published in 'Emerging Contours of Business and Management'",
        "venue": "ISBN: 978-93-91842-41-3",
        "topic": "PHARMEASY: A Fast Growing Healthtech Venture",
        "date": "February 2021",
    },
]


def skill_bar(name, level):
    color = "#388bfd" if level >= 80 else "#1f6feb" if level >= 60 else "#8b949e"
    return (
        f'<div style="margin-bottom:14px;">'
        f'<div style="display:flex;justify-content:space-between;margin-bottom:5px;">'
        f'<span style="font-size:13px;color:#c9d1d9;">{name}</span>'
        f'<span style="font-size:12px;font-family:\'Space Mono\',monospace;color:#8b949e;">{level}%</span>'
        f'</div>'
        f'<div style="background:#21262d;border-radius:4px;height:6px;">'
        f'<div style="width:{level}%;height:6px;border-radius:4px;background:{color};"></div>'
        f'</div>'
        f'</div>'
    )


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
            card_html = (
                f'<div class="card" style="margin-bottom:20px;">'
                f'<div style="font-size:20px;margin-bottom:6px;">{group["icon"]}</div>'
                f'<div style="font-family:\'Space Mono\',monospace;font-size:14px;color:#f0f6fc;'
                f'font-weight:700;margin-bottom:16px;">{group["category"]}</div>'
                f'{bars_html}'
                f'</div>'
            )
            st.markdown(card_html, unsafe_allow_html=True)

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

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">// research & publications</div>', unsafe_allow_html=True)

    for pub in PUBLICATIONS:
        st.markdown(
            f'<div class="card" style="margin-bottom:12px;">'
            f'<div style="display:flex;align-items:flex-start;gap:14px;">'
            f'<span style="font-size:22px;">📄</span>'
            f'<div>'
            f'<div style="font-size:11px;color:#388bfd;font-family:\'Space Mono\',monospace;'
            f'text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;">{pub["type"]} · {pub["date"]}</div>'
            f'<div style="font-family:\'Space Mono\',monospace;font-size:13px;color:#f0f6fc;'
            f'font-weight:700;margin-bottom:4px;">{pub["topic"]}</div>'
            f'<div style="font-size:13px;color:#8b949e;margin-bottom:2px;">{pub["title"]}</div>'
            f'<div style="font-size:12px;color:#58a6ff;">{pub["venue"]}</div>'
            f'</div>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
