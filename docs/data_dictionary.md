# Data Dictionary & Dataset Documentation

## Dataset Metadata
* **Dataset Title:** Student Mental Health Survey Benchmark Dataset
* **Source:** Higher Education Student Mental Health Survey (Public Academic Repository / Kaggle Benchmark)
* **Source URL:** https://raw.githubusercontent.com/Jey-krishna/EDA-on-Student-Mental-Health-Analysis-Using-Python/main/Student%20Mental%20health.csv
* **Date Accessed:** October 6, 2026
* **Original Record Count:** 101 records
* **Original Feature Count:** 11 attributes
* **Format:** Comma-Separated Values (`.csv`)

---

## Variable Taxonomy

| Column Name in Raw Data | Cleaned Field Name | Data Type | Permissible Values / Range | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Timestamp` | `Timestamp` | DateTime | MM/DD/YYYY HH:MM | Timestamp when the survey response was recorded. |
| `Choose your gender` | `Gender` | String (Categorical) | `Female`, `Male` | Biological sex / gender identity of the respondent. |
| `Age` | `Age` | Integer | 18 – 24 | Age of the respondent in years (1 null in raw data, imputed with median). |
| `What is your course?` | `Course` | String (Categorical) | 49 course majors | Academic program or major enrolled in (standardized for case/spacing). |
| - | `Faculty` | String (Categorical) | `Engineering`, `IT & CS`, `Business`, `Science`, `Arts & Humanities`, `Law` | Derived grouping of individual majors into high-level academic faculties. |
| `Your current year of Study` | `Year_of_Study` | String (Ordinal) | `Year 1`, `Year 2`, `Year 3`, `Year 4` | Normalized academic progression standing of the student. |
| `What is your CGPA?` | `CGPA_Range` | String (Ordinal) | `0.00 - 1.99`, `2.00 - 2.49`, `2.50 - 2.99`, `3.00 - 3.49`, `3.50 - 4.00` | Cumulative Grade Point Average performance bracket. |
| - | `CGPA_Midpoint` | Float (Continuous) | 1.00 – 3.75 | Numerical midpoint of the CGPA bracket for mathematical trend calculations. |
| `Marital status` | `Marital_Status` | String (Binary) | `Yes`, `No` | Marital status indicator. |
| `Do you have Depression?` | `Depression` | String (Binary) | `Yes`, `No` | Self-reported clinical or symptomatic depression. |
| `Do you have Anxiety?` | `Anxiety` | String (Binary) | `Yes`, `No` | Self-reported anxiety disorder or persistent acute anxiety. |
| `Do you have Panic attack?` | `Panic_Attacks` | String (Binary) | `Yes`, `No` | Occurrence of panic attack episodes during the academic period. |
| `Did you seek any specialist for a treatment?` | `Sought_Treatment` | String (Binary) | `Yes`, `No` | Whether professional psychological or medical intervention was sought. |
| - | `Condition_Count` | Integer (Discrete) | 0 – 3 | Derived count of positive conditions (Depression + Anxiety + Panic Attacks). |
| - | `Risk_Category` | String (Ordinal) | `High Risk`, `Moderate Risk`, `Low Risk` | Derived risk tier based on co-occurring psychological conditions. |
| - | `Treatment_Gap_Flag` | String (Binary) | `Treatment Gap`, `Engaged with Care`, `No Serious Symptoms` | Flags students with high-risk symptoms who have NOT sought professional treatment. |

---

## Dataset Limitations & Ethics
1. **Self-Reported Nature:** Clinical conditions (Depression, Anxiety, Panic Attacks) are based on survey self-reporting rather than formal clinical diagnostic interviews.
2. **Sample Size:** 101 validated student responses representing a focused cross-sectional snapshot across degree programs.
3. **Anonymity & Privacy:** All records are fully de-identified and free of Personally Identifiable Information (PII) such as student IDs, names, or contact addresses.
