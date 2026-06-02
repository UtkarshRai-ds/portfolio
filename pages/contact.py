import streamlit as st
import requests


FORMSPREE_ENDPOINT = "https://formspree.io/f/xjgznoza"


def render():
    st.markdown('<div class="section-label">// get in touch</div>', unsafe_allow_html=True)
    st.markdown("# Contact")
    st.markdown(
        '<p style="font-size:15px;color:#8b949e;margin-top:-8px;margin-bottom:24px;">'
        "Open to data science roles, collaborations, and conversations about ML in Berlin.</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown('<div class="section-label">// send a message</div>', unsafe_allow_html=True)

        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Name", placeholder="Your name")
            email = st.text_input("Email", placeholder="your@email.com")
            subject = st.selectbox(
                "Subject",
                ["Job Opportunity", "Collaboration / Project", "General Enquiry", "Other"],
            )
            message = st.text_area("Message", placeholder="Tell me about the role or project...", height=150)

            submitted = st.form_submit_button("Send Message ↗")

            if submitted:
                if name and email and message:
                    try:
                        response = requests.post(
                            FORMSPREE_ENDPOINT,
                            data={
                                "name": name,
                                "email": email,
                                "subject": subject,
                                "message": message,
                            },
                            headers={"Accept": "application/json"},
                            timeout=10,
                        )
                        if response.status_code == 200:
                            st.success(
                                f"Message sent successfully! I'll get back to you at {email}.",
                                icon="✅",
                            )
                        else:
                            st.error(
                                "Something went wrong sending your message. Please email me directly at utkarsh26rai@gmail.com",
                                icon="⚠️",
                            )
                    except Exception:
                        st.error(
                            "Could not send message. Please email me directly at utkarsh26rai@gmail.com",
                            icon="⚠️",
                        )
                else:
                    st.error("Please fill in your name, email, and message.", icon="⚠️")

    with col2:
        st.markdown('<div class="section-label">// find me</div>', unsafe_allow_html=True)

        contacts = [
            ("📧", "Email", "utkarsh26rai@gmail.com", "mailto:utkarsh26rai@gmail.com"),
            ("💼", "LinkedIn", "linkedin.com/in/utkarshrai-ds", "https://www.linkedin.com/in/utkarshrai-ds"),
            ("🐙", "GitHub", "github.com/UtkarshRai-ds", "https://github.com/UtkarshRai-ds"),
            ("📍", "Location", "Berlin, Germany", None),
        ]

        for icon, label, value, url in contacts:
            link_html = (
                f'<a href="{url}" target="_blank" style="color:#58a6ff;text-decoration:none;">{value}</a>'
                if url else f'<span style="color:#c9d1d9;">{value}</span>'
            )
            st.markdown(
                f'<div class="card" style="margin-bottom:10px;padding:14px 18px;">'
                f'<div style="display:flex;align-items:center;gap:12px;">'
                f'<span style="font-size:20px;">{icon}</span>'
                f'<div>'
                f'<div style="font-size:11px;color:#8b949e;text-transform:uppercase;'
                f'letter-spacing:1px;font-family:\'Space Mono\',monospace;">{label}</div>'
                f'<div style="font-size:14px;margin-top:2px;">{link_html}</div>'
                f'</div>'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

        st.markdown('<div class="section-label" style="margin-top:20px;">// availability</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="card">'
            '<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;">'
            '<span style="width:10px;height:10px;background:#3fb950;border-radius:50%;display:inline-block;"></span>'
            '<span style="font-family:\'Space Mono\',monospace;font-size:13px;color:#3fb950;">Available Now</span>'
            '</div>'
            '<div style="font-size:13px;color:#8b949e;line-height:1.7;">'
            'Holding a Job Seeker Visa in Germany. Open to full-time positions, starting immediately. '
            'Prefer Berlin-based or remote roles within Germany.'
            '</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align:center;padding:20px 0;">'
        '<div style="font-family:\'Space Mono\',monospace;font-size:20px;color:#58a6ff;margin-bottom:8px;">'
        "Let's build something meaningful with data."
        '</div>'
        '<div style="font-size:13px;color:#8b949e;">'
        'Berlin · Open to opportunities · utkarsh26rai@gmail.com'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )
