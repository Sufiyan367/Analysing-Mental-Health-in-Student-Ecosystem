# Project Public Demonstration & Deployment Architecture

## Project: Analysing Mental Health in Student Ecosystem
**Repository:** [`https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem`](https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem)  
**Public Demo URL (GitHub Pages):** [`https://sufiyan367.github.io/Analysing-Mental-Health-in-Student-Ecosystem/`](https://sufiyan367.github.io/Analysing-Mental-Health-in-Student-Ecosystem/)  
**Local Backend Application (Flask):** `http://127.0.0.1:5000`

---

## 1. Public Project Demo Architecture (GitHub Pages)

To fulfill the SkillWallet "Demo URL" requirement without introducing paid cloud infrastructure, browser tunneling, or unauthenticated services, a polished static presentation is hosted natively via **GitHub Pages**:

- **Hosting Platform:** GitHub Pages (Static Web Hosting)
- **Source Branch & Directory:** `main` branch, `/docs` directory
- **Entrypoint:** [`docs/index.html`](index.html)
- **Assets Directory:** [`docs/evidence/`](evidence/) (complete mirrors of high-resolution dashboard, story, and visualization assets)
- **Deployment Status:** **LIVE & PUBLICLY ACCESSIBLE**
- **Public Endpoint:** [`https://sufiyan367.github.io/Analysing-Mental-Health-in-Student-Ecosystem/`](https://sufiyan367.github.io/Analysing-Mental-Health-in-Student-Ecosystem/)

### Features of the Public Showcase:
1. **Interactive Executive KPIs:** 200 cohort records, Avg Anxiety 52.59, Avg Depression 48.09, Avg Screen Time 7.10 hrs.
2. **Dashboard Architecture Preview:** High-resolution desktop dashboard layout ([`docs/evidence/dashboard/desktop_dashboard.png`](evidence/dashboard/desktop_dashboard.png)) with layout specifications.
3. **5-Scene Guided Data Story:** Full visual scenes and clinical findings:
   - Scene 1: Baseline Stress Spread ([`docs/evidence/story/01_baseline.png`](evidence/story/01_baseline.png))
   - Scene 2: Symptom Surges ([`docs/evidence/story/02_psychological_symptoms.png`](evidence/story/02_psychological_symptoms.png))
   - Scene 3: Lifestyle Deficits ([`docs/evidence/story/03_lifestyle_and_stress.png`](evidence/story/03_lifestyle_and_stress.png))
   - Scene 4: Vulnerability & Peer Buffer ([`docs/evidence/story/04_vulnerability_and_support.png`](evidence/story/04_vulnerability_and_support.png))
   - Scene 5: Intervention Efficacy ([`docs/evidence/story/05_intervention_and_progress.png`](evidence/story/05_intervention_and_progress.png))
4. **Key Empirical Takeaways:** Four core diagnostic insights derived directly from the verified dataset.
5. **Project Methodology & Schema:** Complete 18-variable domain specification and integrity audit.
6. **Direct Media & Report Links:** Links to the 6:26 MP4 demonstration video, printable PDF report, and GitHub source code.

---

## 2. Local Full-Stack Backend (Python Flask)

The full-stack Flask application remains available for local execution and development:

- **Local Endpoint:** `http://127.0.0.1:5000`
- **Execution Command:** `python app.py`
- **WSGI Specification:** `gunicorn app:app` (configured in [`requirements.txt`](../requirements.txt) and [`render.yaml`](../render.yaml))
- **Production Status:** Localhost-only (not publicly exposed)

### Verified Local Routes (100% HTTP 200 OK):
- `GET /` — Executive Overview & live KPI computations
- `GET /dashboard` — Multi-device responsive dashboard switcher
- `GET /story` — 5-scene guided narrative carousel
- `GET /about` — Technical data dictionary and schema documentation
- `GET /evidence/<path>` — Direct evidence asset delivery

---

## 3. Tableau Public Cloud Status & Transparency

> [!IMPORTANT]
> **Native Tableau Cloud Status: PENDING MANUAL GUI AUTHORING**
>
> In accordance with academic honesty principles, all Tableau worksheets (8 unique charts), calculated fields (10 formulas), responsive layouts, and story narrative steps are fully specified and prototyped in Python and Flask.
>
> Native Tableau Public workbook publication remains pending manual creation in the authenticated author session on profile [`sufiyansurve333`](https://public.tableau.com/app/profile/sufiyansurve333).
>
> Neither the GitHub Pages static showcase nor the Flask backend fabricate active Tableau Cloud URLs until real publication is executed.
