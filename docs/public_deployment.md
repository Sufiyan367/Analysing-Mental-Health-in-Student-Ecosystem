# Flask Demo Deployment & Local Server Verification Report

## Project: Analysing Mental Health in Student Ecosystem
**Repository:** [`https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem`](https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem)  
**Framework:** Python Flask 3.0.3 with WSGI Gunicorn 21+  
**Target Platform:** [Render](https://render.com) (Native Python Web Service)

---

## 1. Local Server Status (Verified Running)

The application is actively running and accessible locally:

- **Local URL:** [`http://127.0.0.1:5000`](http://127.0.0.1:5000)
- **Local Host Address:** `0.0.0.0:5000`
- **Execution Mode:** Production-style (`debug=False`), dynamically bound to `$PORT` (default: `5000`)
- **Status:** **ACTIVE & OPERATIONAL** (Background Daemon Process)

### Verified Route Results (All HTTP 200 OK)

| Route | Status | Page Title | Verified Content & Assets |
| :--- | :---: | :--- | :--- |
| `/` | **HTTP 200** | *Executive Overview — Analysing Mental Health in Student Ecosystem* | Renders 4 primary cohort KPIs ($N=200$, Anxiety $52.59$, Depression $48.09$, Screen Time $7.10\text{ hrs}$), CSS Grid layout, and 4 diagnostic research pillars. |
| `/dashboard` | **HTTP 200** | *Interactive Dashboards — Analysing Mental Health in Student Ecosystem* | Renders multi-device layout switcher (Desktop, Tablet, Mobile) and responsive prototype panels; `<tableau-viz>` container ready. |
| `/story` | **HTTP 200** | *Guided Data Story — Analysing Mental Health in Student Ecosystem* | Renders 5-scene narrative carousel with previous/next controls, clinical observations, and campus policy recommendations. |
| `/about` | **HTTP 200** | *Methodology & Architecture — Analysing Mental Health in Student Ecosystem* | Renders 18-variable schema dictionary table, 10 calculation formulas, and validation report. |
| `/evidence/<path>` | **HTTP 200** | Static Asset Delivery | Successfully serves charts (`01_stress_level_distribution.png`), prototypes (`student_mental_health_dashboard.png`, `01_baseline.png`), and the 6:26 MP4 demonstration video. |

---

## 2. Public Hosting Status & Exact Blocker Analysis

- **Public Hosting Status:** **PENDING MANUAL 1-CLICK AUTHORIZATION**
- **Public URL Status:** Currently unassigned / 404 until authorized on Render's web portal.
- **Exact Blocker:**
  - Automated cloud deployment requires authenticated credentials (e.g., Render API Key or active GitHub OAuth session in the CLI).
  - The local CLI environment contains no stored Render API tokens or tunneling credentials, and creating third-party accounts without user interaction is prevented by security policy.
  - No paid plans or billing information were introduced, adhering strictly to the zero-cost mandate.
- **Pre-Configured Infrastructure on GitHub `main`:**
  - Infrastructure Blueprint: [`render.yaml`](../render.yaml)
  - Dependencies: [`requirements.txt`](../requirements.txt)
  - Entrypoint: [`app.py`](../app.py) (`gunicorn app:app`)

---

## 3. Exact Manual Action to Activate the Free Public URL

To activate the 100% free public HTTPS URL on Render:

1. Visit [dashboard.render.com](https://dashboard.render.com) and log in with your GitHub account (`Sufiyan367`).
2. Click **New +** $\rightarrow$ **Blueprint** (or **Web Service**).
3. Connect the repository: `Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem`.
4. Render automatically detects [`render.yaml`](../render.yaml) and configures the build (`pip install -r requirements.txt`) and start command (`gunicorn app:app`) on the **Free Tier**.
5. Click **Apply**. Within ~2 minutes, Render assigns the public HTTPS URL (e.g. `https://analysing-mental-health-student-ecosystem.onrender.com`).

---

## 4. Tableau Public Decoupling Notice

> [!IMPORTANT]
> **Native Tableau Cloud Status: PENDING MANUAL GUI AUTHORING**
>
> `TABLEAU_DASHBOARD_URL` and `TABLEAU_STORY_URL` remain empty until manual cloud authoring is published on profile [`sufiyansurve333`](https://public.tableau.com/app/profile/sufiyansurve333).
>
> The web application automatically falls back to verified high-resolution multi-device prototypes with full metric cards.
