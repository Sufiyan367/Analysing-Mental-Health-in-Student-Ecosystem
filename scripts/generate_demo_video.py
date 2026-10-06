"""
Generate 5-6 Minute End-to-End Project Demonstration Video
Synthesizes professional narration via pyttsx3, generates 1920x1080
16:9 walkthrough frames using real project evidence, and merges
into evidence/demo/project_explanation_video.mp4 using ffmpeg/moviepy.
"""

import os
import sys
import time
import subprocess
import pyttsx3
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

def create_demo_video():
    output_dir = os.path.join('evidence', 'demo')
    os.makedirs(output_dir, exist_ok=True)
    temp_dir = os.path.join(output_dir, 'temp_build')
    os.makedirs(temp_dir, exist_ok=True)

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    print(f"Using ffmpeg: {ffmpeg_exe}")

    sections = [
        {
            "id": 1,
            "title": "Project Introduction & Scope",
            "subtitle": "Virtual Internship Capstone — SkillWallet / SmartBridge",
            "script": "Hello everyone. My name is Sufiyan Surve, and this is the comprehensive project demonstration for my capstone project: Analysing Mental Health in Student Ecosystem, completed as part of the Data Analytics with Tableau Virtual Internship on the SkillWallet platform by SmartBridge. In this presentation, I will walk you through our complete end-to-end analytics workflow: from empirical problem definition and data hygiene, through advanced Tableau visual storytelling, performance benchmarking, and web integration in Python Flask.",
            "bullet_points": [
                "Author: Sufiyan Surve (Tableau Public: @sufiyansurve333)",
                "Program: Data Analytics with Tableau — SkillWallet / SmartBridge",
                "Capstone Focus: Mental Health Diagnostics in University Ecosystems",
                "Technology Stack: Python, Pandas, Matplotlib, Tableau Architecture, Flask, Playwright",
                "Dataset Source of Truth: 200 Students x 18 Validated Variables"
            ],
            "img_path": None
        },
        {
            "id": 2,
            "title": "Problem Statement & Analytical Objectives",
            "subtitle": "Moving Campus Care from Reactive Crisis to Proactive Analytics",
            "script": "University students worldwide experience escalating rates of chronic psychological distress, academic burnout, and emotional fatigue. Traditionally, higher education institutions rely on reactive counseling services, meaning students are only noticed after academic crisis or severe symptom manifestation. The objective of this project is to build an empirical, data-driven diagnostic framework. By analyzing standardized psychometric scores alongside daily behavioral habits, we aim to uncover the lifestyle drivers of distress and provide campus leadership with actionable, evidence-based recommendations.",
            "bullet_points": [
                "The Core Challenge: Campus mental distress is historically addressed reactively.",
                "Diagnostic Need: Early identification of student distress before academic probation.",
                "Multivariate Focus: Unifying subjective stress with clinical anxiety and depression.",
                "Behavioral Vectors: Evaluating the compounding role of sleep quality and digital immersion.",
                "Target Outcome: Strategic resource allocation and evidence-based clinical therapy expansion."
            ],
            "img_path": None
        },
        {
            "id": 3,
            "title": "Dataset Acquisition & Standardized Schema",
            "subtitle": "200 Records x 18 Standardized Variables",
            "script": "Our project is grounded strictly in the validated Student Mental Health Ecosystem Dataset, comprising 200 individual student records across 18 standardized variables. The schema captures three critical analytical dimensions: First, demographics such as Age, Gender, and Occupation. Second, standardized psychometric metrics: self-reported Stress Level, Anxiety Score, and Depression Score. Third, lifestyle and intervention indicators: Sleep Quality, Daily Screen Time, Physical Activity Level, Mental Health History, Therapy Type, Intervention Duration, Progress Score, and Medication Usage. No external or mismatched demo attributes were fabricated.",
            "bullet_points": [
                "Cohort Size: N = 200 authentic student profiles (STU_0001 to STU_0200)",
                "Demographics: Age (18-25), Gender (Male, Female, Other), Occupation",
                "Psychometrics: Stress Level (Low, Med, High), Anxiety (0-100), Depression (0-100)",
                "Lifestyle: Sleep Quality (Poor, Avg, Good), Daily Screen Time (hrs), Physical Activity",
                "Clinical Support: Mental Health History, Therapy Type, Intervention Duration, Progress Score",
                "Integrity: Generic demo metrics like Study Hours and HRV are strictly excluded."
            ],
            "img_path": None
        },
        {
            "id": 4,
            "title": "Data Preparation & Integrity Validation",
            "subtitle": "Sub-millisecond Ingestion and Zero Data Quality Defects",
            "script": "Data hygiene is the foundation of trustworthy analytics. Prior to visualization, the dataset underwent an exhaustive integrity audit. We confirmed that all 200 User IDs are strictly unique, ranging from STU 0001 to STU 0200. Zero missing values or null cells exist across all 3,600 data points. Continuous measures were checked against valid clinical boundaries, and categorical labels were normalized. The dataset was certified visualization-ready and archived in data/cleaned/mental_health_student_ecosystem_cleaned.csv.",
            "bullet_points": [
                "Completeness: 0 missing cells out of 3,600 data points (100% complete)",
                "Uniqueness: 200 distinct User IDs with zero duplicate collisions",
                "File Storage: 19.84 Kilobytes on-disk (20,318 bytes); 137.12 Kilobytes in-memory",
                "Parsing Velocity: Mean CSV parse latency of 0.64 milliseconds",
                "Certification: Certified visualization-ready in validation_summary.json"
            ],
            "img_path": os.path.join('evidence', 'performance', 'data_rendering', 'data_rendering_benchmark.png')
        },
        {
            "id": 5,
            "title": "8 Unique Dataset-Grounded Visualizations",
            "subtitle": "Systematic Analytical Exploration of Student Well-being",
            "script": "In the Data Visualization stage, we engineered eight unique, empirically grounded charts: 1. Stress Level Distribution, establishing baseline cohort spread. 2. Stress Level versus Anxiety Score, quantifying anxiety symptom loads. 3. Stress Level versus Depression Score, showing parallel depressive escalation. 4. Gender Mental Health Comparison, evaluating cross-demographic distributions. 5. Sleep Quality versus Stress Level, illustrating restfulness deficits. 6. Screen Time versus Stress Level, measuring digital immersion. 7. Mental Health History Prevalence, revealing pre-existing diagnostic rates. 8. Ranked Therapy Efficacy, measuring recovery progress scores across clinical modalities.",
            "bullet_points": [
                "Vis 1: Stress Level Distribution (Bar Chart: Low 22.0%, Med 53.5%, High 24.5%)",
                "Vis 2: Stress vs Anxiety (Avg: Low 30.27, Med 52.85, High 72.06)",
                "Vis 3: Stress vs Depression (Avg: Low 26.80, Med 47.37, High 68.78)",
                "Vis 4: Gender Mental Health Comparison (Dual-Measure Grouped Bar)",
                "Vis 5: Sleep Quality vs Stress (Stacked Bar: 71.4% Poor Sleep in High Stress)",
                "Vis 6: Screen Time vs Stress (High Stress averages 8.12 hrs/day)",
                "Vis 7: Mental Health History Distribution (Donut Chart: 60% No History)",
                "Vis 8: Ranked Therapy Efficacy (CBT top recovery at 40.80 progress score)"
            ],
            "img_path": os.path.join('evidence', 'visualizations', '01_stress_level_distribution.png')
        },
        {
            "id": 6,
            "title": "Responsive Multi-Device Dashboard Architecture",
            "subtitle": "Desktop (1920x1080), Tablet (1024x768), and Mobile Stack",
            "script": "Next, we unified these findings into an executive multi-device dashboard architecture. The dashboard layout features 4 top-level KPI cards: Total Students at 200, Average Anxiety at 52.59, Average Depression at 48.09, and Daily Screen Time at 7.10 hours per day. Beneath the KPIs, six core analytical panels provide synchronized visual diagnostics. Crucially, we authored responsive variants for Desktop, Tablet in a 2-column format, and Mobile in an accessible vertical scroll stack, ensuring seamless usability across executive boardroom screens and mobile devices.",
            "bullet_points": [
                "4 Verified KPI Cards: Cohort (200), Anxiety (52.59), Depression (48.09), Screen Time (7.10 hrs)",
                "6 Core Panels: Stress Spread, Symptom Triad, Sleep Deficit, Screen Time, History, Therapy",
                "Desktop Layout: 1920 x 1080 widescreen grid (16:9 aspect ratio)",
                "Tablet Layout: 1024 x 768 balanced 2-column card hierarchy",
                "Mobile Layout: Single-column vertical scroll with high-contrast touch targets",
                "Status: High-resolution prototypes and exact layout specifications ready for authoring"
            ],
            "img_path": os.path.join('evidence', 'dashboard', 'student_mental_health_dashboard.png')
        },
        {
            "id": 7,
            "title": "Guided 5-Scene Tableau Data Story",
            "subtitle": "Translating Empirical Diagnostics into Actionable Policy",
            "script": "To guide decision-makers through an intuitive diagnostic journey, we structured a 5-Scene Tableau Data Story: Scene 1 establishes the Cohort Baseline, showing that 78.0% of students suffer from moderate or high stress. Scene 2 examines Symptom Escalation, proving that High Stress students experience a greater than 135% surge in both anxiety and depression. Scene 3 uncovers Lifestyle Factors, showing that 71.4% of high-stress students experience poor sleep and average 8.12 hours of screen exposure. Scene 4 addresses Vulnerability Factors, revealing that 60% of students had no prior mental health history, highlighting acute university first-onset distress. Finally, Scene 5 evaluates Interventions, demonstrating that Cognitive Behavioral Therapy achieves the highest recovery progress score at 40.80.",
            "bullet_points": [
                "Scene 1 — Baseline: 78.0% of cohort in moderate or severe distress tiers",
                "Scene 2 — Symptoms: Steep concurrent surge in anxiety (72.06) and depression (68.78)",
                "Scene 3 — Lifestyle: The triad of sleep loss (71.4%), screen time (8.12 hrs), and inactivity",
                "Scene 4 — Vulnerability: 60% first-onset university cases; only 9.0% on medication",
                "Scene 5 — Recovery: Structured CBT leads clinical efficacy across 7.50 weeks",
                "Evidence: 5 verified high-resolution story scenes stored under evidence/story/"
            ],
            "img_path": os.path.join('evidence', 'story', '05_intervention_and_progress.png')
        },
        {
            "id": 8,
            "title": "Performance Testing & Calculated Fields",
            "subtitle": "Ingestion Latencies, Multi-Predicate Filters, and 10 Production Formulas",
            "script": "In the Performance Testing epic, we conducted comprehensive data rendering benchmarks, filter utilization tests, and calculation audits. Local benchmarks proved sub-millisecond parsing latency of 0.64 milliseconds for the 19.84 kilobyte dataset, with multi-predicate filtering executing in just 0.86 to 1.41 milliseconds. We formally engineered and documented 10 production calculation fields, including Average Anxiety, Average Depression, Therapy Active Indicator, and High-Risk Sleep Deficit Flags, providing exact formulas for native Tableau authoring. The dataset requires less than 0.0013% of Tableau Public capacity, guaranteeing zero latency bottlenecks.",
            "bullet_points": [
                "Data Rendering Volume: 19.84 KB CSV; parsing executes in 0.64 ms; load in 3.17 ms",
                "Filter Scalability: Single filters run in ~0.86 ms; 3-way compound filters run in 1.41 ms",
                "10 Calculation Fields: 5 Measures (Anxiety, Depression, Screen Time, Count, Progress)",
                "5 Dimensions: Therapy Active Flag, High Stress Flag, Distress Index, Age Group, Sleep Flag",
                "Tableau Public Capacity: Dataset consumes <0.0013% of allowed row capacity"
            ],
            "img_path": os.path.join('evidence', 'performance', 'filters', 'filter_performance_benchmark.png')
        },
        {
            "id": 9,
            "title": "Flask Web Integration & Cloud Embedding",
            "subtitle": "Production Web Portal with Modern Embedding and Responsive Fallbacks",
            "script": "For web integration, we built a production-grade Python Flask web portal. The application serves four primary routes: the Executive Overview at root, Dashboards, Guided Story, and Methodology. The architecture embeds Tableau views using modern tableau-viz web components and the Tableau JavaScript API. We implemented a graceful fallback mechanism: environment variables TABLEAU_DASHBOARD_URL and TABLEAU_STORY_URL allow instant live cloud embedding, while in the interim, the interactive portal renders our verified responsive prototypes and 5-scene narrative browser with zero visual degradation.",
            "bullet_points": [
                "Route /: Executive overview with live KPI cards and analytical diagnostic pillars",
                "Route /dashboard: Multi-device prototype layout switcher with Tableau embed frame",
                "Route /story: Interactive 5-scene narrative browser with sequential observations",
                "Route /about: Technical methodology, 18-column schema, and 10 calculation formulas",
                "Tableau Embedding: Modern <tableau-viz> Web Component with JS API v2 fallback",
                "Validation: 100% routes tested (HTTP 200 OK) with Playwright screenshot evidence"
            ],
            "img_path": os.path.join('evidence', 'web_integration', 'home_page.png')
        },
        {
            "id": 10,
            "title": "Key Empirical Findings & Clinical Diagnostics",
            "subtitle": "Summary of Core Psychological & Behavioral Patterns",
            "script": "Our empirical analysis delivers four critical takeaways: First, high stress is ubiquitous: 156 out of 200 students experience elevated stress. Second, behavioral habits compound distress: 71.4% of high-stress students suffer from severe sleep deficits paired with 8.12 hours of screen immersion. Third, there is an institutional care gap: 53.5% of students receive no therapy, including 15 high-stress and 48 medium-stress students. Fourth, evidence-based therapy works: CBT and Counseling show robust, measurable symptom relief across active participants.",
            "bullet_points": [
                "1. Ubiquitous Stress Burden: 78.0% of cohort operates in moderate or severe stress.",
                "2. Direct Symptom Escalation: >135% surge in anxiety and depression for high stress.",
                "3. Lifestyle Risk Intersection: 71.4% poor sleep + 8.12 hrs screen exposure.",
                "4. Acute First-Onset Distress: 60% with no prior history face significant university distress.",
                "5. The Care Gap: 107 students (53.5%) in No Therapy, including 15 high-stress individuals.",
                "6. Clinical Efficacy: Structured CBT demonstrates superior symptom alleviation (40.80 score)."
            ],
            "img_path": os.path.join('evidence', 'visualizations', '08_therapy_type_vs_progress.png')
        },
        {
            "id": 11,
            "title": "Institutional Recommendations & Conclusion",
            "subtitle": "Roadmap for Universities & Status Transparency",
            "script": "Based on these diagnostics, we propose three strategic recommendations for university leadership: 1. Scale accessible Cognitive Behavioral Therapy and counseling capacity. 2. Implement institutional digital wellness and sleep hygiene workshops. 3. Introduce early, opt-in mental health screenings during orientation to identify first-onset distress early. Regarding Tableau status: All authoring blueprints, calculations, and prototypes are complete. Cloud publishing remains pending manual browser authoring. In summary, this capstone delivers a complete, reproducible data pipeline, robust visual architecture, and a modern web portal. Thank you very much for your time and evaluation.",
            "bullet_points": [
                "Recommendation 1: Scale campus CBT and group counseling partnerships.",
                "Recommendation 2: Institutionalize digital wellness and sleep hygiene workshops.",
                "Recommendation 3: Implement early mental health screenings during freshman orientation.",
                "Status Notice: Native Tableau workbook specifications prepared; live cloud publishing pending.",
                "Project Complete: Validated data pipeline, 8 visualizations, responsive dashboard, 5-scene story & Flask portal."
            ],
            "img_path": None
        }
    ]

    print(f"Generating narration audio for {len(sections)} sections via pyttsx3...")
    engine = pyttsx3.init()
    engine.setProperty('rate', 160) # Natural clear speaking pace

    audio_files = []
    durations = []

    for sec in sections:
        sec_id = sec['id']
        wav_path = os.path.join(temp_dir, f"audio_{sec_id:02d}.wav")
        engine.save_to_file(sec['script'], wav_path)
        engine.runAndWait()

        # Probe duration of wav file using ffmpeg
        probe_cmd = [
            ffmpeg_exe, "-i", wav_path, "-hide_banner"
        ]
        res = subprocess.run(probe_cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        # Parse duration from ffmpeg output: Duration: 00:00:28.50
        dur = 30.0 # fallback
        for line in res.stderr.split('\n'):
            if 'Duration:' in line:
                dur_str = line.split('Duration:')[1].split(',')[0].strip()
                parts = dur_str.split(':')
                dur = float(parts[0])*3600 + float(parts[1])*60 + float(parts[2])
                break
        
        # Add a 1.5s padding for smooth transitions
        dur += 1.5
        durations.append(dur)
        audio_files.append(wav_path)
        print(f"Section {sec_id}: Generated {dur:.2f}s audio")

    total_duration = sum(durations)
    print(f"Total video planned duration: {total_duration:.2f} seconds ({total_duration/60:.2f} minutes)")

    # Generate 1920x1080 16:9 Slide Images
    print("Generating high-resolution 1920x1080 video slide frames...")
    slide_images = []

    # Try default fonts
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 46)
        font_sub = ImageFont.truetype("arial.ttf", 26)
        font_head = ImageFont.truetype("arialbd.ttf", 32)
        font_body = ImageFont.truetype("arial.ttf", 26)
        font_meta = ImageFont.truetype("arial.ttf", 22)
    except:
        font_title = ImageFont.load_default()
        font_sub = font_title
        font_head = font_title
        font_body = font_title
        font_meta = font_title

    W, H = 1920, 1080

    for i, sec in enumerate(sections):
        slide = Image.new('RGB', (W, H), color='#0f172a') # Dark slate background
        draw = ImageDraw.Draw(slide)

        # Header Banner
        draw.rectangle([(0, 0), (W, 140)], fill='#1e293b')
        draw.line([(0, 140), (W, 140)], fill='#3b82f6', width=4)

        # Title & Subtitle
        draw.text((60, 30), f"Step {sec['id']:02d} / 11: {sec['title']}", fill='#ffffff', font=font_title)
        draw.text((60, 90), sec['subtitle'], fill='#93c5fd', font=font_sub)

        # Right-aligned header metadata
        meta_text = "Analysing Mental Health in Student Ecosystem | Sufiyan Surve"
        draw.text((W - 650, 55), meta_text, fill='#94a3b8', font=font_meta)

        # Left Column: Bullet Points Card
        has_img = sec['img_path'] and os.path.exists(sec['img_path'])
        card_w = 900 if has_img else 1800
        card_h = 780
        card_x = 60
        card_y = 180

        draw.rounded_rectangle([(card_x, card_y), (card_x + card_w, card_y + card_h)], radius=16, fill='#1e293b', outline='#334155', width=2)
        draw.text((card_x + 40, card_y + 40), "KEY ARCHITECTURAL & EMPIRICAL HIGHLIGHTS", fill='#38bdf8', font=font_head)
        draw.line([(card_x + 40, card_y + 90), (card_x + card_w - 40, card_y + 90)], fill='#334155', width=2)

        # Draw bullet points
        y_cursor = card_y + 120
        for bp in sec['bullet_points']:
            # Bullet point indicator
            draw.ellipse([(card_x + 40, y_cursor + 8), (card_x + 54, y_cursor + 22)], fill='#3b82f6')
            
            # Text wrapping for long lines
            words = bp.split(' ')
            line = ""
            for w in words:
                test_line = line + " " + w if line else w
                if len(test_line) * 14 < (card_w - 120):
                    line = test_line
                else:
                    draw.text((card_x + 70, y_cursor), line, fill='#f1f5f9', font=font_body)
                    y_cursor += 40
                    line = w
            if line:
                draw.text((card_x + 70, y_cursor), line, fill='#f1f5f9', font=font_body)
                y_cursor += 55

        # Right Column: Visual Artifact Image (if present)
        if has_img:
            img_x = 1000
            img_y = 180
            img_w = 860
            img_h = 780
            draw.rounded_rectangle([(img_x, img_y), (img_x + img_w, img_y + img_h)], radius=16, fill='#020617', outline='#334155', width=2)
            
            try:
                raw_img = Image.open(sec['img_path'])
                raw_img.thumbnail((img_w - 40, img_h - 40), Image.Resampling.LANCZOS)
                
                # Center inside the frame
                paste_x = img_x + (img_w - raw_img.width) // 2
                paste_y = img_y + (img_h - raw_img.height) // 2
                slide.paste(raw_img, (paste_x, paste_y))
            except Exception as e:
                print(f"Failed to paste image {sec['img_path']}: {e}")

        # Bottom Subtitle / Narration Caption Bar
        draw.rectangle([(0, H - 90), (W, H)], fill='#020617')
        draw.line([(0, H - 90), (W, H - 90)], fill='#1e293b', width=2)
        caption_preview = sec['script'][:160] + "..." if len(sec['script']) > 160 else sec['script']
        draw.text((60, H - 65), f"Narration: \"{caption_preview}\"", fill='#cbd5e1', font=font_meta)

        slide_path = os.path.join(temp_dir, f"slide_{sec['id']:02d}.png")
        slide.save(slide_path)
        slide_images.append(slide_path)
        print(f"Rendered slide {sec['id']:02d} -> {slide_path}")

    # Build individual video clips for each section and concatenate with ffmpeg
    print("Encoding video segments with ffmpeg...")
    clip_files = []
    for i in range(len(sections)):
        sec_id = sections[i]['id']
        slide_p = slide_images[i]
        audio_p = audio_files[i]
        dur = durations[i]
        clip_p = os.path.join(temp_dir, f"clip_{sec_id:02d}.mp4")

        # Encode single image + audio into mp4
        cmd = [
            ffmpeg_exe, "-y",
            "-loop", "1", "-i", slide_p,
            "-i", audio_p,
            "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-t", str(dur),
            clip_p
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        clip_files.append(clip_p)
        print(f"Encoded clip {sec_id:02d} ({dur:.1f}s)")

    # Concatenate all clips
    concat_list_path = os.path.join(temp_dir, 'concat_list.txt')
    with open(concat_list_path, 'w', encoding='utf-8') as f:
        for cp in clip_files:
            # Format: file 'path'
            f.write(f"file '{os.path.abspath(cp)}'\n")

    final_video_path = os.path.join(output_dir, 'project_explanation_video.mp4')
    print(f"Concatenating all {len(clip_files)} segments into final video: {final_video_path}...")

    concat_cmd = [
        ffmpeg_exe, "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list_path,
        "-c", "copy",
        final_video_path
    ]
    subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    final_size = os.path.getsize(final_video_path)
    print(f"SUCCESS! Video created at: {final_video_path}")
    print(f"Final video size: {final_size / (1024*1024):.2f} MB")
    print(f"Final duration: {total_duration / 60:.2f} minutes ({total_duration:.1f} seconds)")

if __name__ == '__main__':
    create_demo_video()
