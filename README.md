# Analysing Mental Health in Student Ecosystem

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Tableau Public](https://img.shields.io/badge/Tableau_Public-Profile_Prepared-blue?logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/sufiyansurve333)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Data Analytics with Tableau — Virtual Internship Capstone Project**  
> *Platform: SkillWallet / SmartBridge*  
> *Student Author:* Sufiyan Surve  
> *Tableau Public Profile:* [`sufiyansurve333`](https://public.tableau.com/app/profile/sufiyansurve333)  
> *Repository:* [`Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem`](https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem)

---

## 1. Project Title & Overview

**Analysing Mental Health in Student Ecosystem: A Multidimensional Visual Analytics and Clinical Diagnostic Platform**

Higher education institutions face escalating rates of psychological distress, academic burnout, and emotional fatigue among undergraduate and postgraduate students. Historically, campus mental health support operates under a **reactive paradigm**—counseling centers discover student crises only after academic failure, disciplinary action, or acute psychological breakdown.

This capstone project delivers an end-to-end analytical solution connecting self-reported stress tiers with standardized psychometric measures (Anxiety and Depression) and behavioral lifestyle habits (sleep quality, daily screen immersion, physical activity). The platform equips university leadership and counseling departments with empirical diagnostics to move student mental health support from reactive crisis management to proactive, data-informed intervention.

---

## 2. Project Objectives

1. **Establish Cohort Baselines:** Empirically quantify baseline stress distributions across a standardized 200-student university cohort.
2. **Evaluate Symptom Coupling:** Measure how subjective stress escalates into clinical anxiety (52.59 cohort mean) and depression (48.09 cohort mean) burdens.
3. **Isolate Behavioral Stress Drivers:** Examine the compounding lifestyle triad of sleep deprivation (71.4% poor sleep in high stress), screen immersion (8.12 hrs/day in high stress), and physical inactivity.
4. **Identify Institutional Care Gaps:** Contrast pre-existing mental health history against campus first-onset distress, and quantify the treatment reach deficit (53.5% receiving no therapy).
5. **Evaluate Therapy Modalities:** Empirically rank therapeutic interventions by clinical progress scores (CBT top at 40.80 progress score).
6. **Deploy Full-Stack Web Portal:** Deliver an interactive Python Flask portal featuring responsive multi-device dashboards, a 5-scene guided data story, and `<tableau-viz>` cloud embedding.

---

## 3. Dataset Overview & Ground Truth

All project analyses, calculations, visual charts, and dashboard metrics are grounded exclusively in the validated primary dataset:

- **Source File:** [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](data/cleaned/mental_health_student_ecosystem_cleaned.csv) ($19.84\text{ KB}$)
- **Raw Baseline:** [`data/raw/mental_health_student_ecosystem.csv`](data/raw/mental_health_student_ecosystem.csv)
- **Machine-Readable Validation:** [`data/cleaned/validation_summary.json`](data/cleaned/validation_summary.json)
- **Cohort Dimensions:** **200 Rows $\times$ 18 Standardized Columns**
- **Missing / Null Values:** **0 cells (0.00%)**
- **Duplicate Records:** **0 duplicates** (Unique IDs: `STU_0001` to `STU_0200`)
- **Integrity Notice:** *No further data cleaning was required; the dataset is 100% visualization-ready. Generic SkillWallet demo fields referencing non-existent variables (e.g., Study Hours, Heart Rate Variability) were explicitly rejected.*

### Standardized 18-Variable Schema

| # | Attribute Name | Data Type | Permissible Range / Values | Analytical Purpose |
| :-: | :--- | :---: | :---: | :--- |
| **1** | `User ID` | String | `STU_0001` – `STU_0200` | Unique primary key identifier |
| **2** | `Age` | Integer | 18 – 27 years | Demographic maturity segmentation |
| **3** | `Gender` | String | Female, Male, Other | Gender disparity analysis |
| **4** | `Occupation` | String | Undergraduate, Postgrad, Intern, TA, Researcher | Academic workload role |
| **5** | `Stress Level` | String | Low (44), Medium (107), High (49) | Core perceived stress classification |
| **6** | `Anxiety Score` | Integer | 0 – 100 (Mean: 52.59) | Standardized anxiety severity scale |
| **7** | `Depression Score` | Integer | 0 – 100 (Mean: 48.09) | Standardized depression severity scale |
| **8** | `Sleep Quality` | String | Poor (66), Average (89), Good (45) | Physiological restfulness indicator |
| **9** | `Daily Screen Time (hrs)` | Float | 3.0 – 12.0 (Mean: 7.10 hrs) | Digital immersion exposure metric |
| **10** | `Physical Activity Level` | String | Low (86), Moderate (80), High (34) | Weekly physical exercise tier |
| **11** | `Social Interaction Score` | Integer | 1 – 10 (Mean: 5.55) | Interpersonal social connection index |
| **12** | `Mental Health History` | String | No (120), Yes (80) | Pre-existing clinical psychological diagnosis |
| **13** | `Therapy Type` | String | No Therapy (107), Counseling (35), Meditation (28), CBT (20), Support Group (10) | Active intervention modality |
| **14** | `Intervention Duration (weeks)` | Integer | 0 – 16 weeks (Active mean: 6.67) | Cumulative treatment duration |
| **15** | `Progress Score` | Integer | 0 – 100 (Active mean: 35.10) | Post-intervention recovery metric |
| **16** | `Medication Usage` | String | No (182), Yes (18) | Psychiatric pharmacotherapy usage |
| **17** | `Support System Strength` | String | Low (52), Medium (103), High (45) | Perceived social/familial network safety net |
| **18** | `Work-Life Balance Score` | Integer | 1 – 10 (Mean: 5.47) | Academic lifestyle equilibrium |

---

## 4. Technology Stack & Architecture

- **Data Processing & Validation:** Python 3.11, Pandas, NumPy, JSON Schema Validation
- **Visual Analytics & Prototyping:** Matplotlib (GridSpec), Seaborn, PIL
- **Business Intelligence & Storytelling:** Tableau Public Embedding API v3 (`<tableau-viz>`)
- **Web Application:** Python Flask 3.0.3, Jinja2, HTML5 / CSS3 (CSS Grid, Flexbox), Vanilla JavaScript
- **End-to-End Media & Audio:** `pyttsx3` (TTS Audio Engine), FFmpeg (H.264 / AAC Encoding, 1080p 25fps)
- **Documentation & Publishing:** Markdown, Playwright (A4 PDF compilation), Git, GitHub

---

## 5. SkillWallet Virtual Internship Lifecycle Status

| Epic # | Stage / Milestone | Operational Status | Verified Artifacts / Evidence |
| :---: | :--- | :---: | :--- |
| **1** | **Data Collection & Extraction** | **COMPLETED** | [`data/raw/mental_health_student_ecosystem.csv`](data/raw/mental_health_student_ecosystem.csv), [`docs/data_dictionary.md`](docs/data_dictionary.md), [`docs/dataset_validation.md`](docs/dataset_validation.md) |
| **2** | **Data Preparation** | **COMPLETED** | [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](data/cleaned/mental_health_student_ecosystem_cleaned.csv), [`docs/data_preparation.md`](docs/data_preparation.md), [`data/cleaned/validation_summary.json`](data/cleaned/validation_summary.json) |
| **3** | **Data Visualization** | **COMPLETED** | 8 Dataset-Grounded Visualizations ([`evidence/visualizations/`](evidence/visualizations/)), [`docs/data_visualization.md`](docs/data_visualization.md) |
| **4** | **Dashboard** | **COMPLETED — Prototypes & Spec** | Multi-Device Responsive Layouts ([`evidence/dashboard/`](evidence/dashboard/)), [`docs/dashboard_design.md`](docs/dashboard_design.md) |
| **5** | **Story** | **COMPLETED — Prototypes & Spec** | 5-Scene Guided Data Story ([`evidence/story/`](evidence/story/)), [`docs/story.md`](docs/story.md) |
| **6** | **Performance Testing** | **COMPLETED** | Ingestion & Filter Benchmarks, 10 Calculation Specs ([`evidence/performance/`](evidence/performance/)), [`docs/performance_testing.md`](docs/performance_testing.md) |
| **7** | **Web Integration** | **COMPLETED** | Python Flask Portal (`app.py`), `<tableau-viz>` Integration, Route Evidence ([`evidence/web_integration/`](evidence/web_integration/)), [`docs/web_integration.md`](docs/web_integration.md) |
| **8** | **Project Demonstration & Docs** | **COMPLETED** | 6:26-Min Walkthrough Video ([`evidence/demo/project_explanation_video.mp4`](evidence/demo/project_explanation_video.mp4)), Script ([`docs/demo_video_script.md`](docs/demo_video_script.md)), PDF Report ([`evidence/documentation/Project_Documentation.pdf`](evidence/documentation/Project_Documentation.pdf)) |
| **—** | **Tableau Public Publication** | **PENDING MANUAL UPLOAD** | All 8 worksheets, 10 calculations, and layouts are specified; cloud publishing remains pending manual browser session authoring. |

---

## 6. Eight Dataset-Grounded Visualizations

All 8 visualizations are generated strictly from the validated 18-variable schema:

| # | Visualization Title | Chart Type | Dimensions & Measures | Visual Evidence |
| :-: | :--- | :---: | :--- | :--- |
| **1** | **Stress Level Distribution** | Vertical Bar | `Stress Level` vs `Count of User ID` | [`01_stress_level_distribution.png`](evidence/visualizations/01_stress_level_distribution.png) |
| **2** | **Stress Level vs Anxiety Score** | Vertical Bar | `Stress Level` vs `AVG(Anxiety Score)` | [`02_stress_vs_anxiety.png`](evidence/visualizations/02_stress_vs_anxiety.png) |
| **3** | **Stress Level vs Depression Score** | Vertical Bar | `Stress Level` vs `AVG(Depression Score)` | [`03_stress_vs_depression.png`](evidence/visualizations/03_stress_vs_depression.png) |
| **4** | **Gender Mental Health Comparison** | Grouped Bar | `Gender` vs `AVG(Anxiety)`, `AVG(Depression)` | [`04_gender_mental_health_comparison.png`](evidence/visualizations/04_gender_mental_health_comparison.png) |
| **5** | **Sleep Quality vs Stress Level** | Stacked Bar | `Sleep Quality` $\times$ `Stress Level` | [`05_sleep_quality_vs_stress.png`](evidence/visualizations/05_sleep_quality_vs_stress.png) |
| **6** | **Screen Time vs Stress Level** | Vertical Bar | `Stress Level` vs `AVG(Daily Screen Time)` | [`06_screen_time_vs_stress.png`](evidence/visualizations/06_screen_time_vs_stress.png) |
| **7** | **Mental Health History Prevalence** | Donut Chart | `Mental Health History` vs `Count of User ID` | [`07_mental_health_history_distribution.png`](evidence/visualizations/07_mental_health_history_distribution.png) |
| **8** | **Ranked Therapy Efficacy** | Horizontal Bar | `Therapy Type` vs `AVG(Progress Score)` | [`08_therapy_type_vs_progress.png`](evidence/visualizations/08_therapy_type_vs_progress.png) |

---

## 7. Multi-Device Responsive Dashboard

The **Student Mental Health Analysis Dashboard** integrates 4 cohort KPI summary cards and 6 visual diagnostic panels:

- **Cohort KPIs:** Total Students (`200`), Avg Anxiety (`52.59`), Avg Depression (`48.09`), Avg Screen Time (`7.10 hrs/day`).
- **Responsive Variants:**
  - **Desktop Layout (1920×1080 / 16:9):** [`evidence/dashboard/desktop_dashboard.png`](evidence/dashboard/desktop_dashboard.png)
  - **Tablet Layout (1024×768 / 2-Column):** [`evidence/dashboard/tablet_dashboard.png`](evidence/dashboard/tablet_dashboard.png)
  - **Mobile Layout (Single Column Stack):** [`evidence/dashboard/mobile_dashboard.png`](evidence/dashboard/mobile_dashboard.png)
- **Detailed Layout Specification:** [`docs/dashboard_design.md`](docs/dashboard_design.md)

---

## 8. Guided 5-Scene Data Story

A sequential narrative structured to guide university stakeholders through clinical discoveries:

| Scene | Title | Core Question & Key Finding | Visual Evidence |
| :---: | :--- | :--- | :--- |
| **1** | **Student Mental Health Baseline** | Cohort stress distribution: 78.0% in moderate or high stress tiers. | [`01_baseline.png`](evidence/story/01_baseline.png) |
| **2** | **Stress & Psychological Symptoms** | Symptom escalation: >135% surge in anxiety (72.06) & depression (68.78) for high stress. | [`02_psychological_symptoms.png`](evidence/story/02_psychological_symptoms.png) |
| **3** | **Lifestyle Factors and Stress** | Behavioral triad: 71.4% poor sleep & 8.12 hrs/day screen immersion in high stress. | [`03_lifestyle_and_stress.png`](evidence/story/03_lifestyle_and_stress.png) |
| **4** | **Vulnerability & Support Systems** | Acute first-onset distress: 60% have no prior history, yet 14 high-stress students emerged. | [`04_vulnerability_and_support.png`](evidence/story/04_vulnerability_and_support.png) |
| **5** | **Intervention & Recovery Progress** | Care gap & recovery: 53.5% receive No Therapy; CBT leads recovery with a 40.80 progress score. | [`05_intervention_and_progress.png`](evidence/story/05_intervention_and_progress.png) |

---

## 9. Performance Testing & Benchmarking Summary

Performance tests confirmed sub-millisecond data manipulation and high architectural headroom:

- **Data Rendering Volume:** Disk size $19.84\text{ KB}$, in-memory size $137.12\text{ KB}$, parse time $0.64\text{ ms}$, load latency $3.17\text{ ms}$.
- **Filter Evaluation Latency:** 8 single- and multi-predicate filters tested ($0.86 - 1.41\text{ ms}$ execution times).
- **Calculation Field Formulas:** 10 production calculations defined for Tableau.
- **Visual Evidence & Reports:** [`docs/performance_testing.md`](docs/performance_testing.md), [`evidence/performance/`](evidence/performance/).

---

## 10. Web Application & Dynamic Tableau Embedding

The Python Flask application (`app.py`) serves the complete web portal:

- **Launch Command:** `python app.py` (Default port: `5000`)
- **Key Routes:**
  - `/` — **Executive Overview:** High-level KPIs, subgroup badges, and 4 diagnostic pillars.
  - `/dashboard` — **Interactive Dashboards:** Responsive prototype layout switcher and live `<tableau-viz>` cloud container.
  - `/story` — **Guided Data Story:** 5-scene narrative browser with interactive navigation.
  - `/about` — **Methodology & Specifications:** Variable definitions, formulas, and architecture documentation.
  - `/evidence/<path>` — **Static Asset Delivery:** Serves verified PNG/MP4 evidence files.
- **Tableau Environment Variables:**
  - `TABLEAU_DASHBOARD_URL`: Configurable live dashboard embed URL (defaults to prototype fallback when empty).
  - `TABLEAU_STORY_URL`: Configurable live story embed URL (defaults to prototype fallback when empty).
  - `TABLEAU_PROFILE_URL`: Verified Tableau Public author profile [`sufiyansurve333`](https://public.tableau.com/app/profile/sufiyansurve333).
- **Route Validation Screenshots:** [`evidence/web_integration/`](evidence/web_integration/) (`home_page.png`, `dashboard_page.png`, `story_page.png`, `about_page.png`).

---

## 11. 🚀 Public Demo Deployment & Live Access

The Flask web application is configured for production deployment as a containerized Python web service:

- **Hosting Platform:** [Render](https://render.com) (Python 3.11 / Gunicorn WSGI)
- **Infrastructure Blueprint:** [`render.yaml`](render.yaml)
- **Production Build Command:** `pip install -r requirements.txt`
- **Production Start Command:** `gunicorn app:app`
- **Provisioning Status:** Infrastructure files (`render.yaml`, `requirements.txt`, WSGI `app:app`) are configured on `main`. Requires 1-click connection via [dashboard.render.com](https://dashboard.render.com) to assign the active HTTPS endpoint.
- **Deployment Documentation & Steps:** [`docs/public_deployment.md`](docs/public_deployment.md)
- **Tableau Public Status Note:** The deployed web application serves high-resolution interactive prototype layouts and metric cards. Native Tableau Public cloud workbook publishing remains pending manual GUI creation on profile [`sufiyansurve333`](https://public.tableau.com/app/profile/sufiyansurve333).

---

## 12. Demonstration Video & Publication Report

- **End-to-End Walkthrough Video (6:26 mins, 9.84 MB):** [`evidence/demo/project_explanation_video.mp4`](evidence/demo/project_explanation_video.mp4)  
  *Fully compliant with SkillWallet's 5–7 minute requirement (386.13 seconds). Features 1920×1080 16:9 slides, synchronized narration covering all 11 capstone sections, and verified AAC audio.*
- **Verbatim Narration Script:** [`docs/demo_video_script.md`](docs/demo_video_script.md)
- **19-Section Development Documentation:** [`docs/project_development_documentation.md`](docs/project_development_documentation.md)
- **Printable Publication PDF:** [`evidence/documentation/Project_Documentation.pdf`](evidence/documentation/Project_Documentation.pdf) ($175.4\text{ KB}$, 8 pages)

---

## 13. Repository Directory Structure

```
Analysing-Mental-Health-in-Student-Ecosystem/
├── README.md                                    # Main project documentation & status tracker
├── requirements.txt                              # Python environment dependencies
├── app.py                                        # Production Flask web application
│
├── data/
│   ├── raw/
│   │   ├── mental_health_student_ecosystem.csv  # 200-row 18-column primary validated raw data
│   │   └── student_mental_health_raw.csv        # Baseline reference survey extract
│   └── cleaned/
│       ├── mental_health_student_ecosystem_cleaned.csv # Verified visualization-ready dataset
│       ├── student_mental_health_cleaned.csv    # Legacy reference extract
│       └── validation_summary.json              # Machine-readable schema & integrity audit
│
├── docs/
│   ├── problem_statement.md                      # Capstone problem background & target outcomes
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
│   ├── demo_video_script.md                     # Verbatim 6:26 demonstration video script
│   └── project_development_documentation.md      # Comprehensive 19-section development lifecycle documentation
│
├── evidence/
│   ├── visualizations/                          # 8 Verified visualization artifacts (PNG)
│   ├── dashboard/                               # Responsive dashboard prototypes (Desktop, Tablet, Mobile)
│   ├── story/                                   # 5 Verified story scene artifacts (PNG)
│   ├── performance/                             # Performance testing benchmarks & evidence
│   │   ├── data_rendering/                      # Task 1 charts & JSON metrics
│   │   ├── filters/                             # Task 2 filter benchmark charts & JSON metrics
│   │   └── calculations/                        # Task 3 calculation fields specs & diagram
│   ├── web_integration/                         # Full-page web route validation screenshots
│   ├── demo/                                    # Full-length project explanation video (MP4, 6:26)
│   │   └── project_explanation_video.mp4        # Verified playable video with AAC narration
│   └── documentation/                           # Publication-grade printable report
│       └── Project_Documentation.pdf            # Full development lifecycle PDF document
│
├── scripts/
│   ├── generate_student_mental_health_dataset.py # Standardized realistic dataset generator
│   ├── validate_dataset.py                       # Automated 18-variable schema audit script
│   ├── data_cleaning.py                          # Data cleaning & hygiene pipeline script
│   ├── generate_visualizations.py                # Reproducible generator for 8 chart artifacts
│   ├── generate_dashboard_prototypes.py         # Multi-device responsive dashboard generator
│   ├── generate_story_scenes.py                 # 5-Scene story narrative generator
│   ├── benchmark_data_rendering.py              # Task 1 rendering volume benchmark
│   ├── benchmark_filter_utilization.py          # Task 2 filter latency benchmark
│   ├── generate_calculation_fields_spec.py       # Task 3 calculated field specification generator
│   ├── capture_web_screenshots.py               # Playwright automated web validation script
│   ├── generate_screenshots.py                  # Local component screenshot utility
│   ├── generate_demo_video.py                   # Calibrated 6:26 video compiler with voice narration
│   └── generate_documentation_pdf.py            # Playwright A4 printable PDF generator
│
├── tableau/
│   └── README.md                                # Tableau authoring blueprints & pending publication status
├── templates/                                    # Flask Jinja2 HTML templates
└── static/                                       # Responsive CSS & JavaScript assets
```

---

## 14. Tableau Public Authoring Status & Transparency Notice

> [!IMPORTANT]
> **Tableau Public Publication Status: PENDING MANUAL UPLOAD**
>
> All **8 worksheets**, **10 calculation fields**, **multi-device responsive dashboard layouts**, and **5-scene data story** are fully specified, verified, and prototyped in Python and Flask.
>
> To maintain strict academic integrity and avoid session corruption, synthetic XML workbook hacking was stopped. Cloud publishing remains pending manual creation and publishing via the authenticated Tableau Public Web Authoring GUI on the author's profile:  
> 🔗 **Tableau Public Profile:** [`https://public.tableau.com/app/profile/sufiyansurve333`](https://public.tableau.com/app/profile/sufiyansurve333)

Once published to Tableau Public:
1. Export the dashboard URL as `TABLEAU_DASHBOARD_URL`.
2. Export the story URL as `TABLEAU_STORY_URL`.
3. Restart `app.py` to seamlessly transition the portal from prototype frames to live Tableau Cloud embedding.

---

## 15. Key Empirical Findings & Strategic Recommendations

### Empirical Clinical Discoveries
1. **Pervasive Stress Burden:** 78.0% of the cohort (156 of 200) operates in moderate or severe stress tiers.
2. **Direct Symptom Escalation:** High stress drives a **>135% surge** in anxiety (72.06 vs 30.27) and depression (68.78 vs 26.80) relative to low stress.
3. **Lifestyle Risk Triad:** 71.4% of high-stress students suffer from poor sleep, accompanied by **8.12 hours/day** of screen immersion and 75.5% low physical activity.
4. **Acute Campus First-Onset Distress:** 60.0% of students have no prior mental health history, yet 14 high-stress cases emerged within this subgroup during university studies.
5. **Critical Institutional Care Gap:** **53.5% of students (107 of 200)** receive No Therapy, including 15 high-stress and 48 medium-stress students.
6. **Efficacy of Structured Therapy:** Cognitive Behavioral Therapy (CBT) achieves the highest recovery progress score (**40.80** over an average of 7.50 weeks).

### Strategic Campus Recommendations
1. **Scale CBT and Clinical Counseling:** Expand university counseling partnerships and clinical psychology internships to deliver structured cognitive behavioral interventions.
2. **Institutionalize Digital Wellness & Sleep Hygiene:** Embed digital wellness and sleep hygiene workshops into standard residence hall curricula and orientation modules.
3. **Proactive Freshman Mental Health Screening:** Implement opt-in, confidential mental health screenings during orientation to identify distressed students before academic probation.
4. **Expand Peer Support Networks:** Broaden peer-led support groups (recovery score 33.10) to reach un-enrolled students reluctant to access formal psychological clinics.
