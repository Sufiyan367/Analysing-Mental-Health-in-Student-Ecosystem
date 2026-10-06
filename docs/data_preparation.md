# Data Preparation for Visualization

## 1. Overview
This document records the **Data Preparation** phase of the **Analysing Mental Health in Student Ecosystem** project (Course: *Data Analytics with Tableau*, SkillWallet / SmartBridge).

The goal of this phase is to evaluate, audit, and certify that the cleaned dataset meets all structural, typological, and psychometric requirements for dashboard authoring and visual analytics in Tableau.

**Cleaned Dataset Path:** `data/cleaned/mental_health_student_ecosystem_cleaned.csv`  
**Machine-Readable Summary:** `data/cleaned/validation_summary.json`  

---

## 2. Dataset Validation & Integrity Audit

A comprehensive validation of the dataset was conducted with zero modifications required:

| Criterion | Target Requirement | Audit Finding | Result |
| :--- | :--- | :--- | :--- |
| **Row Count** | $\ge 100$ records (150–200 preferred) | **200 rows** | **PASSED** |
| **Column Count** | Exactly 18 schema variables | **18 columns** | **PASSED** |
| **Missing Values** | 0 nulls across all fields | **0 nulls (100% complete)** | **PASSED** |
| **Blank / Whitespace Values**| 0 blank strings | **0 blanks** | **PASSED** |
| **Primary Key Uniqueness** | Unique `User ID` (`STU_0001` - `STU_0200`) | **0 duplicates (200 unique)** | **PASSED** |
| **Data Types** | Typed properly for numerical/categorical | **10 categorical/string, 8 numerical** | **PASSED** |
| **Value Consistency** | Category names clean & standardized | **Consistent labels across all records** | **PASSED** |

### Data Transformations and Cleaning Note:
> **"No further data cleaning was required; the dataset is visualization-ready."**  
> All 200 rows and 18 columns have been retained intact without alterations, deletions, or synthetic distortions.

---

## 3. Dimensional & Measure Classification for Tableau

To streamline authoring in Tableau, variables are classified into categorical **Dimensions** and quantitative **Measures**:

### Dimensions (Categorical / Discrete Attributes)
1. **User ID** (`String` / Nominal): Unique participant identifier (`STU_0001` to `STU_0200`). Serves as level-of-detail key.
2. **Gender** (`String` / Nominal): `Female` (98), `Male` (94), `Other` (8).
3. **Occupation** (`String` / Nominal): Academic role across the student ecosystem:
   - `Undergraduate Student` (103)
   - `Postgraduate Student` (41)
   - `Student Intern` (24)
   - `Graduate Teaching Assistant` (17)
   - `Doctoral Researcher` (15)
4. **Stress Level** (`String` / Ordinal): Perceived stress tier: `Medium` (107), `High` (49), `Low` (44).
5. **Sleep Quality** (`String` / Ordinal): Self-reported sleep restfulness: `Average` (89), `Poor` (66), `Good` (45).
6. **Physical Activity Level** (`String` / Ordinal): Weekly physical exercise level: `Low` (86), `Moderate` (80), `High` (34).
7. **Mental Health History** (`String` / Nominal): Prior history of mental health challenges: `No` (120), `Yes` (80).
8. **Therapy Type** (`String` / Nominal): Modality of therapeutic intervention:
   - `No Therapy` (107)
   - `Counseling` (35)
   - `Meditation` (28)
   - `CBT` (20)
   - `Support Group` (10)
9. **Medication Usage** (`String` / Nominal): Active psychiatric medication: `No` (182), `Yes` (18).
10. **Support System Strength** (`String` / Ordinal): Level of social/familial network support: `Medium` (103), `Low` (52), `High` (45).

### Measures (Continuous / Discrete Quantitative Metrics)
1. **Age** (`Integer`): Participant age in years (Range: `18` to `27`, Mean: `20.61`, Std: `2.02`).
2. **Anxiety Score** (`Integer`): Standardized anxiety psychometric assessment (Range: `5` to `96`, Mean: `52.59`, Std: `16.77`).
3. **Depression Score** (`Integer`): Standardized depression severity metric (Range: `9` to `87`, Mean: `48.09`, Std: `16.65`).
4. **Daily Screen Time (hrs)** (`Float`): Daily digital screen usage (Range: `3.0` to `12.0` hrs, Mean: `7.10`, Std: `1.81`).
5. **Social Interaction Score** (`Integer`): Scale of interpersonal social engagement (Range: `1` to `10`, Mean: `5.55`, Std: `2.00`).
6. **Intervention Duration (weeks)** (`Integer`): Duration in active therapy (Range: `0` to `16` weeks, Mean: `3.10`, Std: `3.90`). *(Zero for students receiving No Therapy; Mean for active therapy = 6.67 weeks)*.
7. **Progress Score** (`Integer`): Post-intervention recovery/improvement score (Range: `0` to `69`, Mean: `16.32`, Std: `19.87`). *(Zero for students receiving No Therapy; Mean for active therapy = 35.10)*.
8. **Work-Life Balance Score** (`Integer`): Self-rated balance between study, work, and personal life (Range: `1` to `10`, Mean: `5.47`, Std: `2.28`).

---

## 4. Evaluated Analytical Relationships

