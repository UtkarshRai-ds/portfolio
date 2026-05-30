import streamlit as st
import os


def render():
    st.markdown('<div class="section-label">// curriculum vitae</div>', unsafe_allow_html=True)
    st.markdown("# Resume")
    st.markdown(
        '<p style="font-size:15px;color:#8b949e;margin-top:-8px;margin-bottom:24px;">'
        "Full professional background — experience, education, and skills at a glance.</p>",
        unsafe_allow_html=True,
    )

    # Download button
    resume_path = os.path.join(os.path.dirname(__file__), "..", "assets", "Utkarsh_Rai_CV.pdf")
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as f:
            st.download_button(
                label="⬇  Download CV (PDF)",
                data=f.read(),
                file_name="Utkarsh_Rai_CV.pdf",
                mime="application/pdf",
            )
    else:
        st.info("💡 Place your PDF CV at `assets/Utkarsh_Rai_CV.pdf` to enable the download button.")

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Experience
    st.markdown('<div class="section-label">// experience</div>', unsafe_allow_html=True)

    experiences = [
        {
            "role": "Data Science Intern",
            "company": "APEX Byte",
            "period": "2023",
            "location": "Remote",
            "bullets": [
                "Designed and implemented SQL-based ETL pipelines for structured data ingestion and transformation.",
                "Built automated data quality framework with 5 validation checks (nulls, types, ranges, duplicates, referential integrity) using pandas.",
                "Reduced manual QA overhead through scripted validation layers, improving pipeline reliability.",
            ],
        },
        {
            "role": "Data Analyst Intern",
            "company": "Goodspace",
            "period": "2023",
            "location": "Remote",
            "bullets": [
                "Performed comprehensive EDA on business datasets using Python (pandas, matplotlib, seaborn).",
                "Built interactive Power BI dashboards with DAX measures for stakeholder reporting.",
                "Delivered executive summaries translating complex data patterns into actionable business recommendations.",
            ],
        },
    ]

    for exp in experiences:
        bullets_html = "".join(
            f'<li style="font-size:13px;color:#8b949e;margin-bottom:6px;line-height:1.6;">{b}</li>'
            for b in exp["bullets"]
        )
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div style="display:flex;justify-content:space-between;flex-wrap:wrap;margin-bottom:4px;">
                <div style="font-family:'Space Mono',monospace;font-size:15px;color:#f0f6fc;font-weight:700;">
                    {exp["role"]}
                </div>
                <div style="font-size:12px;color:#8b949e;font-family:'Space Mono',monospace;">{exp["period"]}</div>
            </div>
            <div style="font-size:13px;color:#58a6ff;margin-bottom:10px;">{exp["company"]} · {exp["location"]}</div>
            <ul style="margin:0;padding-left:16px;">{bullets_html}</ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Education
    st.markdown('<div class="section-label">// education</div>', unsafe_allow_html=True)

    educations = [
        {
            "degree": "MSc Data Analytics",
            "institution": "Berlin School of Business and Innovation",
            "period": "2023 – 2024",
            "location": "Berlin, Germany",
            "detail": "Focus: Machine Learning, Statistical Modelling, Data Engineering",
        },
        {
            "degree": "MBA — Business Analytics & Marketing (Dual)",
            "institution": "Sharda University, Greater Noida",
            "period": "2021 – 2023",
            "location": "India",
            "detail": "Dual specialisation in data-driven strategy and marketing analytics",
        },
    ]

    for edu in educations:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div style="display:flex;justify-content:space-between;flex-wrap:wrap;margin-bottom:4px;">
                <div style="font-family:'Space Mono',monospace;font-size:15px;color:#f0f6fc;font-weight:700;">
                    {edu["degree"]}
                </div>
                <div style="font-size:12px;color:#8b949e;font-family:'Space Mono',monospace;">{edu["period"]}</div>
            </div>
            <div style="font-size:13px;color:#58a6ff;margin-bottom:6px;">{edu["institution"]} · {edu["location"]}</div>
            <div style="font-size:13px;color:#8b949e;">{edu["detail"]}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Key skills summary
    st.markdown('<div class="section-label">// core competencies</div>', unsafe_allow_html=True)

    competency_cols = st.columns(3)
    competencies = [
        ("ML & Modelling", ["scikit-learn", "Optuna", "MLflow", "YOLOv8", "ResNet50"]),
        ("Data Engineering", ["SQL", "ETL Pipelines", "Docker", "GitHub Actions", "pytest"]),
        ("Analytics & BI", ["Power BI", "DAX", "Streamlit", "pandas", "EDA"]),
    ]
    for col, (title, items) in zip(competency_cols, competencies):
        with col:
            items_html = "".join(
                f'<div style="font-size:13px;color:#c9d1d9;padding:5px 0;border-bottom:1px solid #21262d;">'
                f'<span style="color:#388bfd;margin-right:8px;">▸</span>{item}</div>'
                for item in items
            )
            st.markdown(f"""
            <div class="card">
                <div style="font-family:'Space Mono',monospace;font-size:13px;color:#f0f6fc;
                            margin-bottom:12px;font-weight:700;">{title}</div>
                {items_html}
            </div>
            """, unsafe_allow_html=True)
