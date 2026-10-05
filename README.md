# Analysing Mental Health in Student Ecosystem

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Tableau Public](https://img.shields.io/badge/Tableau_Public-Visualizations-E97627?logo=tableau&logoColor=white)](https://public.tableau.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Data Analytics with Tableau — Virtual Internship Project**  
> *Developed for SkillWallet / SmartBridge Platform*

---

## 📌 Executive Summary
The **Analysing Mental Health in Student Ecosystem** project provides a comprehensive, data-driven visual analytics platform designed to evaluate and understand the multifaceted psychological and academic stressors affecting university students. Leveraging **Tableau Public** for multidimensional visual storytelling and **Python Flask** for responsive web application delivery, this project equips institutional decision-makers with actionable diagnostics to proactively address student well-being.

---

## 🗂️ Project Repository Architecture
```
Analysing-Mental-Health-in-Student-Ecosystem/
├── README.md                      # Comprehensive project documentation
├── requirements.txt                # Python environment dependencies
├── .gitignore                      # Git exclusion rules
├── app.py                          # Flask WSGI application entrypoint
│
├── data/
│   ├── raw/                        # Original collected survey datasets
│   └── cleaned/                    # Cleaned, validated, and normalized data
│
├── scripts/
│   └── data_cleaning.py            # Reproducible data cleaning pipeline
│
├── tableau/
│   └── README.md                   # Tableau visualization & workbook documentation
│
├── templates/                      # Jinja2 HTML templates
│   ├── base.html                   # Master layout with navigation & responsive header
│   ├── index.html                  # Landing page with executive metrics
│   ├── dashboard.html              # Embedded interactive Tableau dashboards
│   ├── story.html                  # Embedded interactive Tableau data story
│   └── about.html                  # Methodology, team, and architecture overview
│
├── static/
│   ├── css/
│   │   └── style.css               # Modern typography & responsive layout styling
│   └── js/
│       └── main.js                 # Frontend interactions & embed controls
│
├── screenshots/                    # Verified visual evidence assets
│   ├── worksheets/                 # Individual Tableau worksheet exports
│   ├── dashboards/                 # Dashboard 1 & Dashboard 2 captures
│   ├── story/                      # Story points & sequential scenes
│   ├── flask/                      # Running Flask application UI captures
│   ├── github/                     # GitHub repository verification captures
│   └── skillwallet/                # SkillWallet submission & milestone evidence
│
└── docs/                           # Exhaustive technical documentation
    ├── problem_statement.md        # Problem definition & objectives
    ├── data_dictionary.md          # Variable taxonomy & data schema
    ├── preprocessing.md            # Data wrangling, imputation & audit report
    ├── tableau.md                  # Calculated fields, parameters & sheet details
    ├── findings.md                 # Analytical findings & institutional recommendations
    └── submission.md               # SkillWallet milestone submission log
```

---

## 🚀 Quick Start & Installation

### 1. Prerequisites
* Python 3.10+ installed
* Git installed and configured
* Modern web browser (Chrome, Edge, Brave, Firefox)

### 2. Clone the Repository
```bash
git clone https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem.git
cd Analysing-Mental-Health-in-Student-Ecosystem
```

### 3. Setup Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Flask Web Application
```bash
python app.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser.

---

## 📊 Live Deliverables & Interactive Links
* **GitHub Repository:** [https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem](https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem)
* **Tableau Public Workbook & Dashboards:** *[Pending Publication in Phase 2E/2I]*
* **Interactive Data Story:** *[Pending Publication in Phase 2E/2I]*
