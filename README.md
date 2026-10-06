# Analysing Mental Health in Student Ecosystem

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tableau Public](https://img.shields.io/badge/Tableau_Public-Prepared_For_Authoring-blue?logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/sufiyansurve333)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Data Analytics with Tableau — Virtual Internship Capstone Project**  
> *Platform: SkillWallet / SmartBridge*  
> *Author Profile:* [Tableau Public Profile](https://public.tableau.com/app/profile/sufiyansurve333)

---

## 📌 Executive Summary
The **Analysing Mental Health in Student Ecosystem** project delivers an end-to-end analytical framework and visual diagnostics platform to explore, measure, and understand the psychological stressors impacting university students.

By synthesizing **data engineering**, **validated psychometric metrics**, and **Tableau visual storytelling**, this project provides institutional decision-makers, counseling services, and academic mentors with empirical diagnostics to move campus mental health support from reactive intervention to proactive, data-driven wellness care.

---

## 📍 SkillWallet Project Progress & Lifecycle Stages

| SkillWallet Epic / Section | Task / Milestone | Current Status | Artifacts / Evidence |
| :--- | :--- | :---: | :--- |
| **Data Collection & Extraction** | Downloading the dataset | **COMPLETED** | [`data/raw/mental_health_student_ecosystem.csv`](data/raw/mental_health_student_ecosystem.csv) |
| **Data Collection & Extraction** | Understand the data | **COMPLETED** | [`docs/data_dictionary.md`](docs/data_dictionary.md), [`docs/dataset_validation.md`](docs/dataset_validation.md) |
| **Data Preparation** | Prepare the Data for Visualization | **COMPLETED** | [`docs/data_preparation.md`](docs/data_preparation.md), [`data/cleaned/validation_summary.json`](data/cleaned/validation_summary.json) |
| **Data Visualization** | No of Unique Visualizations | **COMPLETED (8 Artifacts)** | [`docs/data_visualization.md`](docs/data_visualization.md), [`evidence/visualizations/`](evidence/visualizations/) |
| **Data Visualization** | Connect Data with Tableau & Author Worksheets | **NEXT PLANNED STAGE** | To be authored on Tableau Public Web Authoring |
| **Dashboard** | Build Interactive Dashboards | Pending | Dashboard 1 & Dashboard 2 |
| **Story** | Build Guided Story Points | Pending | 5-Scene Story Narrative |
| **Performance Testing** | Performance & Audit Testing | Pending | Latency, filter optimization & responsiveness |
| **Web Integration** | Flask Web Portal Integration | Pending | Embedded Tableau Public visualizations in Flask |
| **Demonstration & Docs** | Final Report & Demonstration | Pending | Video demonstration, slide deck & documentation |

---

## 📊 Dataset Overview & Preparation Status

- **Location:** [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](data/cleaned/mental_health_student_ecosystem_cleaned.csv)
- **Raw Backup:** [`data/raw/mental_health_student_ecosystem.csv`](data/raw/mental_health_student_ecosystem.csv)
- **Dimensions:** **200 Rows $\times$ 18 Columns**
- **Missing Values:** **0** (100% complete across all 18 variables)
- **Duplicate User IDs:** **0** (Unique identifiers: `STU_0001` to `STU_0200`)
- **Data Preparation Status:** **READY FOR VISUALIZATION**
- **Cleaning Note:** *No further data cleaning was required; the dataset is visualization-ready.*

---

## 📈 8 Unique Dataset-Grounded Visualizations

All 8 visualizations are generated strictly from the validated 18-column dataset without fabricating missing features:

| # | Visualization Title | Chart Type | Data Dimensions & Measures | Visual Evidence |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Stress Level Distribution** | Bar Chart | Dimension: `Stress Level`, Measure: `Count of User ID` | [View Image](evidence/visualizations/01_stress_level_distribution.png) |
| **2** | **Stress Level vs Anxiety Score** | Bar Chart | Dimension: `Stress Level`, Measure: `AVG(Anxiety Score)` | [View Image](evidence/visualizations/02_stress_vs_anxiety.png) |
| **3** | **Stress Level vs Depression Score** | Bar Chart | Dimension: `Stress Level`, Measure: `AVG(Depression Score)` | [View Image](evidence/visualizations/03_stress_vs_depression.png) |
| **4** | **Gender Mental Health Comparison** | Grouped Bar | Dimension: `Gender`, Measures: `AVG(Anxiety Score)`, `AVG(Depression Score)` | [View Image](evidence/visualizations/04_gender_mental_health_comparison.png) |
| **5** | **Sleep Quality vs Stress Level** | Stacked Bar | Dimensions: `Sleep Quality`, `Stress Level`, Measure: `Count of User ID` | [View Image](evidence/visualizations/05_sleep_quality_vs_stress.png) |
| **6** | **Screen Time vs Stress Level** | Bar Chart | Dimension: `Stress Level`, Measure: `AVG(Daily Screen Time (hrs))` | [View Image](evidence/visualizations/06_screen_time_vs_stress.png) |
| **7** | **Mental Health History Distribution**| Donut Chart | Dimension: `Mental Health History`, Measure: `Count of User ID` | [View Image](evidence/visualizations/07_mental_health_history_distribution.png) |
| **8** | **Therapy Type vs Progress Score** | Ranked Bar | Dimension: `Therapy Type`, Measure: `AVG(Progress Score)` | [View Image](evidence/visualizations/08_therapy_type_vs_progress.png) |

Detailed interpretations and formulas are available in [`docs/data_visualization.md`](docs/data_visualization.md).

---

## 🏛️ Project Directory Structure

```
Analysing-Mental-Health-in-Student-Ecosystem/
├── README.md                                    # Main project documentation & status tracker
├── requirements.txt                              # Python environment dependencies
│
├── data/
│   ├── raw/
│   │   └── mental_health_student_ecosystem.csv  # 200-row 18-column primary validated raw data
│   └── cleaned/
│       ├── mental_health_student_ecosystem_cleaned.csv # Verified visualization-ready dataset
│       └── validation_summary.json              # Machine-readable schema & integrity audit
│
├── docs/
│   ├── data_dictionary.md                        # Psychometric descriptions & data definitions
│   ├── dataset_validation.md                     # Statistical distributions & integrity audit
│   ├── data_preparation.md                      # Preparation report & visualization mapping
│   ├── data_visualization.md                    # Specifications for 8 dataset-grounded visualizations
│   ├── problem_statement.md                      # Capstone problem background & target outcomes
│   └── tableau.md                                # Tableau authoring architectural reference
│
├── evidence/
│   └── visualizations/                          # 8 Verified visualization artifacts (PNG)
│       ├── 01_stress_level_distribution.png
│       ├── 02_stress_vs_anxiety.png
│       ├── 03_stress_vs_depression.png
│       ├── 04_gender_mental_health_comparison.png
│       ├── 05_sleep_quality_vs_stress.png
│       ├── 06_screen_time_vs_stress.png
│       ├── 07_mental_health_history_distribution.png
│       └── 08_therapy_type_vs_progress.png
│
├── scripts/
│   ├── generate_student_mental_health_dataset.py # Standardized realistic dataset generator
│   ├── validate_dataset.py                       # Automated 18-variable schema audit script
│   └── generate_visualizations.py                # Reproducible generator for 8 chart artifacts
│
├── tableau/                                      # Tableau workbooks and assets
├── templates/                                    # Flask web application Jinja2 templates
└── static/                                       # Web CSS and JavaScript assets
```

---

## 🎯 Next Planned Stage
**Tableau Authoring & Dashboard Construction:**  
- Connect `data/cleaned/mental_health_student_ecosystem_cleaned.csv` via Tableau Public Web Authoring.
- Author interactive native sheets, calculated fields, and dashboards in the authenticated environment.
