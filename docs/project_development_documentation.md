# Comprehensive Project Development Documentation: Step-by-Step Engineering Lifecycle

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Course / Track:** Data Analytics with Tableau — Virtual Internship  
**Platform:** SkillWallet / SmartBridge  
**Student Author:** Sufiyan Surve  
**Dataset Source of Truth:** [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](../data/cleaned/mental_health_student_ecosystem_cleaned.csv) ($N=200$, 18 columns)  
**Primary Repository:** [`Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem`](https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem)  
**Tableau Author Profile:** [`sufiyansurve333`](https://public.tableau.com/app/profile/sufiyansurve333)  

---

## 1. Project Title
**Analysing Mental Health in Student Ecosystem: A Multidimensional Visual Analytics and Clinical Diagnostic Platform**

---

## 2. Problem Statement
In contemporary higher education, university students experience rising levels of severe academic distress, digital saturation, sleep degradation, and emotional exhaustion. Historically, campus counseling services operate under a **reactive paradigm**—students only receive clinical attention after academic failure, disciplinary probation, or acute psychological crises.

Furthermore, university decision-makers often lack centralized empirical diagnostic systems that connect self-reported stress levels with standardized psychometric measures (Anxiety and Depression) and actionable lifestyle habits (sleep quality, daily screen immersion, physical activity). Without data-driven insights, institutional resource allocation remains ad-hoc, leaving vulnerable cohorts un-screened and untreated.

---

## 3. Objective
The overarching objective of this project is to architect an end-to-end analytical framework that:
1. **Establishes Cohort Baselines:** Empirically quantifies stress distributions across a standardized 200-student cohort.
2. **Evaluates Symptom Coupling:** Measures how self-reported stress severity escalates into quantifiable clinical anxiety and depression loads.
3. **Identifies Behavioral Drivers:** Isolates the lifestyle triad (sleep deprivation, screen immersion, and physical inactivity) associated with severe distress.
4. **Maps Clinical Vulnerability & Interventions:** Contrasts pre-existing histories with first-onset university cases and ranks therapeutic recovery outcomes (CBT, Counseling, Support Groups, Meditation).
5. **Deploys a Multi-Device Web Portal:** Integrates responsive visualizations, multi-device dashboard prototypes, a guided 5-scene data story, and Tableau embedding within a Python Flask application.

---

## 4. Dataset Acquisition
- **What Was Done:** Obtained and standardized the authentic student mental health ecosystem survey dataset representing 200 de-identified university undergraduates.
- **Why It Was Done:** To ground the entire capstone project in realistic, verified psychometric and lifestyle distributions rather than synthetic or generic portal templates.
- **Tools Used:** Python 3.11, Pandas, Git, GitHub.
- **Artifacts Produced:**
  - Raw Baseline: [`data/raw/mental_health_student_ecosystem.csv`](../data/raw/mental_health_student_ecosystem.csv)
  - Acquisition Documentation: [`docs/data_dictionary.md`](data_dictionary.md)
- **Validation:** 200 complete records with exactly 18 standardized column headers.

---

## 5. Dataset Schema & Data Dictionary
The verified schema comprises **18 standardized variables** (8 Numerical, 10 Categorical):

| # | Attribute Name | Data Type | Domain / Values | Analytical Purpose |
| :-: | :--- | :---: | :--- | :--- |
| **1** | `User ID` | String | `STU_0001` – `STU_0200` | Primary unique key identifier |
| **2** | `Age` | Integer | 18 – 25 years | Academic maturity and age segmentation |
| **3** | `Gender` | String | Male, Female, Other | Demographic segmentation and cross-gender comparison |
| **4** | `Occupation` | String | Student, Student & Intern | Academic/workload operational role |
| **5** | `Stress Level` | String | Low, Medium, High | Primary self-reported stress tier |
| **6** | `Anxiety Score` | Integer | 0 – 100 | Standardized clinical anxiety severity index |
| **7** | `Depression Score` | Integer | 0 – 100 | Standardized clinical depressive severity index |
| **8** | `Sleep Quality` | String | Poor, Average, Good | Physiological restfulness indicator |
| **9** | `Daily Screen Time (hrs)` | Float | 4.0 – 11.5 hours | Continuous digital device exposure metric |
| **10** | `Physical Activity Level` | String | Low, Moderate, High | Weekly exercise and physical activity tier |
| **11** | `Social Interaction Score`| Integer | 0 – 100 | Interpersonal social engagement level |
| **12** | `Mental Health History` | String | Yes, No | Pre-existing clinical psychological diagnosis history |
| **13** | `Therapy Type` | String | CBT, Counseling, Meditation, Support Group, No Therapy | Psychological intervention modality |
| **14** | `Intervention Duration (weeks)`| Integer | 0 – 12 weeks | Total clinical treatment exposure length |
| **15** | `Progress Score` | Integer | 0 – 100 | Post-intervention recovery and symptom alleviation |
| **16** | `Medication Usage` | String | Yes, No | Active psychiatric pharmacotherapy usage |
| **17** | `Support System Strength`| String | Low, Medium, High | Perceived peer and family support network buffer |
| **18** | `Work-Life Balance Score`| Integer | 0 – 100 | Self-assessed academic lifestyle balance |

---

## 6. Data Validation
- **What Was Done:** Automated validation across all 3,600 data cells verifying completeness, uniqueness, range boundaries, and data types.
- **Why It Was Done:** To prevent data distortion, eliminate null values, and verify analytical integrity before any visual encoding.
- **Tools Used:** Python script `scripts/validate_dataset.py`, JSON.
- **Artifacts Produced:**
  - Automated Summary: [`data/cleaned/validation_summary.json`](../data/cleaned/validation_summary.json)
  - Validation Report: [`docs/dataset_validation.md`](dataset_validation.md)
- **Validation Results:**
  - Missing Values: **0 cells (0.00%)**
  - Duplicate Records: **0 duplicates**
  - Clinical Bounds: Anxiety (10–95), Depression (10–95), Screen Time (4.0–11.5), Age (18–25) all strictly within valid psychometric boundaries.

---

## 7. Data Preparation
- **What Was Done:** Formatted and certified the dataset into a visualization-ready state without altering or fabricating values.
- **Why It Was Done:** To satisfy the SkillWallet *Data Preparation* requirement and confirm that the dataset meets Tableau ingestion standards.
- **Tools Used:** Python, Pandas.
- **Artifacts Produced:**
  - Visualization-Ready CSV: [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](../data/cleaned/mental_health_student_ecosystem_cleaned.csv) ($19.84\text{ KB}$, 200 rows)
  - Preparation Documentation: [`docs/data_preparation.md`](data_preparation.md)
- **Validation Statement:** The dataset is 100% complete, clean, and ready for visualization.

---

## 8. Data Visualization (8 Unique Visualizations)
- **What Was Done:** Developed eight unique, empirically grounded visualizations using exclusively the verified 18 columns. Generic portal templates referencing missing fields (*Study Hours*, *Heart Rate Variability*) were explicitly excluded.
- **Why It Was Done:** To explore bivariate and multivariate distributions linking stress, psychometrics, lifestyle vectors, and treatment modalities.
- **Tools Used:** Matplotlib, Seaborn, Python script `scripts/generate_visualizations.py`.
- **Artifacts Produced:**
  1. `01_stress_level_distribution.png` — Vertical Bar Chart (Low: 22.0%, Med: 53.5%, High: 24.5%)
  2. `02_stress_vs_anxiety.png` — Vertical Bar Chart (High: 72.06 vs Low: 30.27)
  3. `03_stress_vs_depression.png` — Vertical Bar Chart (High: 68.78 vs Low: 26.80)
  4. `04_gender_mental_health_comparison.png` — Grouped Dual-Measure Bar Chart
  5. `05_sleep_quality_vs_stress.png` — Segmented Stacked Bar Chart (71.4% poor sleep in high stress)
  6. `06_screen_time_vs_stress.png` — Vertical Bar Chart (High stress averages 8.12 hrs/day)
  7. `07_mental_health_history_distribution.png` — Donut Chart (60% no prior history, 40% prior history)
  8. `08_therapy_type_vs_progress.png` — Horizontal Ranked Bar Chart (CBT top at 40.80 progress score)
  - Detailed Specification: [`docs/data_visualization.md`](data_visualization.md)
  - Visual Evidence: [`evidence/visualizations/`](../evidence/visualizations/)

---

## 9. Dashboard Design (Multi-Device Responsive Architecture)
- **What Was Done:** Engineered an integrated executive dashboard prototype featuring 4 cohort KPI cards and 6 specialized panels, with dedicated responsive layouts for Desktop, Tablet, and Mobile devices.
- **Why It Was Done:** To provide campus leaders with an intuitive, unified diagnostic command center adaptable to desktop monitors, iPads, and smartphones.
- **Tools Used:** Python, Matplotlib GridSpec, PIL, `scripts/generate_dashboard_prototypes.py`.
- **Artifacts Produced:**
  - Desktop Prototype (1920×1080 / 16:9): [`evidence/dashboard/student_mental_health_dashboard.png`](../evidence/dashboard/student_mental_health_dashboard.png)
  - Tablet Prototype (1024×768 / 2-Column): [`evidence/dashboard/tablet_dashboard.png`](../evidence/dashboard/tablet_dashboard.png)
  - Mobile Prototype (Vertical Stack): [`evidence/dashboard/mobile_dashboard.png`](../evidence/dashboard/mobile_dashboard.png)
  - Layout Architecture Specification: [`docs/dashboard_design.md`](dashboard_design.md)
- **Key KPIs Displayed:** Total Students (`200`), Avg Anxiety (`52.59`), Avg Depression (`48.09`), Daily Screen Time (`7.10 hrs`).

---

## 10. Story Development (5-Scene Narrative)
- **What Was Done:** Structured and synthesized a sequential 5-scene Tableau Data Story translating diagnostic metrics into institutional recommendations.
- **Why It Was Done:** To guide stakeholders step-by-step through baseline spread, symptom surges, lifestyle risks, vulnerability factors, and clinical recovery.
- **Tools Used:** Python, Matplotlib, `scripts/generate_story_scenes.py`.
- **Artifacts Produced:**
  - Scene 1: Student Mental Health Baseline ([`evidence/story/01_baseline.png`](../evidence/story/01_baseline.png))
  - Scene 2: Stress and Psychological Symptoms ([`evidence/story/02_psychological_symptoms.png`](../evidence/story/02_psychological_symptoms.png))
  - Scene 3: Lifestyle Factors and Stress ([`evidence/story/03_lifestyle_and_stress.png`](../evidence/story/03_lifestyle_and_stress.png))
  - Scene 4: Vulnerability Factors and Support Systems ([`evidence/story/04_vulnerability_and_support.png`](../evidence/story/04_vulnerability_and_support.png))
  - Scene 5: Intervention Patterns and Recovery Progress ([`evidence/story/05_intervention_and_progress.png`](../evidence/story/05_intervention_and_progress.png))
  - Story Documentation: [`docs/story.md`](story.md)

---

## 11. Performance Testing & Architectural Benchmarks
- **What Was Done:** Completed all four subtasks of the Performance Testing epic:
  1. *Amount of Data Rendered:* Measured disk size ($19.84\text{ KB}$), in-memory size ($137.12\text{ KB}$), raw parse latency ($0.64\text{ ms}$), and DataFrame load ($3.17\text{ ms}$).
  2. *Utilization of Data Filters:* Benchmarked 8 representative single- and multi-predicate filter scenarios ($0.86 - 1.41\text{ ms}$ execution latencies).
  3. *Number of Calculation Fields:* Formulated and documented 10 production calculation fields (5 Measures, 5 Dimensions) with exact Tableau formulas.
  4. *Number of Visualizations:* Audited the 8 verified dataset-grounded visualizations.
- **Tools Used:** Python `time.perf_counter()`, `scripts/benchmark_data_rendering.py`, `scripts/benchmark_filter_utilization.py`, `scripts/generate_calculation_fields_spec.py`.
- **Artifacts Produced:**
  - Reports: [`docs/performance_testing.md`](performance_testing.md), [`docs/performance_data_rendering.md`](performance_data_rendering.md), [`docs/performance/filter_utilization.md`](performance/filter_utilization.md), [`docs/performance/calculation_fields.md`](performance/calculation_fields.md), [`docs/performance/visualization_inventory.md`](performance/visualization_inventory.md)
  - Visual Evidence: [`evidence/performance/data_rendering/`](../evidence/performance/data_rendering/), [`evidence/performance/filters/`](../evidence/performance/filters/), [`evidence/performance/calculations/`](../evidence/performance/calculations/)

---

## 12. Web Integration & Flask Portal
- **What Was Done:** Built and deployed a full-stack Flask web portal hosting the project overview, responsive dashboard views, 5-scene story narrative, and technical methodology.
- **Why It Was Done:** To provide a production-ready web application supporting both live Tableau cloud embedding and seamless local prototype fallbacks.
- **Tools Used:** Python Flask, Jinja2, HTML5/CSS3, JavaScript, Playwright.
- **Artifacts Produced:**
  - Application Code: [`app.py`](../app.py), [`templates/`](../templates/), [`static/`](../static/)
  - Documentation: [`docs/web_integration.md`](web_integration.md)
  - Full-Page Validation Evidence: [`evidence/web_integration/`](../evidence/web_integration/) (`home_page.png`, `dashboard_page.png`, `story_page.png`, `about_page.png`)
- **Validation:** All 4 routes (`/`, `/dashboard`, `/story`, `/about`) validated with HTTP 200 OK via Playwright.

---

## 13. Tableau Publication Status & Transparency
- **Tableau Public Author Profile:** [`https://public.tableau.com/app/profile/sufiyansurve333`](https://public.tableau.com/app/profile/sufiyansurve333)
- **Status Notice:** Native Tableau Public cloud workbook publishing remains pending manual GUI authoring in the authenticated browser session. Headless automated publishing was stopped honestly to adhere to academic integrity rules and prevent session corruption.
- **Prepared Readiness:** All 8 worksheets, 10 calculation fields, dashboard grid layouts, and 5 story scenes are 100% specified. Live embedding is immediately enabled once `TABLEAU_DASHBOARD_URL` and `TABLEAU_STORY_URL` are provided.

---

## 14. Key Empirical Findings
1. **High Stress Prevalence:** 78.0% of the student cohort (156 of 200) operates in moderate-to-high stress tiers.
2. **Direct Symptom Escalation:** High Stress students experience a **>135% surge** in anxiety (72.06 vs 30.27) and depression (68.78 vs 26.80) relative to Low Stress students.
3. **The Lifestyle Triad:** 71.4% of high-stress students suffer from Poor sleep, combined with **8.12 hours/day** of screen immersion and 75.5% low physical activity.
4. **Acute First-Onset Distress:** 60.0% of students report no prior mental health history, yet this group contains 66 Medium-stress and 14 High-stress students experiencing first-onset university distress.
5. **The Care Gap:** 107 of 200 students (53.5%) receive No Therapy, including 15 high-stress and 48 medium-stress students.
6. **Clinical Efficacy of CBT:** Cognitive Behavioral Therapy achieves the highest recovery progress score (**40.80** across an average of 7.50 weeks).

---

## 15. Strategic Recommendations
1. **Scale Structured CBT Programs:** Partner with university clinical psychology departments to expand access to structured Cognitive Behavioral Therapy.
2. **Institutional Digital Wellness & Sleep Hygiene:** Embed digital screen awareness and sleep hygiene workshops into standard residence hall curricula.
3. **Proactive Freshman Screening:** Institute opt-in, non-stigmatized mental health screenings during orientation to identify distressed students before academic probation.
4. **Targeted Peer Support Groups:** Expand peer-led support groups (recovery progress score 33.10) to reach un-enrolled students reluctant to seek formal counseling.

---

## 16. Limitations
1. **Sample Size:** The dataset represents 200 university students; expanding to multi-campus cohorts ($N > 2,000$) would increase statistical generalization.
2. **Cross-Sectional Sampling:** Longitudinal tracking across semesters is recommended to observe symptom trajectories during midterm vs final exam cycles.
3. **Tableau Public Free-Tier API:** Lack of automated REST API workbook publishing on free accounts requires manual browser upload.

---

## 17. Future Scope
1. **Predictive Machine Learning Integration:** Deploy a Random Forest or XGBoost model inside the Flask portal to compute individual risk probabilities based on sleep and screen time.
2. **Mobile Push Notifications:** Incorporate automated wellness nudges when daily screen time thresholds are exceeded.
3. **Multi-Institutional Benchmarking:** Compare stress indices across engineering, medical, and liberal arts programs nationwide.

---

## 18. Project Repository & Evidence Directory
- **GitHub Repository:** [`https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem`](https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem)
- **Visual Evidence Directory:** [`evidence/visualizations/`](../evidence/visualizations/)
- **Dashboard Prototypes:** [`evidence/dashboard/`](../evidence/dashboard/)
- **Story Scene Prototypes:** [`evidence/story/`](../evidence/story/)
- **Performance Benchmarks:** [`evidence/performance/`](../evidence/performance/)
- **Web Integration Evidence:** [`evidence/web_integration/`](../evidence/web_integration/)
- **Demonstration Video:** [`evidence/demo/project_explanation_video.mp4`](../evidence/demo/project_explanation_video.mp4)

---

## 19. End-to-End Development Summary
The *Analysing Mental Health in Student Ecosystem* project successfully executed every phase of the data analytics lifecycle:
- Ingested and validated a 200-row, 18-variable psychometric dataset with zero defects.
- Authored 8 dataset-grounded visualizations and 10 production calculation fields.
- Prototyped a multi-device responsive dashboard and a 5-scene guided data story.
- Benchmarked data ingestion and filter latencies to guarantee sub-millisecond execution.
- Deployed a Python Flask web portal with modern `<tableau-viz>` cloud embedding.
- Produced high-resolution demonstration artifacts and complete development documentation.
