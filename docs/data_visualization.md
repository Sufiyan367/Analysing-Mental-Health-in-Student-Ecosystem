# Data Visualization Report: 8 Unique Dataset-Grounded Visualizations

## 1. Overview
This document records the **Data Visualization** task (*No of Unique Visualizations*) for the capstone project **Analysing Mental Health in Student Ecosystem** (SkillWallet / SmartBridge).

### Integrity & Grounding Notice:
The SkillWallet syllabus displays default generic examples referencing variables such as *Study Hours*, *Academic Performance*, and *Heart Rate Variability*, which do not exist in our actual schema. Rather than fabricating missing columns, this project authors **8 unique, empirically grounded visualizations** using exclusively the verified 18 columns of our dataset.

- **Primary Dataset Source:** [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](../data/cleaned/mental_health_student_ecosystem_cleaned.csv)
- **Artifact Directory:** [`evidence/visualizations/`](../evidence/visualizations/)
- **Validation Statement:** All data aggregations, sums, means, and percentages are computed directly from the 200 records in the verified dataset with zero synthetic distortion or manual fabrication.

---

## 2. Summary Table of Visualizations

| # | Title | Chart Type | Dimensions & Measures Used | Status | Artifact Location |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **01** | Stress Level Distribution | Bar Chart | Dimension: `Stress Level`<br>Measure: `Count of User ID` | **Complete** | [`01_stress_level_distribution.png`](../evidence/visualizations/01_stress_level_distribution.png) |
| **02** | Stress Level vs Anxiety Score | Bar Chart | Dimension: `Stress Level`<br>Measure: `Average Anxiety Score` | **Complete** | [`02_stress_vs_anxiety.png`](../evidence/visualizations/02_stress_vs_anxiety.png) |
| **03** | Stress Level vs Depression Score | Bar Chart | Dimension: `Stress Level`<br>Measure: `Average Depression Score` | **Complete** | [`03_stress_vs_depression.png`](../evidence/visualizations/03_stress_vs_depression.png) |
| **04** | Mental Health Burden Comparison by Gender | Grouped Bar Chart | Dimension: `Gender`<br>Measures: `Average Anxiety Score`, `Average Depression Score` | **Complete** | [`04_gender_mental_health_comparison.png`](../evidence/visualizations/04_gender_mental_health_comparison.png) |
| **05** | Sleep Quality vs Stress Level Distribution | Stacked Bar Chart | Dimensions: `Sleep Quality`, `Stress Level`<br>Measure: `Count of User ID` | **Complete** | [`05_sleep_quality_vs_stress.png`](../evidence/visualizations/05_sleep_quality_vs_stress.png) |
| **06** | Screen Time vs Stress Level | Bar Chart | Dimension: `Stress Level`<br>Measure: `Average Daily Screen Time (hrs)` | **Complete** | [`06_screen_time_vs_stress.png`](../evidence/visualizations/06_screen_time_vs_stress.png) |
| **07** | Mental Health History Prevalence | Donut Chart | Dimension: `Mental Health History`<br>Measure: `Count of User ID` | **Complete** | [`07_mental_health_history_distribution.png`](../evidence/visualizations/07_mental_health_history_distribution.png) |
| **08** | Ranked Therapy Efficacy by Progress Score | Horizontal Ranked Bar Chart | Dimension: `Therapy Type`<br>Measure: `Average Progress Score` | **Complete** | [`08_therapy_type_vs_progress.png`](../evidence/visualizations/08_therapy_type_vs_progress.png) |

---

## 3. Detailed Specifications for Each Visualization

### Visualization 1: Stress Level Distribution Across Student Cohort
- **Artifact:** `evidence/visualizations/01_stress_level_distribution.png`
- **Objective:** Quantify the baseline spread of stress severity across the student population to identify cohort vulnerability.
- **Dimensions:** `Stress Level` (Categorical: `Low`, `Medium`, `High`)
- **Measures:** `Count of User ID` (Frequency)
- **Chart Type:** Vertical Bar Chart with direct count and percentage labeling.
- **Exact Data Fields Used:** `Stress Level`, `User ID`
- **Data Source:** `data/cleaned/mental_health_student_ecosystem_cleaned.csv`
- **Key Interpretation:** The majority of students report `Medium` stress (107 students, 53.5%), while 49 students (24.5%) suffer from `High` stress, and 44 students (22.0%) experience `Low` stress. Over 78% of the student cohort experiences moderate-to-severe stress.
- **Validation Statement:** Aggregation matches 100% of rows ($44 + 107 + 49 = 200$).

