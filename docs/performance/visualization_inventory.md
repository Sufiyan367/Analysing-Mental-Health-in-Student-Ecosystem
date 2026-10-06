# Performance Testing: Visualization Inventory & Audit

**Project:** Analysing Mental Health in Student Ecosystem  
**Epic:** Performance Testing  
**Task:** No of Visualizations / Graphs  
**Source of Truth:** [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](../../data/cleaned/mental_health_student_ecosystem_cleaned.csv) ($N=200$, 18 columns)  
**Evidence Directory:** [`evidence/visualizations/`](../../evidence/visualizations/)  

---

## 1. Executive Summary & Audit Scope

This document finalizes the **official inventory of visualizations** for the *Analysing Mental Health in Student Ecosystem* project.

> [!IMPORTANT]
> **Audit & Integrity Rules:**  
> - **Zero Fabrication:** Only visualizations built strictly on the validated 18-column dataset are counted. Generic demo charts referencing missing fields (*Study Hours*, *Academic Performance*, *Heart Rate Variability*) are explicitly excluded.
> - **Prototype Status Transparency:** All 8 visual artifacts are high-resolution, reproducible visual prototypes and specification benchmarks generated directly from the underlying CSV dataset. They provide the pixel-exact blueprint for native Tableau authoring. No fake Tableau `.twb`/`.twbx` files or fabricated server URLs are reported.

---

## 2. Total Visualization Count

- **Total Unique Visualizations:** **8**
- **Dataset-Grounded:** **8 / 8 (100%)**
- **Excluded Demo Charts:** **All mismatched portal examples excluded**
- **Multi-Device Dashboard Variants:** **3** (Desktop, Tablet, Mobile)
- **Guided Story Scenes:** **5** (Sequential Narrative Scenes)

---

## 3. Comprehensive Visualization Inventory

| # | Visualization Title | Chart Type | Dimensions & Measures Used | Exact Fields Used | Evidence Path | Implementation Category |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| **1** | **Stress Level Distribution** | Vertical Bar Chart | Dimension: `Stress Level`<br>Measure: `Count of User ID` | `Stress Level`, `User ID` | [`01_stress_level_distribution.png`](../../evidence/visualizations/01_stress_level_distribution.png) | High-Resolution Prototype & Specification |
| **2** | **Stress Level vs Anxiety Score** | Vertical Bar Chart | Dimension: `Stress Level`<br>Measure: `AVG(Anxiety Score)` | `Stress Level`, `Anxiety Score` | [`02_stress_vs_anxiety.png`](../../evidence/visualizations/02_stress_vs_anxiety.png) | High-Resolution Prototype & Specification |
| **3** | **Stress Level vs Depression Score** | Vertical Bar Chart | Dimension: `Stress Level`<br>Measure: `AVG(Depression Score)` | `Stress Level`, `Depression Score` | [`03_stress_vs_depression.png`](../../evidence/visualizations/03_stress_vs_depression.png) | High-Resolution Prototype & Specification |
| **4** | **Gender Mental Health Comparison** | Grouped Dual-Measure Bar Chart | Dimension: `Gender`<br>Measures: `AVG(Anxiety Score)`, `AVG(Depression Score)` | `Gender`, `Anxiety Score`, `Depression Score` | [`04_gender_mental_health_comparison.png`](../../evidence/visualizations/04_gender_mental_health_comparison.png) | High-Resolution Prototype & Specification |
| **5** | **Sleep Quality vs Stress Level** | Segmented Stacked Bar Chart | Dimensions: `Sleep Quality`, `Stress Level`<br>Measure: `Count of User ID` | `Sleep Quality`, `Stress Level`, `User ID` | [`05_sleep_quality_vs_stress.png`](../../evidence/visualizations/05_sleep_quality_vs_stress.png) | High-Resolution Prototype & Specification |
| **6** | **Screen Time vs Stress Level** | Vertical Bar Chart | Dimension: `Stress Level`<br>Measure: `AVG(Daily Screen Time (hrs))` | `Stress Level`, `Daily Screen Time (hrs)` | [`06_screen_time_vs_stress.png`](../../evidence/visualizations/06_screen_time_vs_stress.png) | High-Resolution Prototype & Specification |
| **7** | **Mental Health History Prevalence** | Donut Chart | Dimension: `Mental Health History`<br>Measure: `Count of User ID` | `Mental Health History`, `User ID` | [`07_mental_health_history_distribution.png`](../../evidence/visualizations/07_mental_health_history_distribution.png) | High-Resolution Prototype & Specification |
| **8** | **Ranked Therapy Efficacy** | Horizontal Ranked Bar Chart | Dimension: `Therapy Type`<br>Measure: `AVG(Progress Score)` | `Therapy Type`, `Progress Score` | [`08_therapy_type_vs_progress.png`](../../evidence/visualizations/08_therapy_type_vs_progress.png) | High-Resolution Prototype & Specification |

---

## 4. Analytical Mapping Across Dashboards & Story Scenes

The 8 core visualizations integrate systematically into the higher-level project components:

### Integrated Dashboard Composition:
- **Header KPIs:** Derived aggregations from Visualizations 1, 2, 3, 6 (`COUNTD([User ID])`, `AVG([Anxiety Score])`, `AVG([Depression Score])`, `AVG([Daily Screen Time (hrs)])`).
- **Core Grid Panels:**
  - Panel 1: Stress Level Distribution (Vis 1)
  - Panel 2: Stress vs Anxiety & Depression (Combines Vis 2 & 3)
  - Panel 3: Sleep Quality vs Stress Tier (Vis 5)
  - Panel 4: Screen Time by Stress (Vis 6)
  - Panel 5: Mental Health History Distribution (Vis 7)
  - Panel 6: Ranked Therapy Efficacy (Vis 8)

### Guided Story Scene Integration:
- **Scene 1 (Baseline):** Incorporates Vis 1 + KPI Cards
- **Scene 2 (Psychological Symptoms):** Incorporates Vis 2 & 3
- **Scene 3 (Lifestyle Factors):** Incorporates Vis 5 & 6
- **Scene 4 (Vulnerability Factors):** Incorporates Vis 7 + Support System Breakdown
- **Scene 5 (Intervention Outcomes):** Incorporates Vis 8

---

## 5. Native Tableau Authoring Preparation

Each of the 8 visualizations has been validated for immediate worksheet replication in Tableau:
1. Drag the specified dimension(s) to **Columns** or **Rows** shelf.
2. Drag the measure(s) to **Rows** or **Columns** shelf, setting the aggregation to `AVG` or `COUNT`.
3. Apply standard color palettes (`#2c7bb6`, `#abd9e9`, `#fdae61`, `#d7191c`).
4. Enable mark labels for exact numerical callouts.
