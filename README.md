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
| **Data Visualization** | Connect Data with Tableau & Create Worksheets | **NEXT PLANNED STAGE** | To be authored on Tableau Public Web Authoring |
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

### Data Schema (18 Variables)
1. **User ID** (`String`): Unique identifier (`STU_0001` - `STU_0200`)
2. **Age** (`Integer`): Age of the individual in years (18–27)
3. **Gender** (`String`): Female, Male, Other
4. **Occupation** (`String`): Undergraduate, Postgraduate, Doctoral Researcher, Student Intern, Teaching Assistant
5. **Stress Level** (`String`): Low, Medium, High
6. **Anxiety Score** (`Integer`): Standardized anxiety psychometric score (5–96)
7. **Depression Score** (`Integer`): Standardized depression severity score (9–87)
8. **Sleep Quality** (`String`): Poor, Average, Good
9. **Daily Screen Time (hrs)** (`Float`): Daily screen time in hours (3.0–12.0)
10. **Physical Activity Level** (`String`): Low, Moderate, High
11. **Social Interaction Score** (`Integer`): Interpersonal engagement scale (1–10)
12. **Mental Health History** (`String`): Yes, No
13. **Therapy Type** (`String`): CBT, Counseling, Meditation, Support Group, No Therapy
14. **Intervention Duration (weeks)** (`Integer`): Duration of intervention in weeks (0–16)
15. **Progress Score** (`Integer`): Improvement score post-intervention (0–69)
16. **Medication Usage** (`String`): Yes, No
17. **Support System Strength** (`String`): Low, Medium, High
18. **Work-Life Balance Score** (`Integer`): Self-rated balance score (1–10)

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
│   ├── problem_statement.md                      # Capstone problem background & target outcomes
│   └── tableau.md                                # Tableau authoring architectural reference
│
├── scripts/
│   ├── generate_student_mental_health_dataset.py # Standardized realistic dataset generator
│   └── validate_dataset.py                       # Automated 18-variable schema audit script
│
├── tableau/                                      # Tableau workbooks and assets
├── templates/                                    # Flask web application Jinja2 templates
└── static/                                       # Web CSS and JavaScript assets
```

---

## 🎯 Next Planned Stage
**Epic: Data Visualization**  
- Connect `data/cleaned/mental_health_student_ecosystem_cleaned.csv` via Tableau Public Web Authoring.
- Author the 9 validated analytical worksheets, calculated fields, and interactive chart views.
- Assemble Dashboard 1, Dashboard 2, and the 5-Scene Story Narrative.
