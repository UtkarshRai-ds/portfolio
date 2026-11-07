# Utkarsh Rai — Data Scientist Portfolio

> Live at **[utkarshrai-ds-portfolio.streamlit.app](https://utkarshrai-ds-portfolio.streamlit.app)**

A personal portfolio built with Streamlit, showcasing deployed end-to-end projects spanning forecasting, experimentation, predictive modelling, and computer vision.

Every project below is live, linked to its own repo, and documented with the reasoning behind the modelling decisions.

---

## Pages

| Page | Description |
|------|-------------|
| **About Me** | Bio, domain coverage, education — MSc Data Analytics + BBA/MBA |
| **Projects** | Four deployed projects + two academic publications |
| **Skills** | Category-based tech stack — ML, Data Engineering, Analytics, Business |
| **Resume** | Experience timeline, education, core competencies + downloadable PDF CV |
| **Contact** | Live contact form powered by Formspree |

---

## Projects Featured

### A/B Testing — From Power Analysis to Production
- Power analysis (baseline 10%, MDE 2%, α 0.05, power 0.80 → 3,835 users/group) and proportions z-test on real Kaggle e-commerce data
- Peeking demonstration: false positive rate climbs 5.1% → 14.7% across 5 interim checks
- 1,000-experiment Monte Carlo verification — empirical power 0.777 vs theoretical 0.800
- 🔗 [Live App](https://ab-testing-project0.streamlit.app/) · [GitHub](https://github.com/UtkarshRai-ds/ab-testing-project)

### German Electricity Demand Forecasting
- Day-ahead (24h) hourly load forecasting on SMARD.de + Open-Meteo data, 2020–2026
- Six models benchmarked — Seasonal-Naive, SARIMA, Prophet, LightGBM, XGBoost, CatBoost
- CatBoost at **2.83% MAPE**, beating the grid operator's own forecast (4.40% on the identical hold-out) by ~36%
- Self-conducted leakage audit: shifting rolling and temperature features by the forecast horizon moved MAPE from an inflated 2.24% to an honest 2.83%
- 🔗 [Live App](https://german-electricity-demand-forecasting.streamlit.app/) · [GitHub](https://github.com/UtkarshRai-ds/german-electricity-demand-forecasting)

### Telco Customer Churn Prediction
- IBM Telco dataset · 7,043 rows · 36 engineered features
- Logistic Regression tuned via Optuna (30 trials, 5-fold CV) — AUC 0.838, Recall 0.80 (31pp lift over baseline)
- Risk segmentation: targeting the top 51% risk tier captures 87% of churners
- Docker · GitHub Actions CI/CD · MLflow · 34 pytest tests
- 🔗 [Live App](https://telco-churn-utkarsh.streamlit.app) · [GitHub](https://github.com/UtkarshRai-ds/telco-churn-prediction)

### SkyWatch — Satellite Object Detection
- NWPU VHR-10 dataset · 800 images · 10 classes · 4,811 annotations
- YOLOv8n vs YOLOv8s dual benchmark under identical conditions — mAP50 0.697, Recall 0.690
- Per-class failure analysis surfaced in the dashboard rather than hidden
- Docker · GitHub Actions · Weights & Biases · 40 pytest tests
- 🔗 [Live App](https://huggingface.co/spaces/Utkarsh-DS/Skywatch-Detection) · [GitHub](https://github.com/UtkarshRai-ds/skywatch-detection)

---

## Publications

| Type | Title | Venue |
|------|-------|-------|
| Conference Paper · Nov 2022 | MetaVerse: The New Shape of Marketing | International Marketing Conference, IIM Shillong · ISBN 978-93-5701-583-7 |
| Book Chapter · Feb 2021 | PHARMEASY: A Fast Growing Healthtech Venture | Emerging Contours of Business and Management · ISBN 978-93-91842-41-3 |

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

Each page module exposes a single `render()` function; `app.py` handles sidebar routing and injects the shared CSS.

---

## Connect

- 💼 [LinkedIn](https://www.linkedin.com/in/utkarshrai-ds)
- 🐙 [GitHub](https://github.com/UtkarshRai-ds)
- 📧 <utkarsh26rai@gmail.com>
- 📍 Berlin, Germany — Open to DS, DA, BA & Consultant roles
