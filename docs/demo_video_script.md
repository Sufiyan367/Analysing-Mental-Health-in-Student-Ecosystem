# Demonstration Video Script: Analysing Mental Health in Student Ecosystem

**Course:** Data Analytics with Tableau — Virtual Internship  
**Platform:** SkillWallet / SmartBridge  
**Student Author:** Sufiyan Surve  
**Target Video Duration:** 5–7 Minutes (Calibrated Duration: **6:26 Minutes** / 386.2 seconds)  
**Video Output Artifact:** [`evidence/demo/project_explanation_video.mp4`](../evidence/demo/project_explanation_video.mp4)  

---

## 📋 Video Overview & Presentation Structure

| Section # | Timestamp (Approx.) | Visual Slide / Screen Focus | Script Narration Topic |
| :---: | :---: | :--- | :--- |
| **01** | `00:00 – 00:28` | Title Slide & Project Metadata | Introduction of Student, Project Title & Virtual Internship Context |
| **02** | `00:28 – 00:59` | Problem Statement & Objectives | Psychological distress in universities; shift from reactive crisis to data-driven care |
| **03** | `00:59 – 01:32` | Dataset Sourcing & 18-Column Schema | Validated 200-student ecosystem dataset; 18 psychometric & lifestyle variables |
| **04** | `01:32 – 02:08` | Data Hygiene & Validation Audit | Zero missing cells, unique keys, schema validation, visualization readiness |
| **05** | `02:08 – 02:46` | 8 Unique Visualizations Inventory | Overview of the 8 dataset-grounded charts; rejection of mismatched demo metrics |
| **06** | `02:46 – 03:23` | Responsive Multi-Device Dashboard | Desktop (1920×1080), Tablet (1024×768), and Mobile layouts; 6 core panels & 4 KPIs |
| **07** | `03:23 – 04:01` | Guided 5-Scene Data Story | Sequential narrative: Baseline, Symptoms, Lifestyle, Vulnerability, and Care Progress |
| **08** | `04:01 – 04:39` | Performance Testing & Calculations | Ingestion benchmarks, filter latencies, 10 calculated fields, Tableau headroom |
| **09** | `04:39 – 05:12` | Flask Web Integration & Embedding | Live Flask portal (`/`, `/dashboard`, `/story`, `/about`), `<tableau-viz>` web components |
| **10** | `05:12 – 05:51` | Key Empirical Findings & Insights | 78% stress prevalence, 71.4% poor sleep, first-onset distress, CBT clinical recovery |
| **11** | `05:51 – 06:26` | Institutional Roadmap & Conclusion | Strategic recommendations for universities, Tableau publication status & closing |

---

## 🎙️ Verbatim Narration Script

### Section 1: Title & Introduction (00:00 – 00:28)
> *"Hello everyone. My name is Sufiyan Surve, and this is the project demonstration for my capstone project: **Analysing Mental Health in Student Ecosystem**, completed as part of the Data Analytics with Tableau Virtual Internship on SkillWallet by SmartBridge. In this presentation, I walk you through our complete analytics pipeline: problem formulation, data preparation, Tableau visual storytelling, performance benchmarking, and web integration in Python Flask."*

---

### Section 2: Problem Statement & Objectives (00:28 – 00:59)
> *"University students worldwide face increasing rates of psychological distress, academic burnout, and emotional fatigue. Traditionally, higher education institutions rely on reactive counseling services, discovering student struggles only after academic crisis. The objective of this project is to build an empirical diagnostic framework. By analyzing standardized anxiety and depression metrics alongside daily lifestyle habits, we provide university leadership with actionable, data-driven wellness interventions."*

---

### Section 3: Dataset Acquisition & Standardized Schema (00:59 – 01:32)
> *"Our analysis is grounded strictly in the validated **Student Mental Health Ecosystem Dataset**, consisting of 200 student records across 18 standardized variables. The schema captures three dimensions: demographics like Age and Gender, psychometrics including self-reported Stress Level, Anxiety Score, and Depression Score, and lifestyle factors including Sleep Quality, Daily Screen Time, Physical Activity, Mental Health History, Therapy Type, Intervention Duration, and Progress Score. No external demo metrics were fabricated."*

---

