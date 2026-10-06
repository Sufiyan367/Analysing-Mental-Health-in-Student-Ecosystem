# Web Integration Report: Flask Portal & Tableau Embedding

**Project:** Analysing Mental Health in Student Ecosystem  
**SkillWallet Epic:** Web Integration  
**Tasks Completed:**  
1. Publishing Assessment & Embedding Architecture  
2. Web Integration of Dashboard and Story  
**Source of Truth:** [`data/cleaned/mental_health_student_ecosystem_cleaned.csv`](../data/cleaned/mental_health_student_ecosystem_cleaned.csv) ($N=200$, 18 columns)  
**Evidence Artifacts:** [`evidence/web_integration/`](../evidence/web_integration/)  

---

## 1. Executive Summary

This report establishes the **Web Integration and Cloud Embedding architecture** for the capstone project **Analysing Mental Health in Student Ecosystem**.

The web application is built with **Python Flask** and **Jinja2**, serving a responsive analytics portal that unifies:
1. **Executive Cohort Diagnostics:** Real-time summary KPIs computed directly from the validated 200-student dataset.
2. **Interactive Analytical Dashboards:** A multi-device visual interface supporting both live Tableau Public cloud embedding and high-resolution responsive prototype fallbacks (Desktop 1920×1080, Tablet 1024×768, Mobile).
3. **5-Scene Guided Data Story:** An interactive narrative carousel allowing stakeholders to step through the student mental health journey from baseline diagnostics to institutional recovery outcomes.
4. **Methodology & Architectural Specifications:** Detailed documentation of the 18-variable schema, 10 calculated fields, and 8 unique visualizations.

---

## 2. Web Application Architecture & Routes

The Flask web application is structured with zero external template dependencies and full mobile responsiveness:

| Route | HTTP Method | Page Title / Purpose | Active Content & Dynamic Features | Validation Status |
| :--- | :---: | :--- | :--- | :---: |
| `/` | `GET` | **Executive Overview** | Displays 4 primary cohort KPIs ($N=200$, Anxiety $52.59$, Depression $48.09$, Screen Time $7.10\text{ hrs}$), subgroup badges (High Stress $24.5\%$, Active Therapy $46.5\%$), and 4 analytical research pillars. | **HTTP 200 OK** |
| `/dashboard` | `GET` | **Analytical Dashboards** | Implements the Tableau embedding container. If `TABLEAU_DASHBOARD_URL` is set, embeds the live interactive workbook; otherwise, renders the verified multi-device prototype with a Desktop/Tablet/Mobile layout switcher and panel guide. | **HTTP 200 OK** |
| `/story` | `GET` | **Guided Data Story** | Implements the Tableau Story embedding container. Features an interactive 5-scene navigator displaying verified visual evidence (`01_baseline.png` to `05_intervention_and_progress.png`), observations, transitions, and policy recommendations. | **HTTP 200 OK** |
| `/about` | `GET` | **Methodology & Specs** | Complete technical reference including the 18-variable schema table, 10 calculation formulas, and SkillWallet compliance audit. | **HTTP 200 OK** |
| `/evidence/<path>` | `GET` | **Static Asset Delivery** | Serves high-resolution visual evidence artifacts and prototypes directly from the project's evidence directory. | **HTTP 200 OK** |

---

## 3. Tableau Embedding Mechanism & Configuration

### A. Embedding Standards
The application integrates Tableau's modern **Embedding API v3** via the `<tableau-viz>` web component:
```html
<tableau-viz id="tableauDashboardViz" 
             src="{{ tableau_dashboard_url }}" 
             toolbar="bottom" 
             hide-tabs>
</tableau-viz>
```
Script reference is bundled globally in the base layout:
```html
<script type="module" src="https://public.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js"></script>
```

