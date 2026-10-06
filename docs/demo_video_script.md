# Demonstration Video Script: Analysing Mental Health in Student Ecosystem

**Course:** Data Analytics with Tableau — Virtual Internship  
**Platform:** SkillWallet / SmartBridge  
**Student Author:** Sufiyan Surve  
**Target Video Duration:** 5–7 Minutes (~330–360 seconds)  
**Video Output Artifact:** [`evidence/demo/project_explanation_video.mp4`](../evidence/demo/project_explanation_video.mp4)  

---

## 📋 Video Overview & Presentation Structure

| Section # | Timestamp (Approx.) | Visual Slide / Screen Focus | Script Narration Topic |
| :---: | :---: | :--- | :--- |
| **01** | `00:00 – 00:30` | Title Slide & Project Metadata | Introduction of Student, Project Title & Virtual Internship Context |
| **02** | `00:30 – 01:00` | Problem Statement & Objectives | Psychological distress in universities; shift from reactive crisis to data-driven care |
| **03** | `01:00 – 01:30` | Dataset Sourcing & 18-Column Schema | Validated 200-student ecosystem dataset; 18 psychometric & lifestyle variables |
| **04** | `01:30 – 01:55` | Data Hygiene & Validation Audit | Zero missing cells, unique keys, schema validation, visualization readiness |
| **05** | `01:55 – 02:35` | 8 Unique Visualizations Inventory | Overview of the 8 dataset-grounded charts; rejection of mismatched demo metrics |
| **06** | `02:35 – 03:10` | Responsive Multi-Device Dashboard | Desktop (1920×1080), Tablet (1024×768), and Mobile layouts; 6 core panels & 4 KPIs |
| **07** | `03:10 – 03:55` | Guided 5-Scene Data Story | Sequential narrative: Baseline, Symptoms, Lifestyle, Vulnerability, and Care Progress |
| **08** | `03:55 – 04:30` | Performance Testing & Calculations | Ingestion benchmarks, filter latencies, 10 calculated fields, Tableau headroom |
| **09** | `04:30 – 05:00` | Flask Web Integration & Embedding | Live Flask portal (`/`, `/dashboard`, `/story`, `/about`), `<tableau-viz>` web components |
| **10** | `05:00 – 05:30` | Key Empirical Findings & Insights | 78% stress prevalence, 71.4% poor sleep, first-onset distress, CBT clinical recovery |
| **11** | `05:30 – 05:55` | Institutional Roadmap & Conclusion | Strategic recommendations for universities, Tableau publication status & closing |

---

## 🎙️ Verbatim Narration Script

### Section 1: Title & Introduction (00:00 – 00:30)
> *"Hello everyone. My name is Sufiyan Surve, and this is the comprehensive project demonstration for my capstone project: **Analysing Mental Health in Student Ecosystem**, completed as part of the Data Analytics with Tableau Virtual Internship on the SkillWallet platform by SmartBridge.*  
> *In this presentation, I will walk you through our complete end-to-end analytics workflow: from empirical problem definition and data hygiene, through advanced Tableau visual storytelling, performance benchmarking, and web integration in Python Flask."*

---

### Section 2: Problem Statement & Objectives (00:30 – 01:00)
> *"University students worldwide experience escalating rates of chronic psychological distress, academic burnout, and emotional fatigue. Traditionally, higher education institutions rely on reactive counseling services—meaning students are only noticed after academic crisis or severe symptom manifestation.*  
> *The objective of this project is to build an empirical, data-driven diagnostic framework. By analyzing standardized psychometric scores alongside daily behavioral habits, we aim to uncover the lifestyle drivers of distress and provide campus leadership with actionable, evidence-based recommendations."*

---

### Section 3: Dataset Acquisition & Standardized Schema (01:00 – 01:30)
> *"Our project is grounded strictly in the validated **Student Mental Health Ecosystem Dataset**, comprising 200 individual student records across 18 standardized variables.*  
> *The schema captures three critical analytical dimensions:*  
> *First, demographics such as Age, Gender, and Occupation.*  
> *Second, standardized psychometric metrics: self-reported Stress Level, Anxiety Score, and Depression Score.*  
> *Third, lifestyle and intervention indicators: Sleep Quality, Daily Screen Time, Physical Activity Level, Mental Health History, Therapy Type, Intervention Duration, Progress Score, and Medication Usage.*  
> *No external or mismatched attributes—such as Study Hours or Heart Rate Variability—were fabricated; our analysis is 100% dataset-grounded."*

---

### Section 4: Data Validation & Preparation (01:30 – 01:55)
> *"Data hygiene is the foundation of trustworthy analytics. Prior to visualization, the dataset underwent an exhaustive integrity audit.*  
> *We confirmed that all 200 User IDs are strictly unique, ranging from `STU_0001` to `STU_0200`.*  
> *Zero missing values or null cells exist across all 3,600 data points. Continuous measures were checked against valid clinical boundaries, and categorical labels were normalized.*  
> *The dataset was certified visualization-ready and archived in `data/cleaned/mental_health_student_ecosystem_cleaned.csv`."*

---

