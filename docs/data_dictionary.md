# Data Dictionary: Student Mental Health Ecosystem Dataset

## 1. Dataset Overview
* **Dataset File:** `data/raw/mental_health_student_ecosystem.csv`
* **Domain:** Student Mental Health & Psychological Well-being Analytics
* **Target Audience:** Academic Counseling Centers, University Administrators, Health Services
* **Record Count:** 200 validated individual profiles
* **Feature Count:** 18 standardized variables
* **Dataset Type:** Cross-sectional psychological and lifestyle assessment benchmark modeled specifically for higher-education ecosystems and Tableau analytics.

---

## 2. Variable Dictionary & Schema Specifications

| # | Column Name | Data Type | Role | Permissible Values / Range | Description |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **1** | `User ID` | String (Text) | Dimension (Primary Key) | `STU_0001` to `STU_0200` | Unique alphanumeric identifier assigned to each participant; guarantees record individuality. |
| **2** | `Age` | Integer (Number) | Measure (Continuous) | 18 – 28 years | Age of the individual in completed years. |
| **3** | `Gender` | String (Text) | Dimension (Categorical) | `Female`, `Male`, `Other` | Self-reported gender identity of the student. |
| **4** | `Occupation` | String (Text) | Dimension (Categorical) | `Undergraduate Student`, `Postgraduate Student`, `Doctoral Researcher`, `Graduate Teaching Assistant`, `Student Intern` | Current academic role or research position within the university ecosystem. |
| **5** | `Stress Level` | String (Text) | Dimension (Ordinal) | `Low`, `Medium`, `High` | Categorical classification of chronic perceived academic and life stress. |
| **6** | `Anxiety Score` | Integer (Number) | Measure (Continuous) | 0 – 100 | Standardized numerical assessment score indicating anxiety severity (higher values denote elevated acute/chronic anxiety). |
| **7** | `Depression Score` | Integer (Number) | Measure (Continuous) | 0 – 100 | Standardized numerical score measuring severity of depressive symptoms. |
| **8** | `Sleep Quality` | String (Text) | Dimension (Ordinal) | `Poor`, `Average`, `Good` | Subjective sleep evaluation assessing duration, sleep onset latency, and daytime fatigue. |
| **9** | `Daily Screen Time (hrs)` | Float (Number) | Measure (Continuous) | 3.0 – 12.0 hours | Self-reported average daily hours engaged with digital screens (laptops, phones, tablets). |
| **10** | `Physical Activity Level` | String (Text) | Dimension (Ordinal) | `Low`, `Moderate`, `High` | Weekly level of intentional aerobic or muscular physical exercise. |
| **11** | `Social Interaction Score` | Integer (Number) | Measure (Continuous) | 1 – 10 | Psychometric index measuring frequency and perceived quality of interpersonal social connections. |
| **12** | `Mental Health History` | String (Text) | Dimension (Binary) | `Yes`, `No` | Indicates whether the individual has a diagnosed prior history of psychological disorders. |
| **13** | `Therapy Type` | String (Text) | Dimension (Categorical) | `CBT`, `Counseling`, `Meditation`, `Support Group`, `No Therapy` | Primary psychological or therapeutic intervention modality engaged. |
| **14** | `Intervention Duration (weeks)` | Integer (Number) | Measure (Discrete) | 0 – 16 weeks | Cumulative duration of active psychological therapy or clinical support. |
| **15** | `Progress Score` | Integer (Number) | Measure (Continuous) | 0 – 100 | Quantitative clinical improvement score observed following intervention (0 indicates unmanaged/no therapy). |
| **16** | `Medication Usage` | String (Text) | Dimension (Binary) | `Yes`, `No` | Indicates current prescription medication usage for psychiatric/mental health support. |
| **17** | `Support System Strength` | String (Text) | Dimension (Ordinal) | `Low`, `Medium`, `High` | Perceived availability and emotional responsiveness of family, peer, and institutional safety nets. |
| **18** | `Work-Life Balance Score` | Integer (Number) | Measure (Continuous) | 1 – 10 | Composite score evaluating ability to balance academic demands, personal well-being, and leisure. |

---

## 3. Structural Consistency & Analytical Design

1. **Behavioral Realism:** Variables maintain coherent epidemiological correlations. Students reporting high daily screen time and poor sleep quality demonstrate elevated anxiety and depression scores.
2. **Intervention Dynamics:** Non-zero `Intervention Duration` and positive `Progress Score` are strictly associated with active therapy modalities (`CBT`, `Counseling`, `Meditation`, `Support Group`), whereas `No Therapy` defaults to zero intervention weeks.
3. **Data Integrity:** Fully sanitized tabular extract with zero null values, zero duplicates, and uniform casing across all categorical labels.
