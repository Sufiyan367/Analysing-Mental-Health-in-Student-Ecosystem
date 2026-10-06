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
| **Dashboard** | Responsive and Design of Dashboard | **COMPLETED (Prototypes & Spec)** | [`docs/dashboard_design.md`](docs/dashboard_design.md), [`evidence/dashboard/`](evidence/dashboard/) |
| **Story** | No of Scenes of Story | **COMPLETED (5 Scenes)** | [`docs/story.md`](docs/story.md), [`evidence/story/`](evidence/story/) |
| **Performance Testing** | Performance & Audit Testing | **COMPLETED (4 Subtasks)** | [`docs/performance_testing.md`](docs/performance_testing.md), [`evidence/performance/`](evidence/performance/) |
| **Web Integration** | Web Integration of Dashboard and Story | **COMPLETED (Flask Portal & Embedding)** | [`docs/web_integration.md`](docs/web_integration.md), [`evidence/web_integration/`](evidence/web_integration/) |
| **Demonstration & Docs** | Final Report & Demonstration | **NEXT PLANNED STAGE** | Project demonstration slide deck & documentation |

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

## 📖 Guided 5-Scene Data Story: Analysing Mental Health in Student Ecosystem

The 5-scene data story guides institutional leaders from macro-level baseline diagnostics through lifestyle risks, vulnerability factors, and clinical treatment progress:

| Scene | Scene Title | Core Question & Focus | Visual Artifact |
| :---: | :--- | :--- | :--- |
| **1** | **Student Mental Health Baseline** | Establish cohort population stress spread and KPI baseline. | [`01_baseline.png`](evidence/story/01_baseline.png) |
| **2** | **Stress & Psychological Symptoms** | Quantify symptom escalation (Anxiety & Depression) by stress tier. | [`02_psychological_symptoms.png`](evidence/story/02_psychological_symptoms.png) |
| **3** | **Lifestyle Factors and Stress** | Examine sleep deficits (71.4% poor sleep) and screen immersion (8.12 hrs). | [`03_lifestyle_and_stress.png`](evidence/story/03_lifestyle_and_stress.png) |
| **4** | **Vulnerability & Support Systems** | Assess pre-existing history (40%) vs campus first-onset distress. | [`04_vulnerability_and_support.png`](evidence/story/04_vulnerability_and_support.png) |
| **5** | **Intervention & Recovery Progress** | Evaluate therapy modalities (CBT top at 40.8 score) & campus policy. | [`05_intervention_and_progress.png`](evidence/story/05_intervention_and_progress.png) |

Detailed narrative transitions and policy recommendations are documented in [`docs/story.md`](docs/story.md).

---

## 🖥️ Student Mental Health Analysis Dashboard

The **Student Mental Health Analysis Dashboard** unifies the project's empirical findings into an interactive, multi-device diagnostic tool for campus administrators and counselors.

### Verified Cohort KPIs
- **Total Students:** `200` (Full cohort sample)
- **Average Anxiety Score:** `52.59` (Normalized psychometric score 0–100)
- **Average Depression Score:** `48.09` (Normalized psychometric score 0–100)
- **Average Daily Screen Time:** `7.10 hrs/day` (Continuous measurement)

### Core Visualizations Incorporated
1. **Stress Level Distribution** (Bar Chart)
2. **Stress vs. Anxiety & Depression Scores** (Grouped Bar Chart)
3. **Sleep Quality vs. Stress Tier** (Stacked Bar Chart)
4. **Daily Screen Time by Stress Level** (Bar Chart)
5. **Mental Health History Prevalence** (Donut Chart)
6. **Ranked Therapy Efficacy** (Horizontal Bar Chart)