### Section 5: The 8 Unique Visualizations (01:55 – 02:35)
> *"In the Data Visualization stage, we engineered eight unique, empirically grounded charts:*  
> *1. Stress Level Distribution, establishing baseline cohort spread.*  
> *2. Stress Level versus Anxiety Score, quantifying anxiety symptom loads.*  
> *3. Stress Level versus Depression Score, showing parallel depressive escalation.*  
> *4. Gender Mental Health Comparison, evaluating cross-demographic distributions.*  
> *5. Sleep Quality versus Stress Level, illustrating restfulness deficits.*  
> *6. Screen Time versus Stress Level, measuring digital immersion.*  
> *7. Mental Health History Prevalence, revealing pre-existing diagnostic rates.*  
> *8. Ranked Therapy Efficacy, measuring recovery progress scores across clinical modalities.*  
> *Every visualization is backed by a high-resolution prototype and exact Tableau shelf specifications."*

---

### Section 6: Responsive Multi-Device Dashboard Design (02:35 – 03:10)
> *"Next, we unified these findings into an executive multi-device dashboard architecture.*  
> *The dashboard layout features 4 top-level KPI cards: Total Students at 200, Average Anxiety at 52.59, Average Depression at 48.09, and Daily Screen Time at 7.10 hours per day.*  
> *Beneath the KPIs, six core analytical panels provide synchronized visual diagnostics.*  
> *Crucially, we authored responsive variants for Desktop (1920 by 1080), Tablet (1024 by 768 in a 2-column format), and Mobile (in an accessible vertical scroll stack), ensuring seamless usability across executive boardroom screens and mobile devices."*

---

### Section 7: Guided 5-Scene Data Story (03:10 – 03:55)
> *"To guide decision-makers through an intuitive diagnostic journey, we structured a 5-Scene Tableau Data Story:*  
> *Scene 1 establishes the Cohort Baseline, showing that 78.0% of students suffer from moderate or high stress.*  
> *Scene 2 examines Symptom Escalation, proving that High Stress students experience a greater than 135% surge in both anxiety and depression.*  
> *Scene 3 uncovers Lifestyle Factors, showing that 71.4% of high-stress students experience poor sleep and average 8.12 hours of screen exposure.*  
> *Scene 4 addresses Vulnerability Factors, revealing that 60% of students had no prior mental health history, highlighting acute university first-onset distress.*  
> *Finally, Scene 5 evaluates Interventions, demonstrating that Cognitive Behavioral Therapy achieves the highest recovery progress score at 40.80."*

---

### Section 8: Performance Testing & Calculation Fields (03:55 – 04:30)
> *"In the Performance Testing epic, we conducted comprehensive data rendering benchmarks, filter utilization tests, and calculation audits.*  
> *Local benchmarks proved sub-millisecond parsing latency of 0.64 milliseconds for the 19.84 kilobyte dataset, with multi-predicate filtering executing in just 0.86 to 1.41 milliseconds.*  
> *We formally engineered and documented 10 production calculation fields—including Average Anxiety, Average Depression, Therapy Active Indicator, and High-Risk Sleep Deficit Flags—providing exact formulas for native Tableau authoring.*  
> *The dataset requires less than 0.0013% of Tableau Public capacity, guaranteeing zero latency bottlenecks."*

---

### Section 9: Flask Web Integration & Embedding (04:30 – 05:00)
> *"For web integration, we built a production-grade Python Flask web portal.*  
> *The application serves four primary routes: the Executive Overview at root, Dashboards, Guided Story, and Methodology.*  
> *The architecture embeds Tableau views using modern `<tableau-viz>` web components and the Tableau JavaScript API.*  
> *We implemented a graceful fallback mechanism: environment variables `TABLEAU_DASHBOARD_URL` and `TABLEAU_STORY_URL` allow instant live cloud embedding, while in the interim, the interactive portal renders our verified responsive prototypes and 5-scene narrative browser with zero visual degradation."*

---

### Section 10: Key Empirical Findings (05:00 – 05:30)
> *"Our empirical analysis delivers four critical takeaways:*  
> *First, high stress is ubiquitous: 156 out of 200 students experience elevated stress.*  
> *Second, behavioral habits compound distress: 71.4% of high-stress students suffer from severe sleep deficits paired with 8.12 hours of screen immersion.*  
> *Third, there is an institutional care gap: 53.5% of students receive no therapy, including 15 high-stress and 48 medium-stress students.*  
> *Fourth, evidence-based therapy works: CBT and Counseling show robust, measurable symptom relief across active participants."*

---

### Section 11: Institutional Recommendations & Conclusion (05:30 – 05:55)
> *"Based on these diagnostics, we propose three strategic recommendations for university leadership:*  
> *1. Scale accessible Cognitive Behavioral Therapy and counseling capacity.*  
> *2. Implement institutional digital wellness and sleep hygiene workshops.*  
> *3. Introduce early, opt-in mental health screenings during orientation to identify first-onset distress early.*  
> *In summary, this capstone delivers a complete, reproducible data pipeline, robust visual architecture, and a modern web portal.*  
> *Thank you very much for your time and evaluation."*
