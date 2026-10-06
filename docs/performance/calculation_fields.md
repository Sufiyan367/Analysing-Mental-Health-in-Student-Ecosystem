# Performance Testing: Inventory & Specification of Calculation Fields

**Project:** Analysing Mental Health in Student Ecosystem  
**Epic:** Performance Testing  
**Task:** No of Calculation Fields  
**Source of Truth:** [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](../../data/cleaned/mental_health_student_ecosystem_cleaned.csv) ($N=200$, 18 columns)  
**Evidence Artifacts:**  
- Specification Data: [`evidence/performance/calculations/calculation_fields_spec.json`](../../evidence/performance/calculations/calculation_fields_spec.json)  
- Visual Inventory Summary: [`evidence/performance/calculations/calculation_fields_inventory.png`](../../evidence/performance/calculations/calculation_fields_inventory.png)  

---

## 1. Executive Summary & Audit Rationale

To maintain analytical rigor, calculated fields are not arbitrarily inflated. Every calculated field documented in this specification fulfills a direct, demonstrable need within the 8 unique visualizations, the responsive multi-device dashboard, or the 5-scene narrative story.

> [!CRITICAL]
> **Tableau Integration Notice & Academic Integrity:**  
> A Python-derived column or statistical function is **not** automatically a Tableau calculated field. Because Tableau Public Web Authoring requires interactive browser manipulation that cannot be injected via automated headless backdoors, **no claim is made that these fields already exist inside a compiled Tableau `.twb`/`.twbx` file**.  
> Instead, this document provides the **exact production-grade Tableau formula definitions, data types, and application mappings** prepared for immediate native entry during GUI authoring.

---

## 2. Calculated Field Summary

Across the project architecture, **10 calculated fields** are genuinely required:
- **Calculated Measures (5):** Aggregate metrics for symptom severity, digital exposure, and clinical recovery.
- **Calculated Dimensions (5):** Demographic segmentation, clinical triage indicators, and compound vulnerability flags.

---

## 3. Detailed Specification of Genuinely Required Calculation Fields

### 1. `Average Anxiety Score`
- **Field Name:** `Average Anxiety Score`
- **Role & Type:** Calculated Measure (Aggregation), Continuous Float
- **Tableau Formula:**
  ```tableau
  AVG([Anxiety Score])
  ```
- **Source Field(s):** `Anxiety Score`
- **Why It Is Needed:** Provides the standardized population benchmark for generalized anxiety symptoms across dynamic filter selections.
- **Where It Is Used:** Header KPI Cards, Vis 2 (Stress vs Anxiety), Vis 4 (Gender Comparison), Story Scene 1 & 2.
- **Overall Dataset Value:** `52.59` (on 0–100 scale).

---

### 2. `Average Depression Score`
- **Field Name:** `Average Depression Score`
- **Role & Type:** Calculated Measure (Aggregation), Continuous Float
- **Tableau Formula:**
  ```tableau
  AVG([Depression Score])
  ```
- **Source Field(s):** `Depression Score`
- **Why It Is Needed:** Provides the baseline psychometric benchmark for depressive symptom severity.
- **Where It Is Used:** Header KPI Cards, Vis 3 (Stress vs Depression), Vis 4 (Gender Comparison), Story Scene 1 & 2.
- **Overall Dataset Value:** `48.09` (on 0–100 scale).

---

### 3. `Average Daily Screen Time`
- **Field Name:** `Average Daily Screen Time`
- **Role & Type:** Calculated Measure (Aggregation), Continuous Float
- **Tableau Formula:**
  ```tableau
  AVG([Daily Screen Time (hrs)])
  ```
- **Source Field(s):** `Daily Screen Time (hrs)`
- **Why It Is Needed:** Measures average digital exposure to detect lifestyle immersion and study-habit fatigue.
- **Where It Is Used:** Header KPI Card, Vis 6 (Screen Time vs Stress), Story Scene 1 & 3.
- **Overall Dataset Value:** `7.10 hrs` (7.0955 hrs).

---

### 4. `Total Student Cohort`
- **Field Name:** `Total Student Cohort`
- **Role & Type:** Calculated Measure (Aggregation), Discrete Integer
- **Tableau Formula:**
  ```tableau
  COUNTD([User ID])
  ```
- **Source Field(s):** `User ID`
- **Why It Is Needed:** Establishes the exact population denominator to compute percentage distributions across stress and demographic slices.
- **Where It Is Used:** Header KPI Card, Vis 1 (Distribution), Vis 5 (Sleep), Vis 7 (History), Story Scenes 1–5.
- **Overall Dataset Value:** `200` unique students.

---

### 5. `Therapy Active Indicator`
- **Field Name:** `Therapy Active Indicator`
- **Role & Type:** Calculated Dimension, Discrete String
- **Tableau Formula:**
  ```tableau
  IF [Therapy Type] != 'No Therapy' THEN 'Enrolled in Therapy' ELSE 'No Therapy' END
  ```
