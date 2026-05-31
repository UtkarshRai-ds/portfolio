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
            "role": "Data Science Freelancer",
            "company": "Self Employed",
            "period": "Sep 2024 – Oct 2025",
            "location": "Berlin, Germany",
            "bullets": [
                "Loaded, preprocessed, and augmented image datasets using TensorFlow (Sequential API); designed and trained CNN-based classifiers achieving high accuracy on client-specific use cases.",
                "Fine-tuned ML models (scikit-learn, Keras, TensorFlow) through hyperparameter optimisation and feature engineering, increasing predictive performance by up to 20%.",
                "Engineered end-to-end ETL pipelines for ingesting, cleaning, and transforming structured and unstructured data; monitored pipeline performance for reliability and efficiency.",
                "Created SQL-based ETL workflows, reducing data processing and load times by 30% while boosting reporting reliability.",
                "Extracted and parsed local data from PDFs and spreadsheets with Python, automating contact-list ingestion scripts.",
            ],
        },
        {
            "role": "Data Analytics Intern",
            "company": "APEX Byte",
            "period": "Jun 2024 – Oct 2024",
            "location": "Noida, India (Remote)",
            "bullets": [
                "Implemented data-quality checks (missing values, duplicates, outliers) using pandas and stored procedures, achieving >99% data integrity for downstream analytics.",
                "Wrote and optimised complex SQL queries and indexed key tables, cutting average query runtime by 27% and accelerating insights delivery.",
                "Partnered with product and marketing teams to translate business requirements into data models and KPIs, enabling data-driven decision-making across the organisation.",
            ],
        },
        {
            "role": "Business Analytics Intern",
            "company": "Goodspace Technologies Pvt. Ltd.",
            "period": "Jul 2022 – Sep 2022",
            "location": "Delhi, India",
            "bullets": [
                "Developed and validated linear and logistic regression models to predict user churn, improving retention strategies by 15%.",
                "Performed data mining and exploratory analysis on 100k+ user events using Python (pandas, NumPy), increasing conversion rate by 12%.",
                "Modelled datasets using Power BI and DAX, improving data accuracy by 30%.",
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
            "period": "2023 – 2025",
            "location": "Berlin, Germany",
            "detail": "Machine Learning · Statistical Modelling · Data Engineering · Production Deployment",
        },
        {
            "degree": "BBA + MBA — Business Analytics & Marketing (Integrated)",
            "institution": "Sharda University",
            "period": "2019 – 2023",
            "location": "Greater Noida, India",
            "detail": "Marketing Strategy · Operations Research · Business Intelligence · Consumer Analytics",
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
        ("ML & Modelling", ["scikit-learn", "Optuna", "MLflow", "YOLOv8", "TensorFlow", "Keras"]),
        ("Data Engineering", ["SQL", "ETL Pipelines", "Docker", "GitHub Actions", "pytest"]),
        ("Analytics & BI", ["Power BI", "DAX", "Streamlit", "pandas", "EDA", "Tableau"]),
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