### B. Environment Variable Configuration
To decouple application logic from cloud publication status, embed URLs are read from environment variables:
- `TABLEAU_DASHBOARD_URL`: Full URL of the published Tableau Public dashboard view (e.g. `https://public.tableau.com/views/AnalysingMentalHealthinStudentEcosystem/Dashboard`).
- `TABLEAU_STORY_URL`: Full URL of the published Tableau Public story view (e.g. `https://public.tableau.com/views/AnalysingMentalHealthinStudentEcosystem/Story`).
- `TABLEAU_PROFILE_URL`: Verified Tableau Public author profile: [`sufiyansurve333`](https://public.tableau.com/app/profile/sufiyansurve333).

### C. Graceful Fallback Strategy
When `TABLEAU_DASHBOARD_URL` or `TABLEAU_STORY_URL` are not set (pending cloud publication):
- A polite, informative banner notifies users that live cloud embedding is configured and awaiting URL injection.
- The interface immediately falls back to high-resolution visual prototypes and the interactive 5-scene narrative browser without broken frames, spinners, or missing assets.

---

## 4. Tableau Public Publishing Status & Blockers

> [!IMPORTANT]
> **Academic Integrity Notice:**  
> In accordance with strict guidelines, no synthetic `.twb`/`.twbx` files were hand-coded, and no fake Tableau Public URLs were fabricated.

### Automated Publishing Assessment:
- **Tableau Public Web Authoring:** Tableau Public Web Authoring (`https://public.tableau.com/app/create`) requires interactive user DOM events (drag-and-drop field placement on Shelves, canvas coordinate mapping, modal file pickers) that cannot be reliably operated via headless automation without risking user session corruption.
- **Tableau Free-Tier API Restrictions:** Tableau Public does not support direct workbook publishing via REST API for free accounts.
- **Current Status:** Automated background publication was stopped honestly. The application is **100% prepared** to receive the published URLs as soon as manual workbook authoring is performed.

---

## 5. Local Validation & Screenshot Evidence

The Flask web application was validated locally using high-resolution headless Chromium via Playwright:

| Route Tested | HTTP Status | Response Size | Rendered Title | Evidence File |
| :--- | :---: | :---: | :--- | :--- |
| `http://127.0.0.1:5055/` | **200 OK** | $9.7\text{ KB}$ | Executive Overview — Analysing Mental Health in Student Ecosystem | [`evidence/web_integration/home_page.png`](../evidence/web_integration/home_page.png) |
| `http://127.0.0.1:5055/dashboard` | **200 OK** | $8.6\text{ KB}$ | Interactive Dashboards — Analysing Mental Health in Student Ecosystem | [`evidence/web_integration/dashboard_page.png`](../evidence/web_integration/dashboard_page.png) |
| `http://127.0.0.1:5055/story` | **200 OK** | $13.6\text{ KB}$ | Guided Data Story — Analysing Mental Health in Student Ecosystem | [`evidence/web_integration/story_page.png`](../evidence/web_integration/story_page.png) |
| `http://127.0.0.1:5055/about` | **200 OK** | $10.8\text{ KB}$ | Methodology & Architecture — Analysing Mental Health in Student Ecosystem | [`evidence/web_integration/about_page.png`](../evidence/web_integration/about_page.png) |

All 4 routes executed with zero console errors, complete styling, active navigation bar highlighting, and responsive image scaling.

---

## 6. Exact Remaining Manual Step

To complete live Tableau Public cloud embedding:
1. Open [`https://public.tableau.com/app/create`](https://public.tableau.com/app/create) in your authenticated browser.
2. Click **Upload from computer** and select `data/cleaned/mental_health_student_ecosystem_cleaned.csv`.
3. Add the 10 calculation fields specified in [`docs/performance/calculation_fields.md`](performance/calculation_fields.md).
4. Build the worksheets according to [`docs/performance/visualization_inventory.md`](performance/visualization_inventory.md).
5. Assemble the dashboard and story according to [`docs/dashboard_design.md`](dashboard_design.md) and [`docs/story.md`](story.md).
6. Click **File > Publish As** to publish the workbook to your account `sufiyansurve333`.
7. Copy the published share URLs and set them in your environment:
   ```bash
   set TABLEAU_DASHBOARD_URL="https://public.tableau.com/views/<Workbook>/Dashboard"
   set TABLEAU_STORY_URL="https://public.tableau.com/views/<Workbook>/Story"
   ```
8. Restart Flask (`python app.py`) — the web application will automatically switch to live embedded Tableau views!