### Responsive Dashboard Variants
- **Desktop (1920 $\times$ 1080 / 16:9):** [`evidence/dashboard/student_mental_health_dashboard.png`](evidence/dashboard/student_mental_health_dashboard.png)
- **Tablet (1024 $\times$ 768 / 2-Column):** [`evidence/dashboard/tablet_dashboard.png`](evidence/dashboard/tablet_dashboard.png)
- **Mobile (Vertical Stack):** [`evidence/dashboard/mobile_dashboard.png`](evidence/dashboard/mobile_dashboard.png)
- **Full Architecture & Layout Specification:** [`docs/dashboard_design.md`](docs/dashboard_design.md)

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
│   ├── dashboard_design.md                      # Responsive dashboard architecture & layout specification
│   ├── story.md                                 # 5-Scene guided data story & policy narrative
│   ├── performance_testing.md                   # Overall performance testing & architectural audit
│   ├── performance_data_rendering.md            # Task 1: Data rendering volume & parsing benchmark
│   ├── performance/
│   │   ├── filter_utilization.md                # Task 2: Filter utilization & subsetting benchmark
│   │   ├── calculation_fields.md                # Task 3: Calculation fields inventory & formulas
│   │   └── visualization_inventory.md           # Task 4: Official project visualization audit
│   ├── web_integration.md                       # Flask web portal architecture & Tableau embedding
│   ├── problem_statement.md                      # Capstone problem background & target outcomes
│   └── tableau.md                                # Tableau authoring architectural reference
│
├── evidence/
│   ├── visualizations/                          # 8 Verified visualization artifacts (PNG)
│   ├── dashboard/                               # Responsive dashboard prototypes (Desktop, Tablet, Mobile)
│   ├── story/                                   # 5 Verified story scene artifacts (PNG)
│   ├── performance/                             # Performance testing benchmarks & evidence
│   │   ├── data_rendering/                      # Task 1 charts & JSON metrics
│   │   ├── filters/                             # Task 2 filter benchmark charts & JSON metrics
│   │   └── calculations/                        # Task 3 calculation fields specs & diagram
│   └── web_integration/                         # Full-page web route validation screenshots
│       ├── home_page.png
│       ├── dashboard_page.png
│       ├── story_page.png
│       └── about_page.png
│
├── scripts/
│   ├── generate_student_mental_health_dataset.py # Standardized realistic dataset generator
│   ├── validate_dataset.py                       # Automated 18-variable schema audit script
│   ├── generate_visualizations.py                # Reproducible generator for 8 chart artifacts
│   ├── generate_dashboard_prototypes.py         # Multi-device responsive dashboard generator
│   ├── generate_story_scenes.py                 # 5-Scene story narrative generator
│   ├── benchmark_data_rendering.py              # Task 1 rendering volume benchmark
│   ├── benchmark_filter_utilization.py          # Task 2 filter latency benchmark
│   ├── generate_calculation_fields_spec.py       # Task 3 calculated field specification generator
│   └── capture_web_screenshots.py               # Playwright automated web validation script
│
├── tableau/                                      # Tableau workbooks and assets
├── templates/                                    # Flask web application Jinja2 templates
└── static/                                       # Web CSS and JavaScript assets
```

---

## 🌐 Flask Web Application & Tableau Embedding

A fully functional Flask web application hosts the project diagnostics and provides responsive cloud embedding:

- **Launch Command:** `python app.py` (Default port: `5000`)
- **Web Routes:**
  - `/` — **Executive Overview:** 4 cohort KPIs, subgroup badges, and 4 empirical diagnostic findings.
  - `/dashboard` — **Interactive Dashboards:** Multi-device layout selector (Desktop, Tablet, Mobile) and live Tableau embed container (`TABLEAU_DASHBOARD_URL`).
  - `/story` — **Guided Data Story:** 5-scene narrative browser with interactive step navigation and live Tableau embed container (`TABLEAU_STORY_URL`).
  - `/about` — **Methodology & Architecture:** 18-variable schema dictionary, 10 calculation formulas, and validation report.
- **Visual Validation Evidence:** Full-page verified screenshots under [`evidence/web_integration/`](evidence/web_integration/).

---

## 🎯 Next Planned Stage
**Epic: Demonstration & Final Documentation:**  
- Compile comprehensive project demonstration slides and capstone portfolio.
- Deliver project executive summary and technical walkthrough documentation.