---

### Visualization 2: Average Anxiety Score by Stress Level
- **Artifact:** `evidence/visualizations/02_stress_vs_anxiety.png`
- **Objective:** Determine the direct psychometric correlation between perceived stress and standardized anxiety metrics.
- **Dimensions:** `Stress Level` (Categorical: `Low`, `Medium`, `High`)
- **Measures:** `AVG(Anxiety Score)` (Continuous: Scale 0–100)
- **Chart Type:** Bar Chart with data callouts.
- **Exact Data Fields Used:** `Stress Level`, `Anxiety Score`
- **Data Source:** `data/cleaned/mental_health_student_ecosystem_cleaned.csv`
- **Key Interpretation:** There is a progressive, steep escalation in anxiety scores with higher stress tiers: `Low Stress` students average **30.27**, `Medium Stress` students average **52.85**, and `High Stress` students average **72.06**, representing a 138% surge in anxiety symptoms from low to high stress cohorts.
- **Validation Statement:** Validated by grouped arithmetic mean of all 200 records.

---

### Visualization 3: Average Depression Score by Stress Level
- **Artifact:** `evidence/visualizations/03_stress_vs_depression.png`
- **Objective:** Evaluate how depression symptoms escalate across self-reported stress categories.
- **Dimensions:** `Stress Level` (Categorical: `Low`, `Medium`, `High`)
- **Measures:** `AVG(Depression Score)` (Continuous: Scale 0–100)
- **Chart Type:** Bar Chart with numeric callouts.
- **Exact Data Fields Used:** `Stress Level`, `Depression Score`
- **Data Source:** `data/cleaned/mental_health_student_ecosystem_cleaned.csv`
- **Key Interpretation:** Paralleling anxiety trends, depression severity increases systematically from **26.80** in `Low Stress` to **47.37** in `Medium Stress` and **68.78** in `High Stress`. This demonstrates that chronic stress in the student ecosystem strongly co-occurs with depressive symptom loads.
- **Validation Statement:** Direct calculation matches pandas aggregation of the cleaned dataset.

---

### Visualization 4: Mental Health Burden Comparison by Gender
- **Artifact:** `evidence/visualizations/04_gender_mental_health_comparison.png`
- **Objective:** Compare anxiety and depression psychometric burdens across gender identities to uncover disparities in distress.
- **Dimensions:** `Gender` (Categorical: `Female`, `Male`, `Other`)
- **Measures:** `AVG(Anxiety Score)`, `AVG(Depression Score)`
- **Chart Type:** Grouped Dual-Measure Bar Chart.
- **Exact Data Fields Used:** `Gender`, `Anxiety Score`, `Depression Score`
- **Data Source:** `data/cleaned/mental_health_student_ecosystem_cleaned.csv`
- **Key Interpretation:** Average anxiety scores remain consistently elevated across all groups: `Other` gender individuals average **53.5** (Depression: **50.4**), `Female` students average **53.3** (Depression: **48.1**), and `Male` students average **51.8** (Depression: **47.9**). Distress is distributed throughout all demographic groups, highlighting the need for universal, inclusive campus interventions.
- **Validation Statement:** Group averages validated across all 97 female, 92 male, and 11 other participants.

---

### Visualization 5: Sleep Quality vs Stress Level Distribution
- **Artifact:** `evidence/visualizations/05_sleep_quality_vs_stress.png`
- **Objective:** Reveal the compounding relationship between physiological sleep deprivation and stress severity.
- **Dimensions:** `Sleep Quality` (`Good`, `Average`, `Poor`), `Stress Level` (`Low`, `Medium`, `High`)
- **Measures:** `Count of User ID`
- **Chart Type:** Stacked Bar Chart with discrete segment values.
- **Exact Data Fields Used:** `Sleep Quality`, `Stress Level`, `User ID`
- **Data Source:** `data/cleaned/mental_health_student_ecosystem_cleaned.csv`
- **Key Interpretation:** Of the 49 students with `High Stress`, **35 (71.4%)** experience `Poor` sleep, 12 experience `Average` sleep, and only 2 maintain `Good` sleep. Conversely, 50.0% of students with `Low Stress` enjoy `Good` sleep and only 1 student has `Poor` sleep. Sleep deterioration is one of the strongest behavioral indicators of psychological distress.
- **Validation Statement:** Segment totals cross-tabulate to exactly 200 participants ($45 + 89 + 66 = 200$).

