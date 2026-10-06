# Data Story: Analysing Mental Health in Student Ecosystem

## 1. Executive Summary & Narrative Objective
This document outlines the **5-Scene Guided Data Story** for the capstone project **Analysing Mental Health in Student Ecosystem** (Course: *Data Analytics with Tableau*, SkillWallet / SmartBridge).

### Story Objective:
To guide institutional stakeholders through an evidence-based journey that:
1. Establishes the student population's psychological distress baseline.
2. Dissects how subjective stress levels manifest into quantifiable anxiety and depression symptoms.
3. Examines lifestyle vectors (sleep deprivation, screen time saturation, and physical inactivity) associated with high stress.
4. Explores vulnerability patterns (pre-existing history vs. first-onset cases, support networks, and psychiatric medication).
5. Evaluates intervention outcomes across therapy modalities to propose institutional interventions.

### Target Audience:
- University Deans, Provosts, and Academic Leadership
- Student Mental Health and Counseling Center Directors
- Student Affairs and Wellness Committees

**Source of Truth:** [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](../data/cleaned/mental_health_student_ecosystem_cleaned.csv) ($N=200$, 18 columns)  
**Story Visual Evidence:** [`evidence/story/`](../evidence/story/)

---

## 2. Story Structure & Scene-by-Scene Architecture

```
Scene 1: Student Mental Health Baseline
   └── [Question: What is the overall distress prevalence across the student cohort?]
         │
         ▼
Scene 2: Stress and Psychological Symptoms
   └── [Question: How do anxiety and depression symptom loads escalate across stress tiers?]
         │
         ▼
Scene 3: Lifestyle Factors and Stress
   └── [Question: What behavioral vectors (sleep, screen time, exercise) correlate with high stress?]
         │
         ▼
Scene 4: Vulnerability Factors and Support Systems
   └── [Question: How do prior mental-health history and social support influence student resilience?]
         │
         ▼
Scene 5: Intervention Patterns and Recovery Progress
   └── [Question: Which therapeutic interventions demonstrate measurable symptom recovery?]
```

---

## 3. Detailed Scene Specifications

### Scene 1 — Student Mental Health Baseline
- **Artifact:** [`evidence/story/01_baseline.png`](../evidence/story/01_baseline.png)
- **Analytical Objective:** Introduce the student cohort and establish the foundational psychological distress baseline across all 200 participants.
- **Visualizations Incorporated:**
  - 4 Header KPI Cards: Total Students (`200`), Average Anxiety Score (`52.59`), Average Depression Score (`48.09`), Average Daily Screen Time (`7.10 hrs`).
  - Stress Level Distribution (Bar Chart): Low (`44`, 22.0%), Medium (`107`, 53.5%), High (`49`, 24.5%).
- **Exact Dataset Fields Used:** `User ID`, `Stress Level`, `Anxiety Score`, `Depression Score`, `Daily Screen Time (hrs)`.
- **Evidence-Based Observations:**
  1. *High Stress Prevalence:* Over three-quarters of the student population (**78.0%**, 156 of 200) experience moderate-to-high stress levels.
  2. *Elevated Symptom Baseline:* The student cohort demonstrates an average anxiety score of **52.59** and an average depression score of **48.09** (scale 0–100), reflecting a substantial baseline burden of distress.
  3. *High Digital Exposure:* Students average **7.10 hours** of daily screen time across academic study and personal devices.
- **Narrative Transition:** *Having established the cohort baseline, how do these self-reported stress categories translate into standardized clinical anxiety and depression symptom loads?*

---

### Scene 2 — Stress and Psychological Symptoms
- **Artifact:** [`evidence/story/02_psychological_symptoms.png`](../evidence/story/02_psychological_symptoms.png)
- **Analytical Objective:** Quantify how standardized anxiety and depression scores escalate across low, medium, and high stress tiers.
- **Visualizations Incorporated:**
  - Grouped Dual-Measure Bar Chart: `AVG(Anxiety Score)` and `AVG(Depression Score)` by `Stress Level`.
- **Exact Dataset Fields Used:** `Stress Level`, `Anxiety Score`, `Depression Score`.
- **Evidence-Based Observations:**
  1. *Steep Symptom Escalation:* Students in the High Stress group average **72.06** in anxiety and **68.78** in depression, compared to **30.27** and **26.80** respectively for Low Stress students (a $>135\%$ symptom escalation).
  2. *Concurrent Symptom Manifestation:* Anxiety and depression scores increase in parallel across stress categories, confirming that high academic stress co-occurs with compounding psychological distress.
  3. *Proximity to Clinical Thresholds:* The High Stress cohort approaches severe clinical symptom thresholds on both standardized psychometric scales.
- **Narrative Transition:** *Given the severity of psychological symptoms in high-stress students, what lifestyle habits (sleep patterns, screentime immersion) distinguish this cohort?*

---

### Scene 3 — Lifestyle Factors and Stress
- **Artifact:** [`evidence/story/03_lifestyle_and_stress.png`](../evidence/story/03_lifestyle_and_stress.png)
- **Analytical Objective:** Examine the associations between physiological sleep restfulness, digital exposure, and stress levels.
- **Visualizations Incorporated:**
  - Sleep Quality vs. Stress Tier (Stacked Bar Chart: Good, Average, Poor by Stress Level).
  - Average Daily Screen Time by Stress Level (Bar Chart).
