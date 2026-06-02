# Utkarsh Rai — Data Scientist Portfolio

> Live at **[utkarshrai-ds-portfolio.streamlit.app](https://utkarshrai-ds-portfolio.streamlit.app)**

A production-grade personal portfolio built with Streamlit, showcasing end-to-end ML projects, business analytics experience, and academic publications. Dark GitHub-inspired design with a fully functional contact form.

---

## Pages

| Page | Description |
|------|-------------|
| **About Me** | Bio, domain expertise, education — MSc Data Analytics + BBA/MBA |
| **Projects** | Telco Churn Prediction · SkyWatch Satellite Detection · Publications |
| **Skills** | Category-based tech stack — ML, Data Engineering, Analytics, Business |
| **Resume** | Full experience timeline + downloadable PDF CV |
| **Contact** | Live contact form powered by Formspree |

---

## Projects Featured

### Telco Customer Churn Prediction
- IBM Telco dataset · 7,043 rows · 36 engineered features
- Tuned Logistic Regression via Optuna — AUC 0.838, Recall 0.80 (31pp lift)
- Docker · GitHub Actions CI/CD · MLflow · 34 pytest tests
- 🔗 [Live App](https://telco-churn-utkarsh.streamlit.app) · [GitHub](https://github.com/UtkarshRai-ds/telco-churn-prediction)

### SkyWatch — Satellite Object Detection
- NWPU VHR-10 dataset · 800 images · 10 classes · 4,811 annotations
- YOLOv8n vs YOLOv8s dual benchmark — mAP50 0.697, Recall 0.690
- Docker · GitHub Actions · Weights & Biases · 40 pytest tests
- 🔗 [Live App](https://huggingface.co/spaces/Utkarsh-DS/Skywatch-Detection)

---

## Tech Stack

```
Frontend      Streamlit · Custom CSS (GitHub dark theme)
Backend       Python 3.12 · Pillow · Requests
Deployment    Streamlit Community Cloud
Contact Form  Formspree
```

---

## Run Locally

```bash
git clone https://github.com/UtkarshRai-ds/portfolio.git
cd portfolio
pip install -r requirements.txt
streamlit run app.py
```

---

## Project Structure

```
portfolio/
├── app.py                  # Entry point — routing & global CSS
├── requirements.txt
├── runtime.txt             # python-3.12
├── .streamlit/
│   └── config.toml         # Hide default Streamlit sidebar nav
├── assets/
│   ├── photo.jpg           # Profile photo
│   └── Utkarsh_Rai_CV.pdf  # Downloadable CV
└── pages/
    ├── about.py            # About Me page
    ├── projects.py         # Projects + Publications
    ├── skills.py           # Skills + Certifications
    ├── resume.py           # Resume timeline
    └── contact.py          # Contact form (Formspree)
```

---

## Connect

- 💼 [LinkedIn](https://www.linkedin.com/in/utkarshrai-ds)
- 🐙 [GitHub](https://github.com/UtkarshRai-ds)
- 📧 utkarsh26rai@gmail.com
- 📍 Berlin, Germany — Open to DS, DA, BA & Consultant roles
