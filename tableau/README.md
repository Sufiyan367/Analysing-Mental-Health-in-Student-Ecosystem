# Tableau Visualizations & Dashboard Architecture

## Project: Analysing Mental Health in Student Ecosystem

This module documents the visual analytics blueprints, worksheet specifications, calculation formulas, and dashboard architectures designed for **Analysing Mental Health in Student Ecosystem**.

### Authoring Status & Packaged Workbook (.twbx)

> [!NOTE]
> **Production Packaged Tableau Workbook (.twbx) Available:**
>
> The verified native Tableau workbook package [`Analysing_Mental_Health_in_Student_Ecosystem.twbx`](Analysing_Mental_Health_in_Student_Ecosystem.twbx) is pre-configured with all 8 worksheets, the primary Executive Diagnostic Dashboard, and the 5-Scene Guided Data Story, bundling the complete source dataset [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](../data/cleaned/mental_health_student_ecosystem_cleaned.csv).
>
> You can open this `.twbx` directly in **Tableau Desktop / Tableau Public Desktop** and publish it to the authenticated author profile ([`sufiyan.surve`](https://public.tableau.com/app/profile/sufiyan.surve)).

---

### Primary Source Dataset
- **File:** [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](../data/cleaned/mental_health_student_ecosystem_cleaned.csv)
- **Cohort Size:** $N = 200$ university students
- **Validated Attributes:** 18 columns (0 missing values, 0 duplicate records)

---

### Worksheets Inventory (8 Verified Visualizations)

1. **Stress Level Distribution** — Vertical Bar Chart (`Stress Level` vs `COUNT([User ID])`).
2. **Stress Level vs Anxiety Score** — Vertical Bar Chart (`Stress Level` vs `AVG([Anxiety Score])`).
3. **Stress Level vs Depression Score** — Vertical Bar Chart (`Stress Level` vs `AVG([Depression Score])`).
4. **Mental Health Burden by Gender** — Grouped Bar Chart (`Gender` vs `AVG([Anxiety Score])`, `AVG([Depression Score])`).
5. **Sleep Quality vs Stress Level** — Stacked Bar Chart (`Sleep Quality` $\times$ `Stress Level`).
6. **Daily Screen Time vs Stress Level** — Vertical Bar Chart (`Stress Level` vs `AVG([Daily Screen Time (hrs)])`).
7. **Mental Health History Prevalence** — Donut / Pie Chart (`Mental Health History` vs `COUNT([User ID])`).
8. **Ranked Therapy Efficacy** — Horizontal Ranked Bar Chart (`Therapy Type` vs `AVG([Progress Score])`).

*Detailed visualization specifications and field mappings are documented in [`docs/data_visualization.md`](../docs/data_visualization.md).*

---

### Calculated Fields Specification (10 Production Formulas)

Full formulas and classification metadata are documented in [`docs/performance/calculation_fields.md`](../docs/performance/calculation_fields.md). Key examples:

1. **Stress High Flag:** `IF [Stress Level] = "High" THEN 1 ELSE 0 END`
2. **Active Therapy Flag:** `IF [Therapy Type] != "No Therapy" THEN 1 ELSE 0 END`
3. **Severe Distress Indicator:** `IF [Anxiety Score] >= 70 AND [Depression Score] >= 70 THEN 1 ELSE 0 END`
4. **Screen Time Category:** `IF [Daily Screen Time (hrs)] < 6.0 THEN "Low Screen" ELSEIF [Daily Screen Time (hrs)] <= 8.0 THEN "Moderate Screen" ELSE "High Screen" END`
5. **High Stress Poor Sleep Flag:** `IF [Stress Level] = "High" AND [Sleep Quality] = "Poor" THEN 1 ELSE 0 END`

---

### Interactive Dashboard Architecture

- **Desktop (1920×1080 / 16:9):** 4 cohort KPI cards (`Total Students`: 200, `Avg Anxiety`: 52.59, `Avg Depression`: 48.09, `Avg Screen Time`: 7.10 hrs) and 6 visual diagnostic panels.
- **Tablet (1024×768 / 2-Column):** Touch-optimized layout with collapsible filtering.
- **Mobile (Vertical Stack):** Single-column stacked layout optimized for mobile screens.
- **Visual Evidence:** [`evidence/dashboard/`](../evidence/dashboard/)
- **Documentation:** [`docs/dashboard_design.md`](../docs/dashboard_design.md)

---

### 5-Scene Guided Data Story

1. **Scene 1:** Student Mental Health Baseline
2. **Scene 2:** Stress and Psychological Symptoms
3. **Scene 3:** Lifestyle Factors and Stress
4. **Scene 4:** Vulnerability Factors and Support Systems
5. **Scene 5:** Intervention Patterns and Recovery Progress
- **Visual Evidence:** [`evidence/story/`](../evidence/story/)
- **Documentation:** [`docs/story.md`](../docs/story.md)

---

### Web Integration Container

The Python Flask web application (`app.py`) provides dynamic `<tableau-viz>` web components configured via environment variables:
- `TABLEAU_DASHBOARD_URL`: Configurable URL for published Tableau Dashboard.
- `TABLEAU_STORY_URL`: Configurable URL for published Tableau Story.
When URLs are left unset, the portal automatically displays high-resolution responsive prototypes with full metric cards.
