import streamlit as st


def render():
    st.markdown('<div class="section-label">// who am i</div>', unsafe_allow_html=True)
    st.markdown("# Utkarsh Rai")
    st.markdown(
        '<p style="font-size:20px; color:#8b949e; margin-top:-10px;">Data Scientist · Berlin, Germany 🇩🇪</p>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class="card">
        <p style="font-size:15px; color:#c9d1d9; line-height:1.8;">
        I'm a data scientist with an <span class="highlight-text">MSc in Data Analytics</span> (Berlin School of Business 
        and Innovation) and an <span class="highlight-text">MBA in Business Analytics & Marketing</span>. 
        I build end-to-end machine learning systems — from raw data pipelines to production-grade deployment.
        </p>
        <p style="font-size:15px; color:#c9d1d9; line-height:1.8; margin-top:12px;">
        Currently on a <span class="highlight-text">Job Seeker Visa</span> in Berlin, targeting Junior Data Scientist, 
        Data Analyst, Business Analyst, and Data Consultant roles. I care deeply about interpretable models, 
        business-aligned ML, and clean reproducible code.
        </p>
        <p style="font-size:15px; color:#c9d1d9; line-height:1.8; margin-top:12px;">
        Outside of data: learning German 🇩🇪 (A2 → B2 journey), exploring Vedic astrology, and building 
        in public on LinkedIn.
        </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-label" style="margin-top:24px;">// what i bring</div>', unsafe_allow_html=True)

        cols = st.columns(3)
        highlights = [
            ("🧠", "ML Engineering", "End-to-end pipelines with MLflow, Optuna, scikit-learn"),
            ("📊", "Business Analytics", "Power BI, DAX, translating data into decisions"),
            ("🚀", "Production Mindset", "Docker, GitHub Actions CI/CD, Streamlit deployment"),
        ]
        for c, (icon, title, desc) in zip(cols, highlights):
            with c:
                st.markdown(f"""
                <div class="card" style="text-align:center; min-height:140px;">
                    <div style="font-size:28px; margin-bottom:10px;">{icon}</div>
                    <div style="font-family:'Space Mono',monospace; font-size:13px; color:#f0f6fc; margin-bottom:8px;">{title}</div>
                    <div style="font-size:12px; color:#8b949e; line-height:1.6;">{desc}</div>
                </div>
                """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-label">// quick stats</div>', unsafe_allow_html=True)
        stats = [
            ("2", "Years Experience"),
            ("5+", "Projects Shipped"),
            ("2", "Research Publications"),
            ("AWS", "Cloud Certified"),
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
            <div style="font-size:13px; color:#c9d1d9; line-height:1.8;">
                <div style="margin-bottom:8px;">🔍 Open to full-time DS roles in Germany</div>
                <div style="margin-bottom:8px;">🇩🇪 Learning German (A2 level)</div>
                <div style="margin-bottom:8px;">🏗️ Building ML portfolio projects</div>
                <div>📝 Writing about DS on LinkedIn</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">// education</div>', unsafe_allow_html=True)

    edu_col1, edu_col2 = st.columns(2)
    educations = [
        ("Berlin School of Business and Innovation", "MSc Data Analytics", "2023 – 2024", "Berlin, Germany"),
        ("Sharda University, Greater Noida", "MBA — Business Analytics & Marketing (Dual)", "2021 – 2023", "India"),
    ]
    for col, (inst, degree, period, loc) in zip([edu_col1, edu_col2], educations):
        with col:
            st.markdown(f"""
            <div class="card">
                <div style="font-family:'Space Mono',monospace; font-size:13px; color:#58a6ff;">{degree}</div>
                <div style="font-size:15px; color:#f0f6fc; font-weight:600; margin: 6px 0;">{inst}</div>
                <div style="font-size:12px; color:#8b949e;">{period} · {loc}</div>
            </div>
            """, unsafe_allow_html=True)
