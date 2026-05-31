import streamlit as st


PROJECTS = [
    {
        "title": "Telco Customer Churn Prediction",
        "status": "live",
        "period": "May 2026",
        "description": (
            "End-to-end production ML system on the IBM Telco dataset (7,043 rows × 21 features). "
            "Built a full feature engineering pipeline (36 features after OHE), tuned Logistic Regression "
            "via Optuna (30 trials, 5-fold CV), achieving AUC 0.838 and Recall 0.80 — a 31pp lift over baseline. "
            "Deployed as a 4-page Streamlit dashboard with Docker, CI/CD via GitHub Actions, and MLflow tracking."
        ),
        "tags": ["scikit-learn", "Optuna", "MLflow", "Streamlit", "Docker", "GitHub Actions", "pandas"],
        "tag_type": "blue",
        "metrics": [
            ("AUC", "0.838"),
            ("Recall", "0.800"),
            ("Features", "36"),
            ("Trials", "30"),
        ],
        "live_url": "https://telco-churn-utkarsh.streamlit.app",
        "github_url": "https://github.com/UtkarshRai-ds/telco-churn-prediction",
        "highlight": "Targets top 51% risk tier → captures 87% of churners",
    },
    {
        "title": "SkyWatch — Satellite Object Detection",
        "status": "live",
        "period": "2024",
        "description": (
            "End-to-end computer vision pipeline for multi-class object detection in very-high-resolution "
            "satellite imagery using the NWPU VHR-10 dataset (800 images, 10 classes, 4,811 annotations). "
            "Trained and benchmarked YOLOv8n vs YOLOv8s under identical conditions on Google Colab T4 GPU. "
            "YOLOv8s achieved mAP50 of 0.697 with Recall 0.690; YOLOv8n offers 3.7× fewer parameters at "
            "comparable accuracy — surfacing a real speed/accuracy trade-off. Includes a bridge failure "
            "analysis: the most annotated class (29.5% of dataset) achieves only 0.03 mAP50 due to extreme "
            "aspect ratios and background confusion — intentionally exposed in the dashboard. "
            "Deployed as a 5-page Streamlit dashboard on HuggingFace Spaces with Docker and GitHub Actions CI."
        ),
        "tags": ["YOLOv8", "Ultralytics", "PyTorch", "Streamlit", "Docker", "GitHub Actions", "W&B", "OpenCV", "Plotly"],
        "tag_type": "orange",
        "metrics": [
            ("mAP50", "0.697"),
            ("Recall", "0.690"),
            ("Classes", "10"),
            ("Tests", "40"),
        ],
        "live_url": "https://huggingface.co/spaces/Utkarsh-DS/Skywatch-Detection",
        "github_url": "https://github.com/utkarsh26rai/skywatch-detection",
        "highlight": "Dual-model benchmark: YOLOv8n vs YOLOv8s with explicit failure mode analysis",
    },
    {
        "title": "Computer Vision Research — DIOR Dataset",
        "status": "research",
        "period": "2023",
        "description": (
            "Academic research on aerial object detection using the DIOR dataset (20 classes, remote sensing imagery). "
            "Implemented and benchmarked ResNet50 and YOLOv8 architectures, analysing performance across "
            "diverse geospatial object categories. Work contributed to a published conference paper and book chapter."
        ),
        "tags": ["YOLOv8", "ResNet50", "PyTorch", "DIOR dataset", "OpenCV"],
        "tag_type": "orange",
        "metrics": [
            ("Classes", "20"),
            ("Models", "2"),
            ("Output", "Paper"),
        ],
        "live_url": None,
        "github_url": None,
        "highlight": "Published conference paper & book chapter on remote sensing detection",
    },
]

PUBLICATIONS = [
    {
        "type": "Conference Paper",
        "date": "November 2022",
        "topic": "MetaVerse: The New Shape of Marketing",
        "venue": "International Marketing Conference · IIM Shillong",
    },
    {
        "type": "Book Chapter",
        "date": "February 2021",
        "topic": "PHARMEASY: A Fast Growing Healthtech Venture",
        "venue": "Emerging Contours of Business and Management · ISBN: 978-93-91842-41-3",
    },
]

