import streamlit as st


def render():
    st.markdown('<div class="section-label">// who am i</div>', unsafe_allow_html=True)
    st.markdown("# Utkarsh Rai")
    st.markdown(
        '<p style="font-size:20px; color:#8b949e; margin-top:-10px;">Data Scientist & Business Analyst · Berlin, Germany 🇩🇪</p>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class="card">
        <p style="font-size:15px; color:#c9d1d9; line-height:1.9;">
        I sit at the intersection of <span class="highlight-text">data science and business strategy</span> — 
        a combination that's rarer than it sounds. With an 
        <span class="highlight-text">MSc in Data Analytics</span> (Berlin School of Business and Innovation) 
        and a <span class="highlight-text">BBA + MBA in Business Analytics & Marketing</span> (Sharda University), 
        I bring both the technical depth to build ML systems and the business fluency to know 
        <em>why</em> they matter.
        </p>
        <p style="font-size:15px; color:#c9d1d9; line-height:1.9; margin-top:14px;">
        My work spans the full stack of data-driven decision-making: designing predictive models, 
        engineering production pipelines, building BI dashboards, and translating complex outputs 
        into decisions that stakeholders can act on. I'm drawn to problems where the real challenge 
        isn't just the model — it's understanding the business well enough to ask the right question.
        </p>
        <p style="font-size:15px; color:#c9d1d9; line-height:1.9; margin-top:14px;">
        I'm fluent across the analytics spectrum — 
        <span class="highlight-text">time series forecasting, customer segmentation, operations research, 
        marketing analytics, A/B testing, and computer vision</span> — and comfortable bridging 
        the gap between a Jupyter notebook and a boardroom recommendation. I'm also curious about 
        <span class="highlight-text">AI product roles</span> where technical literacy and business 
        judgment converge.
        </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-label" style="margin-top:24px;">// what i bring</div>', unsafe_allow_html=True)

        cols = st.columns(3)
        highlights = [
            ("🧠", "ML & Predictive Analytics", "End-to-end pipelines: feature engineering, model tuning, MLflow, deployment"),
            ("📊", "Business Intelligence", "Power BI, Tableau, DAX — turning raw data into executive-ready insights"),
            ("🎯", "Business Problem Solving", "Marketing analytics, segmentation, forecasting, ops research — strategy meets data"),
        ]
        for c, (icon, title, desc) in zip(cols, highlights):
            with c:
                st.markdown(f"""
                <div class="card" style="text-align:center; min-height:160px;">
                    <div style="font-size:28px; margin-bottom:10px;">{icon}</div>
                    <div style="font-family:'Space Mono',monospace; font-size:12px; color:#f0f6fc; margin-bottom:8px;">{title}</div>
                    <div style="font-size:12px; color:#8b949e; line-height:1.6;">{desc}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown('<div class="section-label" style="margin-top:28px;">// domains i work across</div>', unsafe_allow_html=True)

        domains = [
            ("📈", "Time Series & Forecasting", "Demand planning, trend analysis, temporal modelling"),
            ("🛒", "Marketing Analytics", "Customer segmentation, churn prediction, campaign analysis, A/B testing"),
            ("⚙️", "Operations Research", "Optimisation, process efficiency, data-driven operations"),
            ("👁️", "Computer Vision", "Object detection, satellite imagery, YOLOv8, ResNet50"),
            ("🗃️", "Data Engineering", "ETL pipelines, data quality frameworks, SQL, Docker, CI/CD"),
            ("🤖", "AI Product Thinking", "Translating ML capabilities into product features and business value"),
        ]

        d_cols = st.columns(2)
        for i, (icon, title, desc) in enumerate(domains):
            with d_cols[i % 2]:
                st.markdown(f"""
                <div class="card" style="margin-bottom:10px; padding:16px 20px;">
                    <div style="display:flex; align-items:flex-start; gap:12px;">
                        <span style="font-size:20px;">{icon}</span>
                        <div>
                            <div style="font-family:'Space Mono',monospace; font-size:12px; 
                                        color:#f0f6fc; font-weight:700; margin-bottom:4px;">{title}</div>
                            <div style="font-size:12px; color:#8b949e; line-height:1.6;">{desc}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-label">// quick stats</div>', unsafe_allow_html=True)
        stats = [
            ("3+", "Years Experience"),
            ("5+", "Projects Shipped"),
            ("2", "Research Publications"),
            ("2", "Degrees"),
        ]
        for val, label in stats:
            st.markdown(f"""
            <div class="metric-box" style="margin-bottom:12px;">
                <div class="metric-value">{val}</div>
                <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-label" style="margin-top:20px;">// currently</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card">
            <div style="font-size:13px; color:#c9d1d9; line-height:1.9;">
                <div style="margin-bottom:8px;">🔍 Open to DS, DA, BA & Consultant roles in Germany</div>
                <div style="margin-bottom:8px;">🤖 Curious about AI Product Management</div>
                <div style="margin-bottom:8px;">🇩🇪 Learning German (A2 → B2)</div>
                <div>📝 Building in public on LinkedIn</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-label" style="margin-top:20px;">// open to</div>', unsafe_allow_html=True)
        roles = [
            "Junior Data Scientist",
            "Data Analyst",
            "Business Analyst",
            "Data Consultant",
            "AI Product (curious)",
        ]
        roles_html = "".join(
            f'<div style="font-size:12px;color:#79c0ff;padding:5px 0;border-bottom:1px solid #21262d;">'
            f'<span style="color:#388bfd;margin-right:8px;">▸</span>{r}</div>'
            for r in roles
        )
        st.markdown(f'<div class="card">{roles_html}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">// education</div>', unsafe_allow_html=True)

    edu_col1, edu_col2 = st.columns(2)
    educations = [
        (
            "Berlin School of Business and Innovation",
            "MSc Data Analytics",
            "2023 – 2025",
            "Berlin, Germany",
            "Machine Learning · Data Engineering · Statistical Modelling · Production Deployment"
        ),
        (
            "Sharda University",
            "BBA + MBA — Business Analytics & Marketing (Integrated)",
            "2019 – 2023",
            "Greater Noida, India",
            "Marketing Strategy · Operations Research · Business Intelligence · Consumer Analytics"
        ),
    ]
    for col, (inst, degree, period, loc, focus) in zip([edu_col1, edu_col2], educations):
        with col:
            st.markdown(f"""
            <div class="card">
                <div style="font-family:'Space Mono',monospace; font-size:13px; color:#58a6ff;">{degree}</div>
                <div style="font-size:15px; color:#f0f6fc; font-weight:600; margin: 6px 0;">{inst}</div>
                <div style="font-size:12px; color:#8b949e; margin-bottom:10px;">{period} · {loc}</div>
                <div style="font-size:11px; color:#8b949e; border-top:1px solid #21262d; padding-top:8px; line-height:1.7;">
                    {focus}
                </div>
            </div>
            """, unsafe_allow_html=True)