- **Source Field(s):** `Therapy Type`
- **Why It Is Needed:** Distinguishes students receiving active psychological interventions from un-enrolled students without filtering out records.
- **Where It Is Used:** Vis 8 (Therapy Efficacy), Dashboard Treatment Section, Story Scene 5.
- **Distribution in Dataset:** Active: `93` students (46.5%), No Therapy: `107` students (53.5%).

---

### 6. `High Stress Indicator`
- **Field Name:** `High Stress Indicator`
- **Role & Type:** Calculated Dimension (Binary Flag), Discrete String
- **Tableau Formula:**
  ```tableau
  IF [Stress Level] = 'High' THEN 'High Stress' ELSE 'Low or Moderate Stress' END
  ```
- **Source Field(s):** `Stress Level`
- **Why It Is Needed:** Enables conditional color formatting (e.g. red alert highlighting) and isolated calculation of high-risk student subsets.
- **Where It Is Used:** Dashboard High-Risk Alert cards, Story Scene 2 & 4.
- **Distribution in Dataset:** High Stress: `49` students (24.5%), Low/Moderate: `151` students (75.5%).

---

### 7. `Psychological Distress Index`
- **Field Name:** `Psychological Distress Index`
- **Role & Type:** Calculated Measure (Row-level Continuous), Float
- **Tableau Formula:**
  ```tableau
  ([Anxiety Score] + [Depression Score]) / 2.0
  ```
- **Source Field(s):** `Anxiety Score`, `Depression Score`
- **Why It Is Needed:** Synthesizes comorbid anxiety and depressive symptom loads into a single unified clinical severity index (0–100).
- **Where It Is Used:** Multivariate correlation analysis, Story Scene 2 composite symptom analysis.
- **Overall Dataset Value:** `50.34` mean index.

---

### 8. `Age Group`
- **Field Name:** `Age Group`
- **Role & Type:** Calculated Dimension (Categorical Binning), Discrete String
- **Tableau Formula:**
  ```tableau
  IF [Age] <= 19 THEN '18-19 (Underclass)'
  ELSEIF [Age] <= 21 THEN '20-21 (Upperclass)'
  ELSE '22+ (Postgraduate/Senior)'
  END
  ```
- **Source Field(s):** `Age`
- **Why It Is Needed:** Groups continuous student age into meaningful academic lifecycle segments, eliminating discrete noise in visual filters.
- **Where It Is Used:** Demographic filters, exploratory cohort comparisons.
- **Distribution in Dataset:** 18–19: `64` students, 20–21: `80` students, 22+: `56` students.

---

### 9. `Active Therapy Progress Score`
- **Field Name:** `Active Therapy Progress Score`
- **Role & Type:** Calculated Measure (Conditional Aggregation), Continuous Float
- **Tableau Formula:**
  ```tableau
  IF [Therapy Type] != 'No Therapy' THEN [Progress Score] ELSE NULL END
  ```
- **Source Field(s):** `Progress Score`, `Therapy Type`
- **Why It Is Needed:** Computes mean clinical improvement exclusively among students who completed psychological therapy, preventing zero-value distortion from un-enrolled students.
- **Where It Is Used:** Vis 8 (Therapy Type vs Progress Score), Dashboard Therapy Bar Chart, Story Scene 5.
- **Overall Dataset Value:** `35.78` across active recipients ($n=93$).

---

### 10. `High-Risk Sleep Deficit Flag`
- **Field Name:** `High-Risk Sleep Deficit Flag`
- **Role & Type:** Calculated Dimension (Compound Boolean Flag), Discrete String
- **Tableau Formula:**
  ```tableau
  IF [Stress Level] = 'High' AND [Sleep Quality] = 'Poor' 
  THEN 'High Risk (Severe Sleep Deficit)' 
  ELSE 'Standard Risk' 
  END
  ```
- **Source Field(s):** `Stress Level`, `Sleep Quality`
- **Why It Is Needed:** Identifies the highest-vulnerability lifestyle cohort (35 students, 71.4% of the high-stress subpopulation) for proactive clinical alerts.
- **Where It Is Used:** Dashboard behavioral triage cards, Story Scene 3 lifestyle vector callout.
- **Distribution in Dataset:** High Risk: `35` students (17.5% of total cohort).

---

## 4. Tableau Implementation Guide

During native authoring in Tableau Public Web Authoring or Tableau Desktop:
1. Open the Data pane and select **Create Calculated Field**.
2. Enter the field name exactly as specified above.
3. Paste the formula from the code blocks above.
4. Verify the pill type: Measures should default to Green continuous pills, Dimensions to Blue discrete pills.
5. Apply default number formatting (e.g. 2 decimal places for `Average Anxiety Score`, `Average Depression Score`, and `Average Daily Screen Time`).
