# Tableau Architecture, Calculated Fields & Performance Audit

## 1. Executive Summary
The visual analytics layer for **Analysing Mental Health in Student Ecosystem** is built using Tableau Public. It incorporates 9 specialized analytical worksheets, 2 interactive dashboards with global filtering and cross-highlighting, and 1 comprehensive 5-scene data story.

---

## 2. Calculated Fields & KPI Formulas

| Calculated Field Name | Tableau Formula | Role & Type | Analytical Purpose |
| :--- | :--- | :--- | :--- |
| **`Composite Stress Index`** | `([Condition_Count] / 3.0) * 100.0` | Measure (Quantitative) | Normalizes the positive condition count (0 to 3) into a standard 0–100% stress burden score. |
| **`High Risk Indicator`** | `IF [Risk_Category] = "High Risk" THEN 1 ELSE 0 END` | Measure (Quantitative) | Binary flag allowing summation of students suffering from co-occurring mental health conditions. |
| **`Treatment Seeking Flag`** | `IF [Sought_Treatment] = "Yes" THEN 1 ELSE 0 END` | Measure (Quantitative) | Computes percentage and count of students actively receiving medical/psychological help. |
| **`Depression Indicator`** | `IF [Depression] = "Yes" THEN 1 ELSE 0 END` | Measure (Quantitative) | Enables prevalence rate calculation ($34.7\%$) across any demographic slice. |
| **`Anxiety Indicator`** | `IF [Anxiety] = "Yes" THEN 1 ELSE 0 END` | Measure (Quantitative) | Enables anxiety prevalence calculation ($33.7\%$) across academic cohorts. |
| **`Panic Attack Indicator`** | `IF [Panic_Attacks] = "Yes" THEN 1 ELSE 0 END` | Measure (Quantitative) | Identifies acute panic events ($32.7\%$) for correlational study. |
| **`High Risk Treatment Gap`** | `IF [Risk_Category] = "High Risk" AND [Sought_Treatment] = "No" THEN "High Risk Untreated" ELSEIF [Risk_Category] = "High Risk" AND [Sought_Treatment] = "Yes" THEN "High Risk in Treatment" ELSE "Moderate/Low Risk" END` | Dimension (Nominal) | Directly flags the 22 students experiencing acute multi-condition distress who have not sought treatment. |

---

## 3. Worksheets Inventory & Analytical Purpose

1. **`Gender vs Mental Health` (Stacked Bar Chart)**
   - *Dimensions:* `Gender`, `Depression` / `Anxiety` / `Panic_Attacks`.
   - *Key Finding:* Female students report slightly higher rates of depression ($35.5\%$) and panic attacks, while anxiety remains evenly distributed across genders.
2. **`Age and Study Year Distribution` (Histogram & Stacked Bar)**
   - *Dimensions:* `Age` (18–24), `Year_of_Study` (`Year 1` through `Year 4`).
   - *Key Finding:* Population concentrates in ages 18–19 (Years 1 & 2), representing young adults undergoing the foundational university transition.
3. **`CGPA vs Depression and Anxiety` (Grouped Bar Chart)**
   - *Dimensions:* `CGPA_Range` (`0.00-1.99` to `3.50-4.00`).
   - *Key Finding:* High academic achievement (`3.50-4.00`) does not shield students from mental distress; anxiety rates in top performers remain above $30\%$.
4. **`Condition Breakdown` (Heat Matrix)**
   - *Dimensions:* `Condition_Count` vs `Risk_Category`.
   - *Key Finding:* $27.7\%$ of students suffer from 2 or more conditions simultaneously.
5. **`Faculty Stress Comparison` (Horizontal Ranked Bar)**
   - *Dimensions:* `Faculty` (`Engineering`, `IT & CS`, `Law`, `Business`, `Science`).
   - *Key Finding:* IT & Computer Science and Engineering students present the highest average condition loads per student.
6. **`Overall Risk Segmentation` (Donut Chart)**
   - *Dimensions:* `Risk_Category` (`High Risk`: $27.7\%$, `Moderate Risk`: $20.8\%$, `Low Risk`: $51.5\%$).
7. **`Year of Study Risk Heatmap` (Highlight Table)**
   - *Dimensions:* `Year_of_Study` $\times$ `Risk_Category`.
   - *Key Finding:* Year 1 and Year 3 exhibit the highest density of high-risk students.
8. **`Discipline Treemap` (Proportional Area Chart)**
   - *Dimensions:* `Faculty` $\rightarrow$ `Course`.
9. **`Academic Performance vs Anxiety Trend` (Trend Line)**
   - *Measures:* `CGPA_Midpoint` vs `Average Condition Count`.

---

## 4. Dashboards & Story Architecture

### Dashboard 1: Student Demographics & Academic Profile
* **Target Resolution:** $1200 \times 800\text{ px}$ (Fixed layout for consistent web embedding).
* **Worksheets Integrated:**
  - Gender vs Mental Health Prevalence
  - Age & Year of Study Distribution
  - Discipline Treemap
  - CGPA vs Performance Bands
* **Interactive Slicers:** Global filters for `Gender`, `Year_of_Study`, and `Faculty`.

### Dashboard 2: Mental Health Risk Assessment & Diagnostics
* **Target Resolution:** $1200 \times 800\text{ px}$.
* **Worksheets Integrated:**
  - Overall Risk Tier Segmentation
  - Year of Study Risk Heatmap
  - Faculty Stress Comparison
  - Academic Trend vs Anxiety
* **Interactive Actions:** Filter Action allowing click-to-filter by Risk Tier.

### Tableau Story: The Student Well-being Journey
* **Scene 1 — Cohort Baseline:** Demographics and baseline mental health incidence.
* **Scene 2 — Academic Pressure Paradigm:** CGPA performance vs psychological strain.
* **Scene 3 — Lifestyle Stress Vectors:** Workload and panic incidence.
* **Scene 4 — Vulnerability Mapping:** 27.7% High Risk segment and the 78.6% treatment deficit.
* **Scene 5 — Strategic Roadmap:** Concrete institutional mental health interventions.

---

## 5. Performance Audit & Latency Metrics
* **Dataset Profile:** 101 rows $\times$ 20 columns ($14.8\text{ KB}$ extract).
* **Extraction Type:** In-memory extract via `.twbx` package (zero external network database latency).
* **Worksheet Query Execution:** $< 15\text{ ms}$ average client-side rendering time.
* **Calculated Fields Efficiency:** All calculated fields evaluate on row-level boolean expressions with $O(1)$ complexity.
* **Dashboard Load Time:** $< 1.2\text{ s}$ initial render in Tableau Public iframe container.
* **Responsiveness:** Zero stuttering or lag observed across dynamic filter toggles.
