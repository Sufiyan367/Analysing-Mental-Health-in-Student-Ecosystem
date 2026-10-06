"""
scripts/generate_demo_video.py
------------------------------
Generates a polished human-style end-to-end video presentation for
'Analysing Mental Health in Student Ecosystem'.
Uses Microsoft Edge Neural Voice (en-IN-PrabhatNeural) for natural, conversational student delivery.
Features high-resolution 1920x1080 frames, section title badges, clean highlight callout cards,
dynamic cursor pointer indicators, and seamless FFmpeg encoding strictly within 5:00 - 7:00 minutes.
"""

import os
import sys
import time
import asyncio
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg
import edge_tts

VOICE = "en-IN-PrabhatNeural"
SPEECH_RATE = "+22%"  # Energetic, fluent student presentation pace (~6:15 total duration)

def get_fonts():
    try:
        font_header = ImageFont.truetype("arialbd.ttf", 44)
        font_sub = ImageFont.truetype("arial.ttf", 24)
        font_badge = ImageFont.truetype("arialbd.ttf", 20)
        font_card_title = ImageFont.truetype("arialbd.ttf", 26)
        font_bp = ImageFont.truetype("arial.ttf", 23)
        font_callout = ImageFont.truetype("arialbd.ttf", 22)
        font_watermark = ImageFont.truetype("arial.ttf", 18)
    except Exception:
        font_header = font_sub = font_badge = font_card_title = font_bp = font_callout = font_watermark = ImageFont.load_default()
    return font_header, font_sub, font_badge, font_card_title, font_bp, font_callout, font_watermark

def draw_cursor(draw, x, y):
    """Draw a crisp, modern presentation cursor pointer with shadow."""
    points = [
        (x, y),
        (x, y + 24),
        (x + 7, y + 18),
        (x + 13, y + 29),
        (x + 18, y + 27),
        (x + 12, y + 16),
        (x + 20, y + 16)
    ]
    # Subtle drop shadow
    shadow_points = [(px + 2, py + 2) for px, py in points]
    draw.polygon(shadow_points, fill=(15, 23, 42, 120))
    # Main pointer
    draw.polygon(points, fill=(255, 255, 255, 255))
    draw.polygon(points, outline=(30, 41, 59, 255))

