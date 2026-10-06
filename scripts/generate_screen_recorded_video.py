import asyncio
import os
import time
import subprocess
from playwright.async_api import async_playwright

SECTIONS_CONFIG = [
    {
        "id": "01_intro",
        "audio": "scratch/s01.mp3",
        "description": "Introduction & Problem Statement (Homepage Header & Hero)",
        "actions": "act_intro"
    },
    {
        "id": "02_kpis",
        "audio": "scratch/s02.mp3",
        "description": "Cohort KPIs & Baseline Spread",
        "actions": "act_kpis"
    },
    {
        "id": "03_methodology",
        "audio": "scratch/s03.mp3",
        "description": "Methodology & 18-Variable Schema Integrity",
        "actions": "act_methodology"
    },
    {
        "id": "04_dashboard",
        "audio": "scratch/s04.mp3",
        "description": "Executive Diagnostic Dashboard & Stress Correlations",
        "actions": "act_dashboard"
    },
    {
        "id": "05_scene1",
        "audio": "scratch/s05_scene1.mp3",
        "description": "Story Scene 1 - Baseline Stress Spread",
        "actions": "act_scene1"
    },
    {
        "id": "06_scene2",
        "audio": "scratch/s05_scene2.mp3",
        "description": "Story Scene 2 - Anxiety & Depression Escalation",
        "actions": "act_scene2"
    },
    {
        "id": "07_scene3",
        "audio": "scratch/s05_scene3.mp3",
        "description": "Story Scene 3 - Sleep Deficit & Screen Immersion",
        "actions": "act_scene3"
    },
    {
        "id": "08_scene4",
        "audio": "scratch/s05_scene4.mp3",
        "description": "Story Scene 4 - Vulnerability & Support Network Buffer",
        "actions": "act_scene4"
    },
    {
        "id": "09_scene5",
        "audio": "scratch/s05_scene5.mp3",
        "description": "Story Scene 5 - Therapy Progress & Institutional Care Gap",
        "actions": "act_scene5"
    },
    {
        "id": "10_findings",
        "audio": "scratch/s06.mp3",
        "description": "Key Empirical Findings Review",
        "actions": "act_findings"
    },
    {
        "id": "11_conclusion",
        "audio": "scratch/s07.mp3",
        "description": "Strategic Recommendations & Closing",
        "actions": "act_conclusion"
    }
]

INJECT_JS = """() => {
    // Add custom cursor
    if (!document.getElementById('demo-cursor')) {
        const cursor = document.createElement('div');
        cursor.id = 'demo-cursor';
        cursor.style.position = 'fixed';
        cursor.style.width = '32px';
        cursor.style.height = '32px';
        cursor.style.pointerEvents = 'none';
        cursor.style.zIndex = '999999';
        cursor.style.transition = 'left 0.7s cubic-bezier(0.25, 1, 0.5, 1), top 0.7s cubic-bezier(0.25, 1, 0.5, 1), transform 0.2s ease';
        cursor.innerHTML = `<svg width="32" height="32" viewBox="0 0 24 24" fill="none" style="filter: drop-shadow(0 3px 8px rgba(0,0,0,0.5));">
            <path d="M5.5 3.21V20.8c0 .45.54.67.85.35l4.86-4.86a.5.5 0 0 1 .35-.15h6.87c.45 0 .67-.54.35-.85L6.35 2.85a.5.5 0 0 0-.85.36z" fill="#2563eb" stroke="#ffffff" stroke-width="1.8"/>
        </svg>`;
        document.body.appendChild(cursor);
        window.moveCursorTo = (x, y) => {
            cursor.style.left = x + 'px';
            cursor.style.top = y + 'px';
        };
        window.pulseCursor = () => {
            cursor.style.transform = 'scale(0.8)';
            setTimeout(() => { cursor.style.transform = 'scale(1)'; }, 200);
        };
    }

    // Add presenter badge overlay at top right
    if (!document.getElementById('presenter-badge')) {
        const badge = document.createElement('div');
        badge.id = 'presenter-badge';
        badge.style.position = 'fixed';
        badge.style.top = '16px';
        badge.style.right = '24px';
        badge.style.zIndex = '999990';
        badge.style.background = 'rgba(15, 23, 42, 0.88)';
        badge.style.backdropFilter = 'blur(10px)';
        badge.style.border = '1px solid rgba(59, 130, 246, 0.4)';
        badge.style.padding = '8px 18px';
        badge.style.borderRadius = '9999px';
        badge.style.color = '#ffffff';
        badge.style.fontFamily = "'Plus Jakarta Sans', sans-serif";
        badge.style.fontSize = '13px';
        badge.style.fontWeight = '600';
        badge.style.boxShadow = '0 4px 15px rgba(0,0,0,0.2)';
        badge.style.display = 'flex';
        badge.style.alignItems = 'center';
        badge.style.gap = '8px';
        badge.innerHTML = `<span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#10b981; box-shadow:0 0 8px #10b981;"></span>
        <span>Presenter: <strong>Sufiyan Surve</strong> | Student Ecosystem Walkthrough</span>`;
        document.body.appendChild(badge);
    }

    // Smooth scroll helper
    window.smoothScrollTo = (targetY, durationMs) => {
        const startY = window.pageYOffset;
        const diff = targetY - startY;
        const startTime = performance.now();
        function step(now) {
            const elapsed = now - startTime;
            const progress = Math.min(elapsed / durationMs, 1);
            const ease = 0.5 - Math.cos(progress * Math.PI) / 2;
            window.scrollTo(0, startY + diff * ease);
            if (progress < 1) {
                requestAnimationFrame(step);
            }
        }
        requestAnimationFrame(step);
    };
}"""