- **Exact Dataset Fields Used:** `Sleep Quality`, `Daily Screen Time (hrs)`, `Physical Activity Level`, `Stress Level`.
- **Evidence-Based Observations:**
  1. *Compounded Sleep Deficit:* Among the 49 students with High Stress, **35 (71.4%)** report Poor sleep, 12 report Average sleep, and only 2 maintain Good sleep. Conversely, 50.0% of Low Stress students report Good sleep.
  2. *Extended Digital Immersion:* High Stress students log an average of **8.12 hours/day** of screen time (+2.12 hours more than Low Stress students at 6.00 hrs/day).
  3. *Physical Inactivity Vector:* 75.5% (37 of 49) of High Stress students engage in Low physical activity, showing a triad of sleep loss, screen immersion, and sedentary routines.
- **Narrative Transition:** *Beyond daily lifestyle habits, how do pre-existing mental health history, support networks, and psychiatric medication intersect with student vulnerability?*

---

### Scene 4 — Vulnerability Factors and Support Systems
- **Artifact:** [`evidence/story/04_vulnerability_and_support.png`](../evidence/story/04_vulnerability_and_support.png)
- **Analytical Objective:** Explore prior mental-health diagnoses, social support network strength, and psychiatric medication usage across stress tiers.
- **Visualizations Incorporated:**
  - Prior Mental Health History Prevalence (Donut Chart: 60% No History, 40% Prior History).
  - Support System Strength vs. Stress Tier (Stacked Bar Chart: Low, Medium, High support).
- **Exact Dataset Fields Used:** `Mental Health History`, `Support System Strength`, `Medication Usage`, `Stress Level`.
- **Evidence-Based Observations:**
  1. *Pre-Existing History Concentration:* 40.0% (80 students) have a documented prior mental health history; within the High Stress cohort, **71.4% (35 of 49)** have a pre-existing history.
  2. *Campus First-Onset Cases:* 60.0% (120 students) report no prior history, yet this group includes 66 Medium-stress and 14 High-stress students, highlighting significant first-onset distress occurring during university studies.
  3. *Support System Buffer:* Students with High support networks are disproportionately concentrated in Low (8) and Medium (24) stress tiers.
  4. *Targeted Medication Usage:* Only 9.0% (18 students) use psychiatric medication, with 15 of the 18 users belonging to the High Stress tier.
- **Narrative Transition:** *For students engaged in active psychological support, which therapy modalities demonstrate empirical recovery gains?*

---

### Scene 5 — Intervention Patterns and Recovery Progress
- **Artifact:** [`evidence/story/05_intervention_and_progress.png`](../evidence/story/05_intervention_and_progress.png)
- **Analytical Objective:** Evaluate the clinical efficacy of therapeutic interventions, analyze treatment durations, and outline strategic campus recommendations.
- **Visualizations Incorporated:**
  - Ranked Average Progress Score by Therapy Type (Horizontal Bar Chart across active recipients $n=93$).
- **Exact Dataset Fields Used:** `Therapy Type`, `Intervention Duration (weeks)`, `Progress Score`, `Medication Usage`.
- **Evidence-Based Observations:**
  1. *CBT Demonstrates Strongest Recovery:* Cognitive Behavioral Therapy (CBT) achieves the highest average progress score (**40.80** across an average duration of 7.50 weeks), demonstrating the efficacy of structured cognitive restructuring.
  2. *Broad Therapeutic Benefit:* Counseling (**34.43**), Support Groups (**33.10**), and Meditation (**32.57**) all yield positive progress scores, confirming that diverse clinical and peer-led modalities provide measurable symptom relief.
  3. *The Institutional Care Gap:* **107 of 200 students (53.5%)** receive "No Therapy", including 14 students with High Stress and 66 with Medium Stress, pointing to a critical service reach deficit.
- **Strategic Policy Recommendations:**
  - *Expand CBT Availability:* Partner with counseling interns and clinical psychology departments to increase capacity for evidence-based CBT.
  - *Institutional Sleep & Digital Wellness Workshops:* Implement structured campus workshops focusing on digital screen limits and sleep hygiene.
  - *Proactive Early Screening:* Institute opt-in mental health screenings during orientation to identify distressed students before crisis thresholds are reached.

---

## 4. Implementation Status & Tableau Integrity Notice

- **Implementation Method:** The 5 guided story scenes were synthesized programmatically using Python and Matplotlib grid-spec layouts directly against [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](../data/cleaned/mental_health_student_ecosystem_cleaned.csv).
- **Integrity Compliance:**
  - All visual artifacts are stored under [`evidence/story/`](../evidence/story/) as verified Story prototypes and specifications.
  - No synthetic Tableau XML or fake `.twb`/`.twbx` files were hand-coded.
  - No claims of automated Tableau Public publishing were fabricated.
  - Generic demo fields (such as *Study Hours*, *Academic Performance*, and *Heart Rate Variability*) were omitted.