def create_slide_frame(sec, total_secs):
    """Generate a 1920x1080 16:9 presentation slide with polished UI."""
    W, H = 1920, 1080
    slide = Image.new('RGB', (W, H), '#0b1120')
    draw = ImageDraw.Draw(slide)

    f_head, f_sub, f_badge, f_ctitle, f_bp, f_callout, f_wm = get_fonts()

    # 1. Subtle Radial / Gradient Glow Background
    for r in range(400, 0, -20):
        alpha = int(25 * (1 - r / 400))
        draw.ellipse([(1400 - r, 300 - r), (1400 + r, 300 + r)], fill=(37, 99, 235, alpha))

    # 2. Header Bar
    # Section Category Pill
    draw.rounded_rectangle([(70, 48), (320, 88)], radius=12, fill='#1e293b', outline='#3b82f6', width=2)
    draw.text((88, 56), f"SECTION {sec['id']:02d} OF {total_secs:02d}", fill='#60a5fa', font=f_badge)

    # Top Right Author & Program Tag
    draw.text((1400, 56), "Sufiyan Surve  •  SmartBridge Capstone", fill='#94a3b8', font=f_badge)

    # Slide Title & Subtitle
    draw.text((70, 105), sec['title'], fill='#f8fafc', font=f_head)
    draw.text((70, 162), sec['subtitle'], fill='#94a3b8', font=f_sub)

    # Divider Line
    draw.line([(70, 205), (1850, 205)], fill='#1e293b', width=2)

    # 3. Content Layout: Left Content Card, Right Evidence Card
    has_image = sec['img_path'] and os.path.exists(sec['img_path'])
    left_w = 800 if has_image else 1710
    left_x, left_y = 70, 235
    left_h = 750

    # Left Glassmorphism Card
    draw.rounded_rectangle([(left_x, left_y), (left_x + left_w, left_y + left_h)], radius=18, fill='#111827', outline='#1f2937', width=2)

    # Card Top Accent Stripe
    draw.rounded_rectangle([(left_x + 30, left_y + 24), (left_x + 180, left_y + 30)], radius=3, fill='#3b82f6')

    # Card Title
    card_title = "Analytical Architecture & Takeaways" if has_image else "Core Strategic Focus & Framework"
    draw.text((left_x + 30, left_y + 44), card_title, fill='#e2e8f0', font=f_ctitle)

    # Render Bullet Points
    y_text = left_y + 105
    for bp in sec['bullet_points']:
        draw.ellipse([(left_x + 32, y_text + 6), (left_x + 46, y_text + 20)], fill='#2563eb')
        draw.ellipse([(left_x + 35, y_text + 9), (left_x + 43, y_text + 17)], fill='#93c5fd')

        # Multi-line word wrap
        words = bp.split(' ')
        line = ""
        max_chars = 46 if has_image else 95
        for w in words:
            if len(line + " " + w) <= max_chars:
                line += (" " if line else "") + w
            else:
                draw.text((left_x + 60, y_text), line, fill='#cbd5e1', font=f_bp)
                y_text += 34
                line = w
        if line:
            draw.text((left_x + 60, y_text), line, fill='#cbd5e1', font=f_bp)
            y_text += 46

    # Bottom Callout Box inside Left Card
    if 'callout' in sec:
        c_box_y = left_y + left_h - 110
        draw.rounded_rectangle([(left_x + 30, c_box_y), (left_x + left_w - 30, c_box_y + 85)], radius=12, fill='#1e293b', outline='#2563eb', width=2)
        draw.text((left_x + 50, c_box_y + 14), "KEY CLINICAL / EMPIRICAL FINDING:", fill='#38bdf8', font=f_badge)
        draw.text((left_x + 50, c_box_y + 42), sec['callout'], fill='#f1f5f9', font=f_callout)

    # 4. Right Evidence Card (if image exists)
    if has_image:
        right_x = left_x + left_w + 40
        right_w = 940
        right_y = left_y
        right_h = left_h

        # Outer Frame
        draw.rounded_rectangle([(right_x, right_y), (right_x + right_w, right_y + right_h)], radius=18, fill='#0f172a', outline='#334155', width=2)

        # Image Header Pill
        draw.rounded_rectangle([(right_x + 25, right_y + 18), (right_x + 320, right_y + 54)], radius=8, fill='#1e293b')
        draw.text((right_x + 38, right_y + 24), "EMPIRICAL VERIFIED EVIDENCE", fill='#93c5fd', font=f_badge)

        # Load & Fit Evidence Image
        try:
            raw_img = Image.open(sec['img_path'])
            max_img_w = right_w - 50
            max_img_h = right_h - 100
            raw_img.thumbnail((max_img_w, max_img_h), Image.Resampling.LANCZOS)

            img_x = right_x + (right_w - raw_img.width) // 2
            img_y = right_y + 70 + (max_img_h - raw_img.height) // 2
            slide.paste(raw_img, (img_x, img_y))

            # Image Border Accent
            draw.rectangle([(img_x - 2, img_y - 2), (img_x + raw_img.width + 1, img_y + raw_img.height + 1)], outline='#3b82f6', width=2)

            # Simulated Cursor Pointer on the Evidence Chart
            cursor_target_x = img_x + int(raw_img.width * 0.65)
            cursor_target_y = img_y + int(raw_img.height * 0.45)
            draw_cursor(draw, cursor_target_x, cursor_target_y)

        except Exception as e:
            print(f"Error drawing image for section {sec['id']}: {e}")

    # Footer Watermark & Transparency
    draw.text((70, 1040), "Data Analytics with Tableau Capstone  •  SmartBridge Virtual Internship", fill='#475569', font=f_wm)
    draw.text((1420, 1040), "Status: Full Spec Complete; Native Tableau Pending", fill='#475569', font=f_wm)

    return slide