### Section 4: Data Validation & Preparation (01:32 – 02:08)
> *"Data hygiene is foundational to trustworthy analytics. Prior to visualization, the dataset underwent an exhaustive integrity audit. We confirmed all 200 User IDs are unique, spanning STU 0001 through STU 0200. Zero missing values exist across all 3,600 data points. Continuous metrics strictly obey valid clinical boundaries, and categorical entries are normalized. Certified visualization-ready, the clean dataset occupies 19.84 kilobytes on disk and parses in under 0.65 milliseconds."*

---

### Section 5: The 8 Unique Visualizations (02:08 – 02:46)
> *"In the Data Visualization stage, we created eight unique, dataset-grounded visualizations: 1. Stress Level Distribution, establishing baseline cohort spread. 2. Stress Level versus Anxiety Score, and 3. Stress Level versus Depression Score, showing progressive symptom surges. 4. Gender Mental Health Comparison. 5. Sleep Quality versus Stress, capturing restfulness deficits. 6. Screen Time versus Stress. 7. Mental Health History Prevalence. And 8. Ranked Therapy Efficacy, measuring recovery progress scores across clinical modalities."*

---

### Section 6: Responsive Multi-Device Dashboard Design (02:46 – 03:23)
> *"Next, we integrated these findings into an executive multi-device dashboard architecture. The layout features 4 top-level KPI cards: 200 Total Students, Average Anxiety of 52.59, Average Depression of 48.09, and Daily Screen Time of 7.10 hours. Beneath the KPIs, six core panels provide synchronized visual diagnostics. Crucially, we authored responsive layouts for Desktop at 1920 by 1080, Tablet in a 2-column format, and Mobile in a vertical scroll stack, ensuring cross-platform usability."*

---

### Section 7: Guided 5-Scene Data Story (03:23 – 04:01)
> *"To guide decision-makers through an intuitive diagnostic journey, we structured a 5-Scene Tableau Data Story. Scene 1 establishes the Cohort Baseline, showing that 78 percent of students suffer from moderate or high stress. Scene 2 reveals Symptom Escalation, proving high-stress students face a greater than 135 percent surge in anxiety and depression. Scene 3 demonstrates that 71.4 percent of high-stress students experience poor sleep. Scene 4 uncovers that 60 percent are first-onset cases, and Scene 5 proves Cognitive Behavioral Therapy yields the highest recovery progress at 40.80."*

---

### Section 8: Performance Testing & Calculation Fields (04:01 – 04:39)
> *"In Performance Testing, we executed comprehensive ingestion and filter benchmarks. Local benchmarks proved sub-millisecond parsing latency of 0.64 milliseconds for the 19.84 kilobyte dataset, with multi-predicate filtering executing in 0.86 to 1.41 milliseconds. We engineered and documented 10 production calculation fields, including Average Anxiety, Average Depression, Therapy Active Indicator, and High-Risk Sleep Deficit Flags, with exact formulas for native Tableau authoring. The dataset consumes less than 0.0013 percent of Tableau Public capacity."*

---

### Section 9: Flask Web Integration & Embedding (04:39 – 05:12)
> *"For web integration, we built a production-grade Python Flask web application. It serves four primary routes: the Executive Overview, Dashboards, Guided Story, and Methodology. The architecture embeds Tableau views using modern tableau-viz web components and JavaScript API v2. Configurable environment variables TABLEAU_DASHBOARD_URL and TABLEAU_STORY_URL allow instant live cloud embedding, while in the interim, our portal renders responsive prototypes and the 5-scene narrative browser with zero visual degradation."*

---

### Section 10: Key Empirical Findings (05:12 – 05:51)
> *"Our empirical analysis reveals four major clinical takeaways: First, elevated stress is widespread, affecting 78 percent of the cohort. Second, high stress couples with severe symptom escalation, driving anxiety to 72.06 and depression to 68.78. Third, behavioral habits compound distress: 71.4 percent of high-stress students experience poor sleep alongside 8.12 hours of screen immersion. Fourth, there is a critical care gap: 53.5 percent receive no therapy, while CBT leads recovery among active recipients with a 40.80 progress score."*

---

### Section 11: Institutional Recommendations & Conclusion (05:51 – 06:26)
> *"Based on these diagnostics, we propose three strategic recommendations for university leadership: First, expand accessible Cognitive Behavioral Therapy and counseling capacity. Second, institutionalize digital wellness and sleep hygiene workshops. Third, introduce opt-in mental health screenings during freshman orientation to catch first-onset distress early. Note that native Tableau Public publication remains pending manual browser upload, with all blueprints ready. In conclusion, this capstone delivers an end-to-end reproducible analytical solution. Thank you."*
