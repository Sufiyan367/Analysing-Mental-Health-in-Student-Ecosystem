"""
Generate 6-Minute End-to-End Project Demonstration Video
Calibrated strictly to 6:00 - 6:30 minutes (SkillWallet 5-7 min requirement).
Synthesizes professional narration via pyttsx3, renders 1920x1080 16:9 slides
using real project evidence, and encodes into evidence/demo/project_explanation_video.mp4.
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
            "script": "Hello everyone. My name is Sufiyan Surve, and this is the project demonstration for my capstone project: Analysing Mental Health in Student Ecosystem, completed as part of the Data Analytics with Tableau Virtual Internship on SkillWallet by SmartBridge. In this presentation, I walk you through our complete analytics pipeline: problem formulation, data preparation, Tableau visual storytelling, performance benchmarking, and web integration in Python Flask.",
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
            "script": "University students worldwide face increasing rates of psychological distress, academic burnout, and emotional fatigue. Traditionally, higher education institutions rely on reactive counseling services, discovering student struggles only after academic crisis. The objective of this project is to build an empirical diagnostic framework. By analyzing standardized anxiety and depression metrics alongside daily lifestyle habits, we provide university leadership with actionable, data-driven wellness interventions.",
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
            "script": "Our analysis is grounded strictly in the validated Student Mental Health Ecosystem Dataset, consisting of 200 student records across 18 standardized variables. The schema captures three dimensions: demographics like Age and Gender, psychometrics including self-reported Stress Level, Anxiety Score, and Depression Score, and lifestyle factors including Sleep Quality, Daily Screen Time, Physical Activity, Mental Health History, Therapy Type, Intervention Duration, and Progress Score. No external demo metrics were fabricated.",
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
            "script": "Data hygiene is foundational to trustworthy analytics. Prior to visualization, the dataset underwent an exhaustive integrity audit. We confirmed all 200 User IDs are unique, spanning STU 0001 through STU 0200. Zero missing values exist across all 3,600 data points. Continuous metrics strictly obey valid clinical boundaries, and categorical entries are normalized. Certified visualization-ready, the clean dataset occupies 19.84 kilobytes on disk and parses in under 0.65 milliseconds.",
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
            "script": "In the Data Visualization stage, we created eight unique, dataset-grounded visualizations: 1. Stress Level Distribution, establishing baseline cohort spread. 2. Stress Level versus Anxiety Score, and 3. Stress Level versus Depression Score, showing progressive symptom surges. 4. Gender Mental Health Comparison. 5. Sleep Quality versus Stress, capturing restfulness deficits. 6. Screen Time versus Stress. 7. Mental Health History Prevalence. And 8. Ranked Therapy Efficacy, measuring recovery progress scores across clinical modalities.",
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
            "script": "Next, we integrated these findings into an executive multi-device dashboard architecture. The layout features 4 top-level KPI cards: 200 Total Students, Average Anxiety of 52.59, Average Depression of 48.09, and Daily Screen Time of 7.10 hours. Beneath the KPIs, six core panels provide synchronized visual diagnostics. Crucially, we authored responsive layouts for Desktop at 1920 by 1080, Tablet in a 2-column format, and Mobile in a vertical scroll stack, ensuring cross-platform usability.",
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
            "script": "To guide decision-makers through an intuitive diagnostic journey, we structured a 5-Scene Tableau Data Story. Scene 1 establishes the Cohort Baseline, showing that 78 percent of students suffer from moderate or high stress. Scene 2 reveals Symptom Escalation, proving high-stress students face a greater than 135 percent surge in anxiety and depression. Scene 3 demonstrates that 71.4 percent of high-stress students experience poor sleep. Scene 4 uncovers that 60 percent are first-onset cases, and Scene 5 proves Cognitive Behavioral Therapy yields the highest recovery progress at 40.80.",
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
            "script": "In Performance Testing, we executed comprehensive ingestion and filter benchmarks. Local benchmarks proved sub-millisecond parsing latency of 0.64 milliseconds for the 19.84 kilobyte dataset, with multi-predicate filtering executing in 0.86 to 1.41 milliseconds. We engineered and documented 10 production calculation fields, including Average Anxiety, Average Depression, Therapy Active Indicator, and High-Risk Sleep Deficit Flags, with exact formulas for native Tableau authoring. The dataset consumes less than 0.0013 percent of Tableau Public capacity.",
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
            "script": "For web integration, we built a production-grade Python Flask web application. It serves four primary routes: the Executive Overview, Dashboards, Guided Story, and Methodology. The architecture embeds Tableau views using modern tableau-viz web components and JavaScript API v2. Configurable environment variables TABLEAU_DASHBOARD_URL and TABLEAU_STORY_URL allow instant live cloud embedding, while in the interim, our portal renders responsive prototypes and the 5-scene narrative browser with zero visual degradation.",
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
            "script": "Our empirical analysis reveals four major clinical takeaways: First, elevated stress is widespread, affecting 78 percent of the cohort. Second, high stress couples with severe symptom escalation, driving anxiety to 72.06 and depression to 68.78. Third, behavioral habits compound distress: 71.4 percent of high-stress students experience poor sleep alongside 8.12 hours of screen immersion. Fourth, there is a critical care gap: 53.5 percent receive no therapy, while CBT leads recovery among active recipients with a 40.80 progress score.",
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
            "script": "Based on these diagnostics, we propose three strategic recommendations for university leadership: First, expand accessible Cognitive Behavioral Therapy and counseling capacity. Second, institutionalize digital wellness and sleep hygiene workshops. Third, introduce opt-in mental health screenings during freshman orientation to catch first-onset distress early. Note that native Tableau Public publication remains pending manual browser upload, with all blueprints ready. In conclusion, this capstone delivers an end-to-end reproducible analytical solution. Thank you.",
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

    print(f"Generating narration audio for {len(sections)} sections via pyttsx3 at rate 183...")
    engine = pyttsx3.init()
    engine.setProperty('rate', 183) # 183 wpm calibrated to ~6:20-6:30 mins total

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
        dur = 30.0
        for line in res.stderr.split('\n'):
            if 'Duration:' in line:
                dur_str = line.split('Duration:')[1].split(',')[0].strip()
                parts = dur_str.split(':')
                dur = float(parts[0])*3600 + float(parts[1])*60 + float(parts[2])
                break
        
        # 0.8s padding between sections
        dur += 0.8
        durations.append(dur)
        audio_files.append(wav_path)
        print(f"Section {sec_id:02d}: {dur:.2f}s audio")

    total_duration = sum(durations)
    print(f"Total video planned duration: {total_duration:.2f} seconds ({total_duration/60:.2f} minutes = {int(total_duration//60)}:{int(total_duration%60):02d})")

    # Generate 1920x1080 16:9 Slide Images
    print("Generating high-resolution 1920x1080 video slide frames...")
    slide_images = []

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
            draw.ellipse([(card_x + 40, y_cursor + 8), (card_x + 54, y_cursor + 22)], fill='#3b82f6')
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

    # Clean up temporary build files
    try:
        import shutil
        shutil.rmtree(temp_dir)
        print("Cleaned up temp build directory.")
    except Exception as e:
        print(f"Warning: could not clean temp dir: {e}")

    final_size = os.path.getsize(final_video_path)
    print(f"SUCCESS! Video created at: {final_video_path}")
    print(f"Final video size: {final_size / (1024*1024):.2f} MB")
    print(f"Final duration: {total_duration / 60:.2f} minutes ({total_duration:.1f} seconds = {int(total_duration//60)}:{int(total_duration%60):02d})")

if __name__ == '__main__':
    create_demo_video()
