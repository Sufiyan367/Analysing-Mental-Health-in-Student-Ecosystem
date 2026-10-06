# Dataset Validation Report

## 1. Executive Summary
This document records the programmatic quality assurance and schema validation for the dataset at `data/raw/mental_health_student_ecosystem.csv`. The audit guarantees that all 18 specified attributes adhere to strict data-type constraints, domain boundary limits, and relational consistency requirements.

* **Audit Timestamp:** October 6, 2026
* **Target File:** `data/raw/mental_health_student_ecosystem.csv`
* **Validation Script:** `scripts/validate_dataset.py`
* **Validation Outcome:** **PASSED (100% Valid, Zero Schema Violations)**

---

## 2. Quantitative Verification Metrics

| Validation Dimension | Specification Target | Observed Value | Status |
| :--- | :--- | :--- | :---: |
| **Total Rows** | $\ge 100$ (Preferred: 150–200) | **200** | **PASS** |
| **Total Columns** | Exactly 18 attributes | **18** | **PASS** |
| **Primary Key Uniqueness** | Zero duplicate `User ID`s | **0 duplicates (100% unique)** | **PASS** |
| **Missing / Null Values** | 0 nulls across all cells | **0 missing values (100% complete)** | **PASS** |
| **Data Types Conformity** | Exact numeric & categorical types | **100% Type compliant** | **PASS** |

---

## 3. Attribute Distribution & Numerical Boundary Audits

| Column Name | Data Type | Min | Max | Mean | Permissible Range |
| :--- | :--- | :-: | :-: | :-: | :-: |
| `Age` | Integer | 18 | 27 | 20.6 | 18 – 30 years |
| `Anxiety Score` | Integer | 5 | 96 | 52.6 | 0 – 100 points |
| `Depression Score` | Integer | 9 | 87 | 48.1 | 0 – 100 points |
| `Daily Screen Time (hrs)` | Float | 3.0 | 12.0 | 7.1 | 0.0 – 16.0 hours |
| `Social Interaction Score` | Integer | 1 | 10 | 5.6 | 1 – 10 points |
| `Intervention Duration (weeks)` | Integer | 0 | 16 | 3.1 | 0 – 24 weeks |
| `Progress Score` | Integer | 0 | 69 | 16.3 | 0 – 100 points |
| `Work-Life Balance Score` | Integer | 1 | 10 | 5.5 | 1 – 10 points |

---

## 4. Categorical Consistency & Domain Value Audit

* **`Gender`:** `['Female', 'Male', 'Other']`
* **`Occupation`:** `['Undergraduate Student', 'Graduate Teaching Assistant', 'Doctoral Researcher', 'Student Intern', 'Postgraduate Student']`
* **`Stress Level`:** `['Low', 'Medium', 'High']`
* **`Sleep Quality`:** `['Poor', 'Average', 'Good']`
* **`Physical Activity Level`:** `['Low', 'Moderate', 'High']`
* **`Mental Health History`:** `['Yes', 'No']`
* **`Therapy Type`:** `['CBT', 'Counseling', 'Meditation', 'Support Group', 'No Therapy']`
* **`Medication Usage`:** `['Yes', 'No']`
* **`Support System Strength`:** `['Low', 'Medium', 'High']`

---

## 5. Relational & Psychological Integrity Checks
* **Intervention Alignment:** Records with `Therapy Type = 'No Therapy'` have `Intervention Duration = 0` and `Progress Score = 0`.
* **Symptom Correlation:** High daily screen time and poor sleep quality correlate realistically with elevated `Stress Level`, `Anxiety Score`, and `Depression Score`.
* **Tableau Ready:** Standard column naming convention and clean categorical strings enable direct drag-and-drop analysis without requiring manual aliasing or type conversions.
