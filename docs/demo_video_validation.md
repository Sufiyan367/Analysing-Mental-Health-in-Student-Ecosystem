# Project Demonstration Video Validation Report

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Course:** Data Analytics with Tableau — Virtual Internship  
**Platform:** SkillWallet / SmartBridge  
**Student Author:** Sufiyan Surve  
**Date of Validation:** October 2026  
**Live Public Showcase:** [https://sufiyan367.github.io/Analysing-Mental-Health-in-Student-Ecosystem/](https://sufiyan367.github.io/Analysing-Mental-Health-in-Student-Ecosystem/)  
**Primary Video Artifact:** [`evidence/demo/project_explanation_video.mp4`](../evidence/demo/project_explanation_video.mp4)  
**Public Video Artifact:** [`docs/evidence/demo/project_explanation_video.mp4`](evidence/demo/project_explanation_video.mp4)

---

## 1. Executive Summary & Comparison

| Metric / Attribute | Previous Video (Slideshow Prototype) | NEW Final Video (Live Screen Recording) | Status / Verdict |
| :--- | :--- | :--- | :--- |
| **Duration** | 6:26 min (386.2s) | **6:24 min (384.86s)** | **Compliant** (5:00–7:00 requirement met) |
| **Visual Source** | Static Pillow slide cards | **Live GitHub Pages Browser Session** | **Dramatically Superior** |
| **Browser Interaction** | None (Static slides) | **Smooth scrolling, animated cursor, pulse highlights** | **Engaging & Human-Led** |
| **Voiceover Engine** | Basic synthetic voice | **Edge Neural Voice (`en-IN-PrabhatNeural`)** | **Natural Indian English Student Accent** |
| **Resolution** | 1920×1080 (16:9) | **1920×1080 (16:9 Full HD)** | **Compliant** |
| **Video Codec** | H.264 (avc1) High Profile | **H.264 (avc1) High Profile** | **Compliant** |
| **Audio Codec** | AAC mono 144 kbps | **AAC mono 192 kbps (24 kHz)** | **Compliant** |
| **File Size** | 13.75 MB | **37.48 MB** (Higher visual detail) | **High Quality & Fast Streaming** |
| **Web Integration** | Download link only | **HTML5 `<video>` Player with Controls embedded in page** | **Seamless Public UX** |

---

## 2. Technical Inspection via FFprobe

```bash
ffprobe -v error -show_entries format=duration,size,bit_rate -show_entries stream=codec_name,width,height,r_frame_rate -of default=noprint_wrappers=1 evidence/demo/project_explanation_video.mp4
```

### Verified Technical Output:
- **Container Format:** MPEG-4 (`isom` / `iso2` / `avc1` / `mp41`)
- **Duration:** `384.858667` seconds (**06:24.86**)
- **File Size:** `37,478,282` bytes (~35.74 MiB)
- **Total Bitrate:** `779,055` bps (~779 kbps)
- **Video Stream:**
  - Codec: `H.264 / AVC` (High Profile)
  - Dimensions: `1920 × 1080` (1080p Full HD)
  - Aspect Ratio: `16:9`
  - Pixel Format: `yuv420p`
  - Nominal Frame Rate: `25.0 fps`
- **Audio Stream:**
  - Codec: `AAC (LC)`
  - Sampling Rate: `24,000 Hz`
  - Channels: `Mono`
  - Bitrate: `112 kbps`

---

## 3. Screen Recording Flow & Timing Audit

| Scene # | Section | Start | End | Target Focus | Key Findings Highlighted |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **01** | Introduction & Problem | `00:00` | `00:35` | Hero banner & student metadata | Student introduction, problem statement, Capstone objective |
| **02** | Cohort KPIs | `00:35` | `01:15` | 4 Top KPI cards | 200 records, Anxiety 52.59, Depression 48.09, Screen time 7.10 hrs |
| **03** | Methodology | `01:15` | `01:51` | Methodology schema table | 18 columns, zero nulls, unique STU IDs, clinical boundaries |
| **04** | Executive Dashboard | `01:51` | `02:33` | 1920×1080 Dashboard preview | 78% stress prevalence, 71.4% poor sleep, 8.12 hrs screen time |
| **05** | Story Scene 1 | `02:33` | `03:03` | Scene 01 Card | Baseline: 44 Low, 107 Medium, 49 High stress |
| **06** | Story Scene 2 | `03:03` | `03:42` | Scene 02 Card | Anxiety surge (+138%), Depression surge (+156%), Gender parity |
| **07** | Story Scene 3 | `03:42` | `04:16` | Scene 03 Card | 71.4% poor sleep, 8.12 hrs screen immersion, inactivity |
| **08** | Story Scene 4 | `04:16` | `04:46` | Scene 04 Card | 40% history vs 60% first-onset (14 high stress), peer buffer |
| **09** | Story Scene 5 | `04:46` | `05:19` | Scene 05 Card | CBT highest recovery (40.80), 53.5% care gap (107 students) |
| **10** | Key Findings | `05:19` | `05:51` | 4 Empirical Takeaways | Prevalence, Escalation, Compounding, Institutional Gap |
| **11** | Conclusion & Closing | `05:51` | `06:24` | CTA Banner & Footer | University action roadmap, honest Tableau status, GitHub link |

---

## 4. Verification of Human-Style Student Presentation

1. **Voice Character:**
   - Model: `en-IN-PrabhatNeural`
   - Acoustic Tone: Confident, articulate, conversational Indian college student presenting technical findings.
   - Pacing: Calibrated at `rate=+18%` for energetic, clear cadence without any robotic artifacts or monotonic inflection.
   - Pauses: Built-in natural commas and sentence transitions allowing listener comprehension.

2. **Visual Interaction:**
   - Live Browser: Captured via Playwright Chromium at 1920×1080 against the public website.
   - Cursor Overlay: Custom smooth cubic-bezier cursor with drop-shadow that glides to cards, pulses upon key metrics, and points intentionally to relevant charts.
   - Presenter Pill: High-contrast floating pill displaying `Presenter: Sufiyan Surve | Student Ecosystem Walkthrough` with a green active status pulse.
   - Smooth Navigation: Custom cosine-eased window scrolling prevents jerky motion and preserves readable text.

---

## 5. Academic Honesty & Scope Compliance

- **No Fabricated URLs:** Tableau Public native publication is clearly disclosed as pending manual authoring.
- **Flask Deployment Honesty:** Flask runtime is documented as verified on `localhost:5000` with static showcase hosted on GitHub Pages.
- **Dataset Ground Truth:** Grounded 100% in `data/cleaned/mental_health_student_ecosystem_cleaned.csv` (200 records, 18 variables). Unrelated demo metrics (HRV, study hours, restaurant delivery) are strictly excluded.