async def act_intro(page, dur):
    await page.evaluate("window.moveCursorTo(960, 250)")
    await page.wait_for_timeout(3000)
    # Highlight student name & tag
    await page.evaluate("window.moveCursorTo(960, 290)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(4000)
    # Move to title
    await page.evaluate("window.moveCursorTo(800, 360)")
    await page.wait_for_timeout(4000)
    # Move to hero metadata
    await page.evaluate("window.moveCursorTo(640, 460)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(5000)
    # Gentle scroll to peek at KPIs
    await page.evaluate("window.smoothScrollTo(180, 2000)")
    await page.wait_for_timeout(2500)
    await page.evaluate("window.moveCursorTo(960, 520)")

async def act_kpis(page, dur):
    # Scroll to KPI section
    await page.evaluate("window.smoothScrollTo(480, 1800)")
    await page.wait_for_timeout(2000)
    # KPI 1: Cohort Population 200
    await page.evaluate("window.moveCursorTo(490, 620)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(5000)
    # KPI 2: Anxiety 52.59
    await page.evaluate("window.moveCursorTo(800, 620)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # KPI 3: Depression 48.09
    await page.evaluate("window.moveCursorTo(1115, 620)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # KPI 4: Screen Time 7.10 hrs
    await page.evaluate("window.moveCursorTo(1430, 620)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # Center cursor
    await page.evaluate("window.moveCursorTo(960, 620)")

async def act_methodology(page, dur):
    # Scroll directly to methodology section (around y=5100)
    await page.evaluate("window.smoothScrollTo(5100, 2200)")
    await page.wait_for_timeout(2500)
    # Focus table header
    await page.evaluate("window.moveCursorTo(960, 320)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(5000)
    # Demographics row
    await page.evaluate("window.moveCursorTo(700, 450)")
    await page.wait_for_timeout(5000)
    # Psychometrics row
    await page.evaluate("window.moveCursorTo(700, 510)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(5000)
    # Lifestyle habits row
    await page.evaluate("window.moveCursorTo(700, 570)")
    await page.wait_for_timeout(5000)
    # Clinical care row
    await page.evaluate("window.moveCursorTo(700, 630)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(5000)

async def act_dashboard(page, dur):
    # Scroll up to executive dashboard section (around y=720)
    await page.evaluate("window.smoothScrollTo(720, 2500)")
    await page.wait_for_timeout(3000)
    # Dashboard title
    await page.evaluate("window.moveCursorTo(700, 160)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(4000)
    # Point to preview image center
    await page.evaluate("window.moveCursorTo(960, 500)")
    await page.wait_for_timeout(5000)
    # Point to stress distribution chart in dashboard
    await page.evaluate("window.moveCursorTo(650, 460)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # Point to sleep vs stress chart in dashboard
    await page.evaluate("window.moveCursorTo(1250, 460)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # Point to bottom responsive badges
    await page.evaluate("window.moveCursorTo(600, 850)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(5000)

async def act_scene1(page, dur):
    # Scroll to Story Scene 1 (around y=1900)
    await page.evaluate("window.smoothScrollTo(1920, 2000)")
    await page.wait_for_timeout(2500)
    # Point to Scene 1 title
    await page.evaluate("window.moveCursorTo(1150, 320)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(4000)
    # Point to Scene 1 chart
    await page.evaluate("window.moveCursorTo(600, 450)")
    await page.wait_for_timeout(5000)
    # Point to Low, Medium, High bullets
    await page.evaluate("window.moveCursorTo(1150, 440)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(4000)
    await page.evaluate("window.moveCursorTo(1150, 490)")
    await page.wait_for_timeout(4000)

async def act_scene2(page, dur):
    # Scroll to Scene 2 (around y=2400)
    await page.evaluate("window.smoothScrollTo(2400, 1800)")
    await page.wait_for_timeout(2500)
    # Point to Scene 2 title
    await page.evaluate("window.moveCursorTo(1150, 320)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(5000)
    # Point to chart image
    await page.evaluate("window.moveCursorTo(600, 450)")
    await page.wait_for_timeout(6000)
    # Point to Anxiety +138% bullet
    await page.evaluate("window.moveCursorTo(1150, 440)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # Point to Depression +156% bullet
    await page.evaluate("window.moveCursorTo(1150, 480)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)

async def act_scene3(page, dur):
    # Scroll to Scene 3 (around y=2880)
    await page.evaluate("window.smoothScrollTo(2880, 1800)")
    await page.wait_for_timeout(2500)
    # Point to Scene 3 title
    await page.evaluate("window.moveCursorTo(1150, 320)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(4000)
    # Point to Lifestyle chart
    await page.evaluate("window.moveCursorTo(600, 450)")
    await page.wait_for_timeout(5000)
    # Point to 71.4% poor sleep
    await page.evaluate("window.moveCursorTo(1150, 440)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # Point to 8.12 hrs screen time
    await page.evaluate("window.moveCursorTo(1150, 480)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)

async def act_scene4(page, dur):
    # Scroll to Scene 4 (around y=3360)
    await page.evaluate("window.smoothScrollTo(3360, 1800)")
    await page.wait_for_timeout(2500)
    # Point to Scene 4 title
    await page.evaluate("window.moveCursorTo(1150, 320)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(4000)
    # Point to chart
    await page.evaluate("window.moveCursorTo(600, 450)")
    await page.wait_for_timeout(5000)
    # Point to first onset & buffer
    await page.evaluate("window.moveCursorTo(1150, 440)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(5000)
    await page.evaluate("window.moveCursorTo(1150, 490)")
    await page.wait_for_timeout(5000)

async def act_scene5(page, dur):
    # Scroll to Scene 5 (around y=3840)
    await page.evaluate("window.smoothScrollTo(3840, 1800)")
    await page.wait_for_timeout(2500)
    # Point to Scene 5 title
    await page.evaluate("window.moveCursorTo(1150, 320)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(4000)
    # Point to therapy ranking chart
    await page.evaluate("window.moveCursorTo(600, 450)")
    await page.wait_for_timeout(5000)
    # Point to CBT 40.80 progress score
    await page.evaluate("window.moveCursorTo(1150, 440)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # Point to care gap 53.5% no therapy
    await page.evaluate("window.moveCursorTo(1150, 510)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)

async def act_findings(page, dur):
    # Scroll to Key Findings (around y=4350)
    await page.evaluate("window.smoothScrollTo(4350, 2000)")
    await page.wait_for_timeout(2500)
    # Finding 1: Pervasive stress
    await page.evaluate("window.moveCursorTo(540, 420)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # Finding 2: Symptom escalation
    await page.evaluate("window.moveCursorTo(960, 420)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # Finding 3: Behavioral compounding
    await page.evaluate("window.moveCursorTo(1380, 420)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # Finding 4: Institutional care gap
    await page.evaluate("window.moveCursorTo(540, 680)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)

async def act_conclusion(page, dur):
    # Scroll down to CTA & Footer (around y=5600)
    await page.evaluate("window.smoothScrollTo(5600, 2200)")
    await page.wait_for_timeout(2500)
    # Point to CTA banner
    await page.evaluate("window.moveCursorTo(960, 320)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # Point to GitHub repo button
    await page.evaluate("window.moveCursorTo(960, 450)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(6000)
    # Scroll to footer
    await page.evaluate("window.smoothScrollTo(6000, 1500)")
    await page.wait_for_timeout(2000)
    # Point to footer author & Tableau profile
    await page.evaluate("window.moveCursorTo(960, 720)")
    await page.evaluate("window.pulseCursor()")
    await page.wait_for_timeout(8000)

ACTION_MAP = {
    "act_intro": act_intro,
    "act_kpis": act_kpis,
    "act_methodology": act_methodology,
    "act_dashboard": act_dashboard,
    "act_scene1": act_scene1,
    "act_scene2": act_scene2,
    "act_scene3": act_scene3,
    "act_scene4": act_scene4,
    "act_scene5": act_scene5,
    "act_findings": act_findings,
    "act_conclusion": act_conclusion,
}

async def render_all():
    os.makedirs('scratch/clips', exist_ok=True)
    clip_files = []

    for cfg in SECTIONS_CONFIG:
        sec_id = cfg["id"]
        audio_file = cfg["audio"]
        action_fn = ACTION_MAP[cfg["actions"]]
        out_mp4 = f"scratch/clips/{sec_id}.mp4"
        clip_files.append(out_mp4)

        dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', audio_file]).decode().strip())
        print(f"\n==================================================")
        print(f"Rendering {sec_id}: {cfg['description']}")
        print(f"Target duration: {dur:.2f}s")
        print(f"==================================================")

        temp_rec_dir = f"scratch/raw_{sec_id}"
        os.makedirs(temp_rec_dir, exist_ok=True)

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                record_video_dir=temp_rec_dir,
                record_video_size={'width': 1920, 'height': 1080}
            )
            page = await context.new_page()
            await page.goto('https://sufiyan367.github.io/Analysing-Mental-Health-in-Student-Ecosystem/')
            await page.wait_for_timeout(1000)
            await page.evaluate(INJECT_JS)

            start_t = time.time()
            await action_fn(page, dur)
            elapsed = time.time() - start_t
            remaining = dur - elapsed + 0.3
            if remaining > 0:
                await page.wait_for_timeout(int(remaining * 1000))

            await context.close()
            await browser.close()

        # Encode webm to mp4
        webm_files = [f for f in os.listdir(temp_rec_dir) if f.endswith('.webm')]
        if not webm_files:
            raise Exception(f"No webm found for {sec_id}")
        webm_path = os.path.join(temp_rec_dir, webm_files[0])

        cmd = [
            'ffmpeg', '-y',
            '-i', webm_path,
            '-i', audio_file,
            '-c:v', 'libx264', '-preset', 'veryfast', '-pix_fmt', 'yuv420p',
            '-c:a', 'aac', '-b:a', '192k',
            '-shortest',
            out_mp4
        ]
        subprocess.check_call(cmd)
        print(f"Successfully generated {out_mp4}")

    # Concat all clips into final video
    concat_list = "scratch/clips/concat_list.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for c in clip_files:
            f.write(f"file '{os.path.abspath(c).replace(chr(92), '/')}'\n")

    final_mp4 = "evidence/demo/project_explanation_video.mp4"
    docs_mp4 = "docs/evidence/demo/project_explanation_video.mp4"
    os.makedirs("evidence/demo", exist_ok=True)
    os.makedirs("docs/evidence/demo", exist_ok=True)

    print("\nConcatenating all clips...")
    concat_cmd = [
        'ffmpeg', '-y',
        '-f', 'concat', '-safe', '0',
        '-i', concat_list,
        '-c', 'copy',
        final_mp4
    ]
    subprocess.check_call(concat_cmd)
    
    # Mirror copy to docs/
    import shutil
    shutil.copyfile(final_mp4, docs_mp4)
    print(f"Final MP4 produced at {final_mp4} and {docs_mp4}")

if __name__ == '__main__':
    asyncio.run(render_all())
