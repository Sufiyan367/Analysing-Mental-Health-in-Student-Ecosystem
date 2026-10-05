# Data Preprocessing, Imputation & Feature Engineering

## 1. Overview
The preprocessing pipeline transforms raw student survey responses into a structured, validated dataset ready for interactive visual analytics in Tableau Public and the web application.

---

## 2. Pipeline Execution Stages

### Stage 1: Ingestion & Schema Profiling
* **Input:** `data/raw/student_mental_health_raw.csv` (101 rows, 11 columns).
* **Column Renaming:** Mapped conversational questionnaire column titles into clean programming identifiers (`Timestamp`, `Gender`, `Age`, `Course`, `Year_of_Study`, `CGPA_Range`, `Marital_Status`, `Depression`, `Anxiety`, `Panic_Attacks`, `Sought_Treatment`).

### Stage 2: Data Cleaning & Hygiene
* **Whitespace Trimming:** Stripped leading and trailing whitespace across all string columns to resolve mismatched categories (e.g., `'3.50 - 4.00 '` vs `'3.50 - 4.00'`).
* **Missing Value Imputation:**
  - `Age` contained 1 null record.
  - Imputed using the median student age ($19$ years) preserving integer data integrity.
* **Casing Normalization:**
  - `Gender`: Standardized to Title Case (`Female`, `Male`).
  - `Year_of_Study`: Standardized casing variants (`year 1`, `Year 1`, etc.) into four uniform categorical factors: `Year 1`, `Year 2`, `Year 3`, `Year 4`.

### Stage 3: Categorical & Ordinal Standardization
* **CGPA Standardization & Midpoint Mapping:**
  - Normalized range labels: `0.00 - 1.99`, `2.00 - 2.49`, `2.50 - 2.99`, `3.00 - 3.49`, `3.50 - 4.00`.
  - Computed continuous `CGPA_Midpoint` values ($1.00$, $2.25$, $2.75$, $3.25$, $3.75$) to enable correlation analysis and trend lines in Tableau.
* **Academic Course & Faculty Grouping:**
  - 49 distinct raw course responses categorized into 6 core faculty groups:
    1. *Engineering* (Mechanical, Civil, KOE)
    2. *IT & Computer Science* (BIT, BCS, Computer Science)
    3. *Law*
    4. *Business & Economics* (KENMS, Accounting, Banking)
    5. *Humanities & Social Sciences* (Islamic Studies, Communication, Psychology)
    6. *Health & Natural Sciences* (Biomedical, Nursing, Pharmacy, Science)

### Stage 4: Feature Engineering
* **Binary Condition Indicators:** Generated $0/1$ numeric encodings for:
  - `Depression_Binary`
  - `Anxiety_Binary`
  - `Panic_Binary`
  - `Treatment_Binary`
* **Condition Count:** Aggregated metric:
  $$\text{Condition\_Count} = \text{Depression\_Binary} + \text{Anxiety\_Binary} + \text{Panic\_Binary} \quad (\text{Range: } 0 - 3)$$
* **Risk Categorization:**
  - `High Risk`: 2 or 3 co-occurring conditions (28 students, $27.7\%$).
  - `Moderate Risk`: 1 condition (36 students, $35.6\%$).
  - `Low Risk`: 0 conditions (37 students, $36.6\%$).
* **Treatment Gap Diagnosis:**
  - Identified students in `High Risk` who have `Sought_Treatment = No`.
  - Found that **22 out of 28 High-Risk students ($78.6\%$)** have never accessed professional mental health services, representing a critical institutional care gap.

---

## 3. Validation Audit & Data Summary

| Metric | Raw Dataset | Cleaned Dataset |
| :--- | :--- | :--- |
| **Row Count** | 101 | 101 |
| **Column Count** | 11 | 20 |
| **Missing Values** | 1 (in `Age`) | 0 (fully imputed) |
| **Duplicate Rows** | 0 | 0 |
| **Data Types** | 1 Float, 10 Object | 1 Int, 5 Float/Int Derived, 14 Object/Category |
| **Integrity Checks** | Inconsistent strings | Standardized schema verified |
| **Output File** | `data/raw/student_mental_health_raw.csv` | `data/cleaned/student_mental_health_cleaned.csv` |