The dataset exhibits strong, realistic psychometric correlations, making it well-suited for interactive dashboard storytelling:

1. **Stress Level vs. Anxiety & Depression Scores:**
   - `High` Stress: Mean Anxiety = **72.06**, Mean Depression = **68.78**
   - `Medium` Stress: Mean Anxiety = **52.85**, Mean Depression = **47.37**
   - `Low` Stress: Mean Anxiety = **30.27**, Mean Depression = **26.80**
2. **Daily Screen Time vs. Stress Level:**
   - Students with `High` stress average **8.12 hrs/day** screen time, compared to **7.07 hrs/day** for `Medium` and **6.00 hrs/day** for `Low` stress.
3. **Sleep Quality vs. Stress Level:**
   - 71.4% (35 of 49) of students with `High` stress suffer from `Poor` sleep, whereas only 2.3% (1 of 44) of `Low` stress students experience poor sleep.
4. **Physical Activity vs. Stress Level:**
   - 75.5% (37 of 49) of students in the `High` stress group have `Low` physical activity.
5. **Therapy Modalities vs. Progress Score:**
   - Among students undergoing therapy ($n=93$), `CBT` yielded the highest average progress score (**40.80**), followed by `Counseling` (**34.43**), `Support Group` (**33.10**), and `Meditation` (**32.57**).
6. **Work-Life Balance vs. Stress Level:**
   - High stress corresponds to an average balance score of **2.82 / 10**, while low stress students report **8.25 / 10**.

---

## 5. Recommended Tableau Visualizations

Based on the validated dimensions and measures, the following 9 worksheets are targeted for implementation:

| Worksheet | Chart Type | Dimensions & Measures | Analytical Objective |
| :--- | :--- | :--- | :--- |
| **WS 1: Stress vs Anxiety & Depression** | Grouped Bar Chart / Box Plot | Dimension: `Stress Level`<br>Measures: `AVG(Anxiety Score)`, `AVG(Depression Score)` | Display symptom escalation across stress tiers. |
| **WS 2: Screen Time vs Stress Distribution** | Box-and-Whisker Plot / Histogram | Dimension: `Stress Level`<br>Measure: `Daily Screen Time (hrs)` | Highlight screen time saturation among high-stress students. |
| **WS 3: Sleep Quality & Physical Activity Matrix** | Heatmap / Highlight Table | Dimensions: `Sleep Quality`, `Physical Activity Level`<br>Measure: `COUNT(User ID)` / `AVG(Stress Level)` | Showcase the compounding effect of lifestyle habits on well-being. |
| **WS 4: Therapy Efficacy & Progress** | Bar Chart with Reference Line | Dimension: `Therapy Type` (filtered $>0$)<br>Measure: `AVG(Progress Score)` | Compare effectiveness of CBT, Counseling, and Meditation. |
| **WS 5: Intervention Duration vs Progress** | Scatter Plot with Trendline | Measures: `Intervention Duration (weeks)` vs `Progress Score`<br>Dimension: `Therapy Type` | Assess duration-response relationship of mental health interventions. |
| **WS 6: Academic Role Vulnerability** | Horizontal Bar Chart | Dimension: `Occupation`<br>Measures: `AVG(Anxiety Score)`, `AVG(Work-Life Balance)` | Identify high-risk student cohorts (e.g., Doctoral Researchers, Interns). |
| **WS 7: Support System Impact** | Stacked Bar Chart | Dimensions: `Support System Strength`, `Stress Level`<br>Measure: `COUNT(User ID)` | Quantify how peer and familial support buffers severe stress. |
| **WS 8: Medication Usage & History** | Dual-axis / Grouped Column | Dimensions: `Mental Health History`, `Medication Usage`<br>Measure: `AVG(Depression Score)` | Analyze clinical engagement vs distress severity. |
| **WS 9: Holistic Well-Being Profile** | Scatter Plot / Bubble Matrix | Measures: `Social Interaction Score` vs `Work-Life Balance Score`<br>Color: `Stress Level` | Multi-variable landscape of student wellness. |

---

## 6. Derived Analysis Fields (Optional Tableau Calculated Fields)

No irreversible CSV alterations were made. The following calculated fields are recommended for definition natively in Tableau:

1. **`Therapy Status`**:
   ```sql
   IF [Therapy Type] = 'No Therapy' THEN 'Unenrolled' ELSE 'Active Intervention' END
   ```
2. **`High Risk Flag`**:
   ```sql
   IF [Anxiety Score] >= 70 AND [Depression Score] >= 65 THEN 'High Clinical Risk' ELSE 'Moderate/Low Risk' END
   ```
3. **`Screen Time Category`**:
   ```sql
   IF [Daily Screen Time (hrs)] < 5.0 THEN 'Low (<5 hrs)'
   ELSEIF [Daily Screen Time (hrs)] <= 8.0 THEN 'Moderate (5-8 hrs)'
   ELSE 'Heavy (>8 hrs)' END
   ```

---

## 7. Final Readiness Status

**STATUS: READY FOR VISUALIZATION**

- Total Rows Inspected: `200`
- Rows Removed: `0`
- Values Changed: `0`
- The dataset file `data/cleaned/mental_health_student_ecosystem_cleaned.csv` is fully verified, complete, and prepared for direct upload into Tableau Public Web Authoring.
