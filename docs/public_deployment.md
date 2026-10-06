# Public Production Deployment Guide

## Project: Analysing Mental Health in Student Ecosystem
**Repository:** [`https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem`](https://github.com/Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem)  
**Framework:** Python Flask 3.0.3 with WSGI Gunicorn 21+  
**Target Platform:** [Render](https://render.com) (Native Python Web Service)

---

## 1. Hosting Architecture & Specification

The application is architected to run as a stateless, containerized Python web service:

- **Hosting Provider:** Render (Free / Starter Tier Web Service)
- **Environment Runtime:** Python 3.11.x
- **Build Command:** `pip install -r requirements.txt`
- **Production Start Command:** `gunicorn app:app`
- **Infrastructure Blueprint:** [`render.yaml`](../render.yaml)
- **Port Binding:** Automatically binds to the `$PORT` environment variable provided by Render (falls back to port `5000` locally).

---

## 2. Environment Variables Configuration

| Variable Name | Default / Production Value | Purpose |
| :--- | :--- | :--- |
| `PYTHON_VERSION` | `3.11.9` | Sets the Python runtime version on Render. |
| `PORT` | Set automatically by Render | The HTTP listening port for Gunicorn. |
| `TABLEAU_PROFILE_URL` | `https://public.tableau.com/app/profile/sufiyansurve333` | Author profile link displayed across headers and footers. |
| `TABLEAU_DASHBOARD_URL` | `""` (Empty string) | Live Tableau Public dashboard URL. Kept empty until manual authoring is published; triggers verified prototype fallback. |
| `TABLEAU_STORY_URL` | `""` (Empty string) | Live Tableau Public story URL. Kept empty until manual authoring is published; triggers verified prototype fallback. |

---

## 3. Step-by-Step Render Deployment Procedure

To provision the public HTTPS demo URL on Render:

1. **Sign in to Render:**  
   Navigate to [dashboard.render.com](https://dashboard.render.com) and log in using your GitHub account (`Sufiyan367`).
2. **Create New Web Service:**  
   Click **New +** $\rightarrow$ **Web Service**.
3. **Connect GitHub Repository:**  
   Select the repository: `Sufiyan367/Analysing-Mental-Health-in-Student-Ecosystem`.  
   *(If prompted, grant Render access to your public GitHub repositories).*
4. **Configure Service Settings:**
   - **Name:** `analysing-mental-health-student-ecosystem`
   - **Region:** Frankfurt (EU) or Oregon (US West)
   - **Branch:** `main`
   - **Root Directory:** *(leave blank)*
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** `Free`
5. **Add Environment Variables (Optional):**
   - `PYTHON_VERSION` = `3.11.9`
6. **Deploy:**  
   Click **Create Web Service**.
7. **Obtain Public URL:**  
   Once the build completes (approx. 2–3 minutes), Render provides a live HTTPS endpoint:  
   `https://analysing-mental-health-student-ecosystem.onrender.com`

---

## 4. Route Health-Check Specifications

Upon deployment, the following routes provide 100% functionality and sub-second load times:

| Route | Expected Status | Verified Page Title & Content |
| :--- | :---: | :--- |
| `/` | **HTTP 200 OK** | *Executive Overview — Analysing Mental Health in Student Ecosystem*<br>Renders 4 live KPI cards ($N=200$, Anxiety $52.59$, Depression $48.09$, Screen Time $7.10\text{ hrs}$) and 4 empirical diagnostic pillars. |
| `/dashboard` | **HTTP 200 OK** | *Interactive Dashboards — Analysing Mental Health in Student Ecosystem*<br>Renders multi-device layout selector (Desktop, Tablet, Mobile) and responsive prototype views. |
| `/story` | **HTTP 200 OK** | *Guided Data Story — Analysing Mental Health in Student Ecosystem*<br>Renders interactive 5-scene narrative carousel with step controls. |
| `/about` | **HTTP 200 OK** | *Methodology & Architecture — Analysing Mental Health in Student Ecosystem*<br>Renders 18-variable schema dictionary, 10 calculation formulas, and validation report. |
| `/evidence/<path>` | **HTTP 200 OK** | Direct static asset delivery for visual charts, responsive dashboard PNGs, and the 6:26 demonstration video MP4. |

---

## 5. Tableau Public Publication Transparency Notice

> [!IMPORTANT]
> **Native Tableau Cloud Status: PENDING MANUAL GUI AUTHORING**
>
> The Flask web portal is fully decoupled from the Tableau Cloud publication state. When `TABLEAU_DASHBOARD_URL` and `TABLEAU_STORY_URL` are not defined, the portal seamlessly serves high-resolution responsive prototypes with full analytical fidelity.
>
> Once the author publishes the native workbook on Tableau Public ([`sufiyansurve333`](https://public.tableau.com/app/profile/sufiyansurve333)), set the two environment variables in the Render Dashboard under **Environment** to instantly transition the portal to live `<tableau-viz>` cloud components.