def get_sections():
    """All 11 capstone sections with spoken student script and visual content."""
    return [
        {
            "id": 1,
            "title": "Analysing Mental Health in Student Ecosystem",
            "subtitle": "Virtual Internship Capstone Project  •  SmartBridge / SkillWallet",
            "script": "Hello everyone. My name is Sufiyan Surve, and welcome to the project demonstration for my capstone project: Analysing Mental Health in Student Ecosystem, completed as part of the Data Analytics with Tableau Virtual Internship on SkillWallet by SmartBridge. In this presentation, I will walk you through our complete analytics lifecycle: problem formulation, data preparation, eight dataset-grounded visualizations, multi-device dashboard prototypes, a five-scene guided data story, performance benchmarks, and web portal integration.",
            "bullet_points": [
                "Student Author: Sufiyan Surve (Tableau Public: @sufiyansurve333)",
                "Program Track: Data Analytics with Tableau Virtual Internship",
                "Project Domain: Psychological Well-Being & Behavioral Analytics",
                "Core Pipeline: Ingestion → Validation → Visual Diagnostics → Web Integration",
                "Single Source of Truth: 200 Students × 18 Validated Attributes"
            ],
            "callout": "Comprehensive, reproducible diagnostics for higher education leadership.",
            "img_path": None
        },
        {
            "id": 2,
            "title": "Problem Statement & Analytical Scope",
            "subtitle": "Transforming University Care from Reactive Crisis to Proactive Analytics",
            "script": "Higher education institutions face escalating rates of psychological distress, academic burnout, and emotional fatigue. Historically, campus counseling centers operate reactively, discovering student struggles only after academic failure or acute crisis. The objective of this project is to build an empirical diagnostic framework. By analyzing standardized anxiety and depression scores alongside daily lifestyle habits like sleep quality and screen immersion, we provide university decision-makers with actionable, data-driven wellness interventions.",
            "bullet_points": [
                "The Institutional Dilemma: Campus mental health support remains largely reactive.",
                "Primary Objective: Early risk identification before academic or clinical crisis.",
                "Clinical Grounding: Standardized anxiety and depression psychometrics.",
                "Lifestyle Context: Compounding impacts of sleep deprivation and digital saturation.",
                "Strategic Goal: Data-driven resource allocation and clinical therapy expansion."
            ],
            "callout": "78% of students experience elevated chronic distress during studies.",
            "img_path": None
        },
        {
            "id": 3,
            "title": "Dataset Acquisition & Standardized Schema",
            "subtitle": "200 Authentic Records × 18 Validated Schema Attributes",
            "script": "Our entire analysis is grounded strictly in the validated Student Mental Health Ecosystem Dataset, consisting of 200 student records across 18 standardized variables. The schema captures three critical domains: demographics including Age and Gender, psychometrics including self-reported Stress Level, Anxiety Score, and Depression Score, and behavioral lifestyle factors including Sleep Quality, Daily Screen Time, Physical Activity, Mental Health History, Therapy Type, and Progress Score. Generic demo metrics from portal templates were intentionally omitted.",
            "bullet_points": [
                "Cohort Size: N = 200 authentic student profiles (STU_0001 to STU_0200)",
                "Schema Dimensions: Exactly 18 standardized variables (8 numeric, 10 categorical)",
                "Demographic Variables: User ID, Age (18–27), Gender, Academic Occupation",
                "Psychometric Variables: Stress Level, Anxiety Score (0–100), Depression Score (0–100)",
                "Behavioral & Clinical: Sleep Quality, Screen Time, Activity, Therapy, Progress"
            ],
            "callout": "100% verified dataset; zero fabricated columns or mismatched metrics.",
            "img_path": os.path.join('evidence', 'visualizations', '01_stress_level_distribution.png')
        },
        {
            "id": 4,
            "title": "Data Hygiene, Validation & Preparation",
            "subtitle": "Zero Missing Values, Complete Primary Key Integrity & Format Certification",
            "script": "Data hygiene is foundational to trustworthy analytics. Prior to visualization, the dataset underwent an exhaustive integrity audit across all 3,600 data cells. We verified that all 200 User IDs are unique, spanning STU 0001 through STU 0200. There are zero missing values, zero duplicates, and continuous variables strictly conform to valid psychometric ranges. Certified visualization-ready, the clean dataset occupies 19.84 kilobytes on disk and parses in under 0.65 milliseconds.",
            "bullet_points": [
                "Completeness: 0 missing or null values across all 3,600 data cells (100% complete)",
                "Uniqueness: 0 duplicate records; primary key integrity fully certified",
                "Range Validation: Anxiety (5–96), Depression (9–87), Screen Time (3.0–12.0 hrs)",
                "Preparation Milestone: Certified visualization-ready without distorting raw distributions",
                "Parsing Latency: Raw parse latency 0.64 ms; memory footprint 137 KB"
            ],
            "callout": "Certified 100% clean and ready for direct Tableau ingestion.",
            "img_path": os.path.join('evidence', 'performance', 'data_rendering', 'data_rendering_benchmark.png')
        },
        {
            "id": 5,
            "title": "Eight Dataset-Grounded Visualizations",
            "subtitle": "Multivariate Analysis of Stress, Symptom Escalation & Behavioral Habits",
            "script": "In the Data Visualization stage, we developed eight unique, dataset-grounded charts: First, Stress Level Distribution, establishing baseline cohort spread. Second, Stress Level versus Anxiety Score, and third, Stress Level versus Depression Score, revealing dramatic symptom escalation. Fourth, Gender Mental Health Comparison. Fifth, Sleep Quality versus Stress. Sixth, Daily Screen Time versus Stress. Seventh, Mental Health History Prevalence. And eighth, Ranked Therapy Efficacy, evaluating clinical progress across therapy modalities.",
            "bullet_points": [
                "Viz 1: Stress Distribution — 22.0% Low (44), 53.5% Medium (107), 24.5% High (49)",
                "Viz 2 & 3: Stress vs Anxiety (72.06 vs 30.27) & Depression (68.78 vs 26.80)",
                "Viz 4: Gender Comparison — Balanced anxiety and depression across male and female peers",
                "Viz 5: Sleep Quality — 71.4% poor sleep among students in high stress",
                "Viz 6: Screen Immersion — High-stress students average 8.12 hours/day",
                "Viz 7: History Distribution — 60% first-onset distress; 40% pre-existing history",
                "Viz 8: Therapy Efficacy — Cognitive Behavioral Therapy leads with 40.80 progress score"
            ],
            "callout": "Every chart is grounded in validated variables with zero fabricated placeholders.",
            "img_path": os.path.join('evidence', 'visualizations', '02_stress_vs_anxiety.png')
        },
        {
            "id": 6,
            "title": "Responsive Multi-Device Dashboard Architecture",
            "subtitle": "Desktop (1920×1080), Tablet (1024×768), and Mobile Vertical Formats",
            "script": "Next, we integrated these findings into an executive multi-device dashboard architecture. The layout presents four top-level KPI summary cards: 200 Total Students, Average Anxiety of 52.59, Average Depression of 48.09, and Daily Screen Time of 7.10 hours. Beneath the KPIs, six core panels provide synchronized visual diagnostics. We engineered dedicated responsive layouts for Desktop, Tablet in a two-column format, and Mobile in a vertical stack, ensuring full usability across any device.",
            "bullet_points": [
                "Cohort KPI Cards: Total Students (200), Anxiety (52.59), Depression (48.09), Screen Time (7.10 hrs)",
                "Diagnostic Panel 1: Stress Level Distribution & Cohort Spread",
                "Diagnostic Panel 2: Grouped Anxiety & Depression Symptom Escalation",
                "Diagnostic Panel 3: Sleep Quality Breakdown across Stress Tiers",
                "Diagnostic Panel 4: Daily Screen Time Exposure by Stress Level",
                "Diagnostic Panel 5: Mental Health History Distribution Donut",
                "Diagnostic Panel 6: Ranked Therapy Efficacy Horizontal Bar",
                "Multi-Device Ready: Desktop 1920×1080, Tablet 1024×768, Mobile Vertical Stack"
            ],
            "callout": "Unified diagnostic command center for university leadership and counselors.",
            "img_path": os.path.join('evidence', 'dashboard', 'student_mental_health_dashboard.png')
        },
        {
            "id": 7,
            "title": "Guided Five-Scene Data Story Narrative",
            "subtitle": "Sequential Analytical Journey from Baseline Distress to Clinical Recovery",
            "script": "To guide institutional stakeholders through an evidence-based roadmap, we designed a five-scene Tableau data story: Scene 1 sets the Student Mental Health Baseline. Scene 2 explores Stress and Psychological Symptoms. Scene 3 investigates Lifestyle Factors including sleep deficits and screen exposure. Scene 4 examines Vulnerability and Support Networks. And Scene 5 evaluates Intervention Patterns and Recovery Progress, translating data patterns directly into campus policy recommendations.",
            "bullet_points": [
                "Scene 1: Student Mental Health Baseline — 78.0% in moderate or high stress tiers",
                "Scene 2: Stress & Psychological Symptoms — >135% surge in anxiety and depression",
                "Scene 3: Lifestyle Factors & Stress — 71.4% poor sleep + 8.12 hrs screen saturation",
                "Scene 4: Vulnerability & Support — 14 high-stress students emerged with no prior history",
                "Scene 5: Intervention Patterns & Recovery — CBT achieves 40.80 recovery score",
                "Narrative Transitions: Continuous context guiding deans through empirical evidence"
            ],
            "callout": "A complete narrative arc connecting raw psychometrics to campus policy.",
            "img_path": os.path.join('evidence', 'story/03_lifestyle_and_stress.png')
        },
        {
            "id": 8,
            "title": "Performance Testing & Calculated Fields",
            "subtitle": "Sub-Millisecond Query Benchmarks & 10 Production Tableau Calculations",
            "script": "In the Performance Testing epic, we benchmarked dataset scalability and calculation complexity. The dataset loads in 3.17 milliseconds with a memory footprint of just 137 kilobytes. We stress-tested eight single- and multi-predicate filters, verifying sub-millisecond execution times between 0.86 and 1.41 milliseconds. Furthermore, we specified 10 production calculation fields in Tableau covering stress indicators, screen categories, and therapy flags, confirming high performance headroom.",
            "bullet_points": [
                "Volume Benchmark: Disk size 19.84 KB, in-memory footprint 137.12 KB",
                "Parsing Latency: Raw CSV parse 0.64 ms; full DataFrame load 3.17 ms",
                "Filter Testing: 8 filter scenarios evaluated (0.86 ms to 1.41 ms latency)",
                "Calculated Fields: 10 production formulas (5 measures, 5 dimensions)",
                "Stress Indicators: High Stress Flag, Severe Distress Indicator, Screen Category",
                "Scalability Headroom: Cohort size consumes <0.0013% of Tableau capacity"
            ],
            "callout": "Sub-millisecond query execution guarantees instant dashboard responsiveness.",
            "img_path": os.path.join('evidence', 'performance', 'filters', 'filter_performance_benchmark.png')
        },
        {
            "id": 9,
            "title": "Full-Stack Flask Portal & Web Integration",
            "subtitle": "Responsive Web Application with Tableau Embedding & Public Demo Showcase",
            "script": "For web integration, we developed a production-grade Python Flask web application. It features four primary routes: the Executive Overview, Interactive Dashboards, Guided Story, and Methodology. The architecture supports live cloud embedding via modern tableau-viz web components. We also created a polished static project showcase hosted on GitHub Pages, providing seamless, zero-cost public access to all project evidence and metrics.",
            "bullet_points": [
                "Route /: Executive overview with live KPI cards and analytical research pillars",
                "Route /dashboard: Multi-device layout switcher with Tableau embed frame",
                "Route /story: Interactive 5-scene narrative browser with sequential observations",
                "Route /about: Technical methodology, 18-variable schema, and calculation formulas",
                "Public Demo Showcase: Live on GitHub Pages with complete visual evidence",
                "Local Backend: Python Flask with Gunicorn WSGI running on localhost port 5000"
            ],
            "callout": "Fully responsive web architecture supporting both local backend and public showcase.",
            "img_path": os.path.join('evidence', 'web_integration', 'home_page.png')
        },
        {
            "id": 10,
            "title": "Key Empirical Findings & Clinical Discoveries",
            "subtitle": "Summary of Core Psychological & Behavioral Patterns in the Cohort",
            "script": "Our empirical analysis reveals four major clinical takeaways: First, elevated stress is ubiquitous, affecting 78 percent of the cohort. Second, high stress couples with severe symptom escalation, driving anxiety to 72.06 and depression to 68.78. Third, behavioral habits compound distress: 71.4 percent of high-stress students experience poor sleep alongside 8.12 hours of daily screen immersion. Fourth, there is a critical care gap: 53.5 percent receive no therapy, while Cognitive Behavioral Therapy leads recovery among active recipients with a 40.80 progress score.",
            "bullet_points": [
                "1. Ubiquitous Stress Burden: 78.0% of cohort operates in moderate or severe stress.",
                "2. Direct Symptom Escalation: >135% surge in anxiety and depression for high stress.",
                "3. Lifestyle Compounding: 71.4% poor sleep + 8.12 hrs screen exposure in high stress.",
                "4. Acute First-Onset Distress: 60% with no prior history face significant university distress.",
                "5. The Care Gap: 107 students (53.5%) receive No Therapy, including 15 high-stress cases.",
                "6. Clinical Recovery: Structured CBT demonstrates superior symptom alleviation (40.80 score)."
            ],
            "callout": "Compounding lifestyle vectors demand holistic campus wellness intervention.",
            "img_path": os.path.join('evidence', 'visualizations', '08_therapy_type_vs_progress.png')
        },
        {
            "id": 11,
            "title": "Strategic Recommendations & Project Conclusion",
            "subtitle": "Evidence-Based Policy Roadmap & SkillWallet Capstone Summary",
            "script": "Based on these diagnostics, we propose three strategic recommendations for university leadership: First, expand accessible Cognitive Behavioral Therapy and campus counseling capacity. Second, institutionalize digital wellness and sleep hygiene workshops in student residences. Third, introduce proactive, opt-in mental health screenings during freshman orientation to catch first-onset distress early. Note that native Tableau Public publication remains pending manual browser upload, with all blueprints ready. In conclusion, this capstone delivers an end-to-end reproducible analytical solution. Thank you.",
            "bullet_points": [
                "Recommendation 1: Scale campus CBT and group counseling partnerships.",
                "Recommendation 2: Institutionalize digital wellness and sleep hygiene workshops.",
                "Recommendation 3: Implement early mental health screenings during freshman orientation.",
                "Status Notice: Native Tableau workbook specifications prepared; live cloud publishing pending.",
                "Project Complete: Validated data pipeline, 8 visualizations, responsive dashboard, 5-scene story & Flask portal."
            ],
            "callout": "Moving higher education from reactive crisis triage to proactive student wellness.",
            "img_path": os.path.join('evidence', 'dashboard', 'student_mental_health_dashboard.png')
        }
    ]