STATUS_BADGE = {
    "live": ('<span style="background:#0d2d1f;color:#3fb950;border:1px solid #238636;'
             'border-radius:12px;padding:2px 10px;font-size:11px;font-family:\'Space Mono\',monospace;">● LIVE</span>'),
    "research": ('<span style="background:#2d1f0e;color:#ffa657;border:1px solid #9e6a03;'
                 'border-radius:12px;padding:2px 10px;font-size:11px;font-family:\'Space Mono\',monospace;">◆ RESEARCH</span>'),
}

TAG_STYLE = {
    "blue": "background:#1f2d3d;color:#79c0ff;border:1px solid #1f6feb;",
    "orange": "background:#2d1f0e;color:#ffa657;border:1px solid #9e6a03;",
}


def render():
    st.markdown('<div class="section-label">// what i\'ve built</div>', unsafe_allow_html=True)
    st.markdown("# Projects")
    st.markdown(
        '<p style="font-size:15px;color:#8b949e;margin-top:-8px;margin-bottom:24px;">'
        "End-to-end ML systems and computer vision research.</p>",
        unsafe_allow_html=True,
    )

    for proj in PROJECTS:
        tag_css = TAG_STYLE.get(proj["tag_type"], TAG_STYLE["blue"])
        tags_html = "".join(
            f'<span style="display:inline-block;{tag_css}border-radius:12px;'
            f'padding:2px 10px;font-size:12px;margin:2px;font-family:\'Space Mono\',monospace;">{t}</span>'
            for t in proj["tags"]
        )
        metrics_html = "".join(
            f'<div style="text-align:center;padding:10px 16px;background:#0d1117;border-radius:6px;border:1px solid #21262d;">'
            f'<div style="font-family:\'Space Mono\',monospace;font-size:18px;color:#58a6ff;font-weight:700;">{v}</div>'
            f'<div style="font-size:11px;color:#8b949e;margin-top:2px;">{k}</div></div>'
            for k, v in proj["metrics"]
        )
        links_html = ""
        if proj.get("live_url"):
            links_html += (
                f'<a href="{proj["live_url"]}" target="_blank" '
                f'style="color:#3fb950;font-size:13px;text-decoration:none;margin-right:16px;'
                f'font-family:\'Space Mono\',monospace;">▶ Live App</a>'
            )
        if proj.get("github_url"):
            links_html += (
                f'<a href="{proj["github_url"]}" target="_blank" '
                f'style="color:#58a6ff;font-size:13px;text-decoration:none;'
                f'font-family:\'Space Mono\',monospace;">⌥ GitHub</a>'
            )
        st.markdown(
            f'<div class="card" style="margin-bottom:20px;">'
            f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;flex-wrap:wrap;">'
            f'{STATUS_BADGE[proj["status"]]}'
            f'<span style="font-size:12px;color:#8b949e;">{proj["period"]}</span>'
            f'</div>'
            f'<div style="font-family:\'Space Mono\',monospace;font-size:18px;color:#f0f6fc;font-weight:700;margin-bottom:10px;">{proj["title"]}</div>'
            f'<div style="background:#161b22;border-left:3px solid #388bfd;padding:10px 14px;border-radius:0 6px 6px 0;'
            f'font-size:13px;color:#79c0ff;font-family:\'Space Mono\',monospace;margin-bottom:14px;">✦ {proj["highlight"]}</div>'
            f'<p style="font-size:14px;color:#8b949e;line-height:1.7;margin-bottom:14px;">{proj["description"]}</p>'
            f'<div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:14px;">{metrics_html}</div>'
            f'<div style="margin-bottom:14px;">{tags_html}</div>'
            f'<div>{links_html}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">// publications</div>', unsafe_allow_html=True)

    for pub in PUBLICATIONS:
        st.markdown(
            f'<div class="card" style="margin-bottom:12px;">'
            f'<div style="display:flex;align-items:flex-start;gap:14px;">'
            f'<span style="font-size:22px;">📄</span>'
            f'<div>'
            f'<div style="font-size:11px;color:#388bfd;font-family:\'Space Mono\',monospace;'
            f'text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;">{pub["type"]} · {pub["date"]}</div>'
            f'<div style="font-family:\'Space Mono\',monospace;font-size:14px;color:#f0f6fc;font-weight:700;margin-bottom:4px;">{pub["topic"]}</div>'
            f'<div style="font-size:12px;color:#8b949e;">{pub["venue"]}</div>'
            f'</div>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