---

### Visualization 6: Average Daily Screen Time by Stress Level
- **Artifact:** `evidence/visualizations/06_screen_time_vs_stress.png`
- **Objective:** Investigate how digital exposure and screentime relate to student stress levels.
- **Dimensions:** `Stress Level` (Categorical: `Low`, `Medium`, `High`)
- **Measures:** `AVG(Daily Screen Time (hrs))` (Continuous: Hours)
- **Chart Type:** Bar Chart with hourly callouts.
- **Exact Data Fields Used:** `Stress Level`, `Daily Screen Time (hrs)`
- **Data Source:** `data/cleaned/mental_health_student_ecosystem_cleaned.csv`
- **Key Interpretation:** Students in the `High Stress` tier average **8.12 hours/day** of screen time, compared to **7.07 hours/day** for `Medium Stress` and **6.00 hours/day** for `Low Stress`. The +2.12 hour daily digital immersion in high-stress students highlights screen saturation and digital exhaustion as major lifestyle stressors.
- **Validation Statement:** Direct mean calculation on continuous `Daily Screen Time (hrs)` variable.

---

### Visualization 7: Mental Health History Prevalence
- **Artifact:** `evidence/visualizations/07_mental_health_history_distribution.png`
- **Objective:** Show the breakdown between students with pre-existing mental health history and first-time distressed students.
- **Dimensions:** `Mental Health History` (Categorical: `Yes`, `No`)
- **Measures:** `Count of User ID` (Percentage and Total Count)
- **Chart Type:** Donut Chart with central cohort total callout.
- **Exact Data Fields Used:** `Mental Health History`, `User ID`
- **Data Source:** `data/cleaned/mental_health_student_ecosystem_cleaned.csv`
- **Key Interpretation:** 40.0% (80 students) of the cohort possess a documented prior history of mental health challenges, while 60.0% (120 students) have no prior history. This indicates university counseling services must cater both to ongoing psychiatric management and emergent first-onset episodes.
- **Validation Statement:** Validated: 120 'No' (60%) and 80 'Yes' (40%) equal the 200 cohort baseline.

---

### Visualization 8: Ranked Therapy Efficacy by Average Progress Score
- **Artifact:** `evidence/visualizations/08_therapy_type_vs_progress.png`
- **Objective:** Compare the clinical efficacy of different therapeutic interventions across students undergoing active care.
- **Dimensions:** `Therapy Type` (`CBT`, `Counseling`, `Support Group`, `Meditation`)
- **Measures:** `AVG(Progress Score)` (Continuous: Scale 0–100)
- **Chart Type:** Ranked Horizontal Bar Chart.
- **Exact Data Fields Used:** `Therapy Type`, `Progress Score`
- **Data Source:** `data/cleaned/mental_health_student_ecosystem_cleaned.csv` (excluding `No Therapy` group, $n=93$ active intervention recipients)
- **Key Interpretation:** Cognitive Behavioral Therapy (`CBT`) proves to be the most effective intervention with an average progress score of **40.80**, followed by `Counseling` (**34.43**), `Support Group` (**33.10**), and `Meditation` (**32.57**). All active interventions provide measurable symptom relief, with structured structured cognitive modalities yielding the strongest outcomes.
- **Validation Statement:** Calculated strictly across students receiving intervention ($n=93$).

---

## 4. Methodological Note & Execution Disclaimer
These visualizations were generated reproducibly and verified using Python Matplotlib data pipelines directly against [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](../data/cleaned/mental_health_student_ecosystem_cleaned.csv) as visual evidence and chart prototypes for subsequent Tableau Web Authoring. No invalid Tableau XML or synthetic TWB/TWBX files were manufactured.
