# Public Production Deployment Guide

## Project: Analysing Mental Health in Student Ecosystem
**Repository:** [`https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem`](https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem)  
**Framework:** Python Flask 3.0.3 with WSGI Gunicorn 21+  
**Target Platform:** [Render](https://render.com) (Native Python Web Service)

---

## 1. Current Deployment & Verification Status

> [!IMPORTANT]
> **Status: Ready for 1-Click Provisioning on Render (Pending User Dashboard Authorization)**
> 
> The repository includes complete production infrastructure files ([`render.yaml`](../render.yaml), [`requirements.txt`](../requirements.txt), and WSGI entrypoint `app:app`).
> 
> Because Render requires personal account authentication (OAuth / API token) which is not connected locally in this CLI environment, the service has not yet been provisioned on Render's servers. Therefore, `https://analysing-mental-health-student-ecosystem.onrender.com` returns `HTTP 404: Not Found` until the 1-click connection is authorized on [dashboard.render.com](https://dashboard.render.com).

---

## 2. Hosting Architecture & Specification

The application is architected to run as a stateless, containerized Python web service:

- **Hosting Provider:** Render (Free / Starter Tier Web Service)
- **Environment Runtime:** Python 3.11.x
- **Build Command:** `pip install -r requirements.txt`
- **Production Start Command:** `gunicorn app:app`
- **Infrastructure Blueprint:** [`render.yaml`](../render.yaml)
- **Port Binding:** Automatically binds to the `$PORT` environment variable provided by Render (falls back to port `5000` locally).

---

## 3. Environment Variables Configuration

| Variable Name | Production Setting | Purpose |
| :--- | :--- | :--- |
| `PYTHON_VERSION` | `3.11.9` | Sets the Python runtime version on Render. |
| `PORT` | Set automatically by Render | The HTTP listening port for Gunicorn. |
| `TABLEAU_PROFILE_URL` | `https://public.tableau.com/app/profile/sufiyansurve333` | Author profile link displayed across headers and footers. |
| `TABLEAU_DASHBOARD_URL` | `""` (Empty string) | Live Tableau Public dashboard URL. Kept empty until manual authoring is published; triggers verified prototype fallback. |
| `TABLEAU_STORY_URL` | `""` (Empty string) | Live Tableau Public story URL. Kept empty until manual authoring is published; triggers verified prototype fallback. |

---

## 4. 1-Click Provisioning Steps on Render

To provision the live public HTTPS demo endpoint:

1. **Sign in to Render:**  
   Navigate to [dashboard.render.com](https://dashboard.render.com) and log in with your GitHub account (`Sufiyan367`).
2. **Deploy with Blueprint / Web Service:**  
   - Click **New +** $\rightarrow$ **Blueprint** (or **Web Service**).
   - Select repository: `Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem`.
   - Render automatically reads [`render.yaml`](../render.yaml) and populates the build command (`pip install -r requirements.txt`), start command (`gunicorn app:app`), and environment variables.
3. **Deploy:**  
   Click **Apply** / **Create Web Service**.
4. **Live Verification:**  
   Render will build the dependencies and provide the assigned HTTPS URL (e.g. `https://analysing-mental-health-student-ecosystem.onrender.com`).

---

## 5. Local Production Route Health-Check Audit

All core routes and assets were verified against the Flask production application object (`app.app`):

| Route | Status | Verified Page Title & Content |
| :--- | :---: | :--- |
| `/` | **HTTP 200 OK** | *Executive Overview — Analysing Mental Health in Student Ecosystem*<br>Computes all 4 cohort KPIs ($N=200$, Anxiety $52.59$, Depression $48.09$, Screen Time $7.10\text{ hrs}$) directly from CSV; renders CSS Grid and subgroup badges. |
| `/dashboard` | **HTTP 200 OK** | *Interactive Dashboards — Analysing Mental Health in Student Ecosystem*<br>Renders multi-device prototype selector (Desktop, Tablet, Mobile) and responsive diagnostic panels. |
| `/story` | **HTTP 200 OK** | *Guided Data Story — Analysing Mental Health in Student Ecosystem*<br>Renders interactive 5-scene narrative carousel with previous/next controls, observations, and recommendations. |
| `/about` | **HTTP 200 OK** | *Methodology & Architecture — Analysing Mental Health in Student Ecosystem*<br>Renders 18-variable schema dictionary, 10 calculation formulas, and validation compliance report. |
| `/evidence/<path>` | **HTTP 200 OK** | Direct static asset delivery for visual charts, responsive dashboard PNGs, and the 6:26 demonstration video MP4. |

---

## 6. Tableau Public Publication Transparency Notice

> [!IMPORTANT]
> **Native Tableau Cloud Status: PENDING MANUAL GUI AUTHORING**
>
> The Flask web portal is fully decoupled from the Tableau Cloud publication state. When `TABLEAU_DASHBOARD_URL` and `TABLEAU_STORY_URL` are not defined, the portal seamlessly serves high-resolution responsive prototypes with full analytical fidelity.
>
> Once the author publishes the native workbook on Tableau Public ([`sufiyansurve333`](https://public.tableau.com/app/profile/sufiyansurve333)), set the two environment variables in the Render Dashboard under **Environment** to instantly transition the portal to live `<tableau-viz>` cloud components.