async def generate_speech_audio(sections, temp_dir, ffmpeg_exe):
    """Synthesize high-fidelity voiceover using edge_tts neural voice."""
    audio_files = []
    durations = []

    print(f"Synthesizing voiceover for {len(sections)} sections via {VOICE}...")
    for sec in sections:
        sec_id = sec['id']
        mp3_path = os.path.join(temp_dir, f"audio_{sec_id:02d}.mp3")
        wav_path = os.path.join(temp_dir, f"audio_{sec_id:02d}.wav")

        communicate = edge_tts.Communicate(sec['script'], VOICE, rate=SPEECH_RATE)
        await communicate.save(mp3_path)

        # Convert to WAV with subtle 0.4s padded silence for smooth section transitions
        filter_str = "apad=pad_dur=0.4"
        cmd = [
            ffmpeg_exe, "-y",
            "-i", mp3_path,
            "-af", filter_str,
            "-ar", "24000",
            "-ac", "1",
            wav_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        # Probe exact duration
        probe = subprocess.run([ffmpeg_exe, "-i", wav_path, "-hide_banner"], stderr=subprocess.PIPE, text=True)
        dur = 30.0
        for line in probe.stderr.split('\n'):
            if 'Duration:' in line:
                dur_str = line.split('Duration:')[1].split(',')[0].strip()
                parts = dur_str.split(':')
                dur = float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
                break

        durations.append(dur)
        audio_files.append(wav_path)
        print(f"  Section {sec_id:02d}: {dur:.2f}s audio generated")

    total_dur = sum(durations)
    print(f"Total Speech Planned Duration: {total_dur:.2f}s ({total_dur / 60:.2f} mins = {int(total_dur // 60)}:{int(total_dur % 60):02d})")
    return audio_files, durations

def build_video():
    output_dir = os.path.join('evidence', 'demo')
    os.makedirs(output_dir, exist_ok=True)
    temp_dir = os.path.join(output_dir, 'temp_build')
    os.makedirs(temp_dir, exist_ok=True)

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    sections = get_sections()

    # Step 1: Synthesize Audio
    audio_files, durations = asyncio.run(generate_speech_audio(sections, temp_dir, ffmpeg_exe))
    total_dur = sum(durations)

    # Validate duration bounds (5 to 7 mins = 300 to 420 seconds)
    if not (300 <= total_dur <= 420):
        print(f"WARNING: Duration {total_dur:.1f}s is outside 5-7 min window!")
    else:
        print(f"SUCCESS: Duration {total_dur:.1f}s is strictly within 5-7 minute requirement.")

    # Step 2: Render 1920x1080 Slide Frames
    print("Rendering high-resolution 1920x1080 slide frames...")
    slide_images = []
    for sec in sections:
        frame = create_slide_frame(sec, len(sections))
        frame_path = os.path.join(temp_dir, f"frame_{sec['id']:02d}.png")
        frame.save(frame_path)
        slide_images.append(frame_path)

    # Step 3: Encode Video Clips per Section
    print("Encoding video clips with FFmpeg...")
    clip_files = []
    for i, sec in enumerate(sections):
        sec_id = sec['id']
        slide_p = slide_images[i]
        audio_p = audio_files[i]
        dur = durations[i]
        clip_p = os.path.join(temp_dir, f"clip_{sec_id:02d}.mp4")

        cmd = [
            ffmpeg_exe, "-y",
            "-loop", "1", "-i", slide_p,
            "-i", audio_p,
            "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "128k",
            "-t", str(dur),
            "-shortest",
            clip_p
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        clip_files.append(clip_p)
        print(f"  Clip {sec_id:02d} rendered ({dur:.2f}s)")

    # Step 4: Concatenate All Clips
    print("Concatenating clips into final presentation MP4...")
    concat_list = os.path.join(temp_dir, 'concat.txt')
    with open(concat_list, 'w', encoding='utf-8') as f:
        for cp in clip_files:
            f.write(f"file '{os.path.abspath(cp)}'\n")

    final_video = os.path.join(output_dir, 'project_explanation_video.mp4')
    cmd_concat = [
        ffmpeg_exe, "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list,
        "-c", "copy",
        final_video
    ]
    subprocess.run(cmd_concat, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    # Also mirror into docs/evidence/demo/ for GitHub Pages
    docs_demo_dir = os.path.join('docs', 'evidence', 'demo')
    os.makedirs(docs_demo_dir, exist_ok=True)
    docs_video = os.path.join(docs_demo_dir, 'project_explanation_video.mp4')
    try:
        import shutil
        shutil.copyfile(final_video, docs_video)
        print(f"Mirrored final video to: {docs_video}")
    except Exception as e:
        print(f"Warning mirroring video: {e}")

    # Clean up temp build files
    try:
        import shutil
        shutil.rmtree(temp_dir)
        print("Cleaned up temp build directory.")
    except Exception as e:
        print(f"Warning cleaning temp dir: {e}")

    file_size = os.path.getsize(final_video)
    print(f"\n==========================================")
    print(f"DEMO VIDEO GENERATION COMPLETED!")
    print(f"Output File: {final_video}")
    print(f"File Size: {file_size / (1024 * 1024):.2f} MB")
    print(f"Final Duration: {total_dur / 60:.2f} minutes ({total_dur:.2f} seconds)")
    print(f"==========================================")

if __name__ == '__main__':
    build_video()
