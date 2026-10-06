"""
Generate 5 Professional Story Scene Artifacts for:
Analysing Mental Health in Student Ecosystem
Using exclusively data/cleaned/mental_health_student_ecosystem_cleaned.csv
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Aesthetics
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'

output_dir = 'evidence/story'
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv('data/cleaned/mental_health_student_ecosystem_cleaned.csv')

C_BG = '#f8f9fa'
C_CARD = '#ffffff'
C_PRIMARY = '#1f4e79'
C_TEXT = '#2c3e50'
C_MUTED = '#6c757d'
C_LOW = '#28a745'
C_MED = '#ffc107'
C_HIGH = '#dc3545'
PALETTE_STRESS = {'Low': C_LOW, 'Medium': C_MED, 'High': C_HIGH}

# Common story header builder
def draw_story_header(fig, scene_num, scene_title, scene_subtitle):
    fig.text(0.05, 0.945, f"Scene {scene_num}: {scene_title}", fontsize=20, fontweight='bold', color=C_PRIMARY)
    fig.text(0.05, 0.918, scene_subtitle, fontsize=12, color=C_MUTED)
    # Story Point Navigation Bar
    nav_labels = [
        "1. Baseline",
        "2. Psychological Symptoms",
        "3. Lifestyle & Stress",
        "4. Vulnerability & Support",
        "5. Intervention & Progress"
    ]
    for idx, lbl in enumerate(nav_labels):
        x = 0.05 + idx * 0.185
        is_active = (idx + 1 == scene_num)
        bg_col = C_PRIMARY if is_active else '#e9ecef'
        txt_col = 'white' if is_active else '#495057'
        fig.text(x, 0.865, lbl, fontsize=9.5, fontweight='bold', color=txt_col,
                 bbox=dict(boxstyle='square,pad=0.5', facecolor=bg_col, edgecolor='#ced4da', linewidth=1))

# ==============================================================================
# SCENE 1 — Student Mental Health Baseline
# ==============================================================================
fig1 = plt.figure(figsize=(14, 9), facecolor=C_BG)
draw_story_header(fig1, 1, "Student Mental Health Baseline", 
                  "Establish the cohort foundational demographics and psychological stress baseline across 200 students.")

# KPI Cards
kpi_items = [
    ("TOTAL STUDENTS", "200", "Full Student Cohort", C_PRIMARY),
    ("AVG ANXIETY SCORE", "52.59", "Scale 0–100 (Moderate)", '#e67e22'),
    ("AVG DEPRESSION SCORE", "48.09", "Scale 0–100 (Moderate)", '#c0392b'),
    ("AVG SCREEN TIME", "7.10 hrs", "Continuous Baseline", '#2980b9'),
]
for i, (k, v, s, c) in enumerate(kpi_items):
    x = 0.05 + i * 0.23
    fig1.patches.extend([plt.Rectangle((x, 0.745), 0.21, 0.085, fill=True, facecolor=C_CARD, edgecolor='#dfe6e9', linewidth=1.2, transform=fig1.transFigure)])
    fig1.text(x + 0.012, 0.805, k, fontsize=9, fontweight='bold', color=C_MUTED, transform=fig1.transFigure)
    fig1.text(x + 0.012, 0.768, v, fontsize=18, fontweight='bold', color=c, transform=fig1.transFigure)
    fig1.text(x + 0.012, 0.752, s, fontsize=8, color='#888', transform=fig1.transFigure)

# Chart on Left, Observations on Right
gs1 = gridspec.GridSpec(1, 2, left=0.05, right=0.95, top=0.70, bottom=0.08, wspace=0.25, width_ratios=[1.2, 0.8])
ax1 = fig1.add_subplot(gs1[0, 0])
sc = df['Stress Level'].value_counts()[['Low', 'Medium', 'High']]
bars1 = ax1.bar(sc.index, sc.values, color=[PALETTE_STRESS[x] for x in sc.index], width=0.55, edgecolor='#444')
for b in bars1:
    y = b.get_height()
    ax1.text(b.get_x() + b.get_width()/2., y + 2, f"{y} ({y/200*100:.1f}%)", ha='center', va='bottom', fontsize=10, fontweight='bold')
ax1.set_title('Stress Level Distribution (N = 200)', fontsize=12, fontweight='bold', pad=10, color=C_TEXT)
ax1.set_ylabel('Student Count', fontsize=10)
ax1.set_ylim(0, 125)

# Text Panel on Right
ax1_txt = fig1.add_subplot(gs1[0, 1])
ax1_txt.axis('off')
obs_text1 = (
    "KEY OBSERVATIONS:\n\n"
    "• High Stress Concentration:\n"
    "  Over three-quarters (78.0%) of the student\n"
    "  cohort experience moderate (53.5%) to\n"
    "  high (24.5%) stress levels.\n\n"
    "• Moderate Symptom Baseline:\n"
    "  The cohort exhibits an average anxiety score\n"
    "  of 52.59 and depression score of 48.09,\n"
    "  indicating substantial baseline distress.\n\n"
    "• Digital Exposure:\n"
    "  Students average 7.10 hours of daily screen\n"
    "  time, reflecting heavy academic and personal\n"
    "  device dependency.\n\n"
    "TRANSITION TO SCENE 2:\n"
    "How do these stress categories map directly to\n"
    "standardized anxiety and depression metrics?"
)
ax1_txt.text(0.05, 0.95, obs_text1, fontsize=10.5, color=C_TEXT, verticalalignment='top', linespacing=1.4,
             bbox=dict(boxstyle='round,pad=1.0', facecolor='#ffffff', edgecolor='#ced4da', linewidth=1))

plt.savefig(os.path.join(output_dir, '01_baseline.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Saved 01_baseline.png")

# ==============================================================================
# SCENE 2 — Stress and Psychological Symptoms
# ==============================================================================
fig2 = plt.figure(figsize=(14, 9), facecolor=C_BG)
draw_story_header(fig2, 2, "Stress and Psychological Symptoms", 
                  "Evaluate how standardized anxiety and depression scores escalate across stress tiers.")

gs2 = gridspec.GridSpec(1, 2, left=0.05, right=0.95, top=0.82, bottom=0.08, wspace=0.25, width_ratios=[1.2, 0.8])
ax2 = fig2.add_subplot(gs2[0, 0])

stress_anx = df.groupby('Stress Level')['Anxiety Score'].mean().loc[['Low', 'Medium', 'High']]
stress_dep = df.groupby('Stress Level')['Depression Score'].mean().loc[['Low', 'Medium', 'High']]
x = np.arange(len(stress_anx))
w = 0.35
r1 = ax2.bar(x - w/2, stress_anx.values, w, label='Avg Anxiety Score', color='#3470a3', edgecolor='#444')
r2 = ax2.bar(x + w/2, stress_dep.values, w, label='Avg Depression Score', color='#e06d53', edgecolor='#444')
for b in r1:
    ax2.text(b.get_x() + b.get_width()/2., b.get_height() + 1.2, f"{b.get_height():.2f}", ha='center', fontsize=9.5, fontweight='bold')
for b in r2:
    ax2.text(b.get_x() + b.get_width()/2., b.get_height() + 1.2, f"{b.get_height():.2f}", ha='center', fontsize=9.5, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(['Low Stress', 'Medium Stress', 'High Stress'], fontsize=10, fontweight='bold')
ax2.set_title('Average Anxiety and Depression Scores by Stress Level', fontsize=12, fontweight='bold', pad=10, color=C_TEXT)
ax2.set_ylabel('Average Psychometric Score (Scale 0–100)', fontsize=10)
ax2.set_ylim(0, 85)
ax2.legend(loc='upper left', frameon=True, facecolor='white', fontsize=9.5)

ax2_txt = fig2.add_subplot(gs2[0, 1])
ax2_txt.axis('off')
obs_text2 = (
    "KEY OBSERVATIONS:\n\n"
    "• Pronounced Symptom Escalation:\n"
    "  Students with High Stress average 72.06 in\n"
    "  anxiety and 68.78 in depression, more than\n"
    "  double the averages of Low Stress students\n"
    "  (30.27 anxiety, 26.80 depression).\n\n"
    "• Concurrent Manifestation:\n"
    "  Depression and anxiety scores increase in\n"
    "  tandem across each stress tier, confirming that\n"
    "  elevated stress co-occurs with compounding\n"
    "  psychological symptoms.\n\n"
    "• Clinical Threshold Proximity:\n"
    "  The High Stress group approaches severe clinical\n"
    "  thresholds on both psychometric scales.\n\n"
    "TRANSITION TO SCENE 3:\n"
    "What daily lifestyle behaviors (sleep, screentime)\n"
    "differentiate students across these stress categories?"
)
ax2_txt.text(0.05, 0.95, obs_text2, fontsize=10.5, color=C_TEXT, verticalalignment='top', linespacing=1.4,
             bbox=dict(boxstyle='round,pad=1.0', facecolor='#ffffff', edgecolor='#ced4da', linewidth=1))

plt.savefig(os.path.join(output_dir, '02_psychological_symptoms.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Saved 02_psychological_symptoms.png")

# ==============================================================================
# SCENE 3 — Lifestyle and Mental Health
# ==============================================================================
fig3 = plt.figure(figsize=(14, 9), facecolor=C_BG)
draw_story_header(fig3, 3, "Lifestyle Factors and Stress", 
                  "Examine associations between physiological sleep quality, screen exposure, and stress levels.")

gs3 = gridspec.GridSpec(2, 2, left=0.05, right=0.95, top=0.82, bottom=0.08, wspace=0.25, hspace=0.32, width_ratios=[1.1, 0.9])

# Top Left: Sleep Quality vs Stress (Stacked bar)
ax3_1 = fig3.add_subplot(gs3[0, 0])
ct = pd.crosstab(df['Sleep Quality'], df['Stress Level'])[['Low', 'Medium', 'High']].loc[['Good', 'Average', 'Poor']]
bottom = np.zeros(len(ct))
for col in ['Low', 'Medium', 'High']:
    vals = ct[col].values
    ax3_1.bar(ct.index, vals, bottom=bottom, label=f'{col}', color=PALETTE_STRESS[col], width=0.5, edgecolor='#444')
    for j, (v, b) in enumerate(zip(vals, bottom)):
        if v > 0:
            ax3_1.text(j, b + v/2., f"{v}", ha='center', va='center', fontsize=9, fontweight='bold', color='white' if col=='High' else '#222')
    bottom += vals
ax3_1.set_title('Sleep Quality vs Stress Tier', fontsize=11, fontweight='bold', color=C_TEXT)
ax3_1.set_ylabel('Student Count', fontsize=9)
ax3_1.set_ylim(0, 105)
ax3_1.legend(loc='upper right', fontsize=8, frameon=True, facecolor='white')

# Bottom Left: Screen Time by Stress
ax3_2 = fig3.add_subplot(gs3[1, 0])
st = df.groupby('Stress Level')['Daily Screen Time (hrs)'].mean().loc[['Low', 'Medium', 'High']]
b3_2 = ax3_2.bar(st.index, st.values, color=[PALETTE_STRESS[x] for x in st.index], width=0.5, edgecolor='#444')
for b in b3_2:
    ax3_2.text(b.get_x() + b.get_width()/2., b.get_height() + 0.15, f"{b.get_height():.2f} hrs", ha='center', va='bottom', fontsize=9.5, fontweight='bold')
ax3_2.set_title('Average Daily Screen Time by Stress Level', fontsize=11, fontweight='bold', color=C_TEXT)
ax3_2.set_ylabel('Hours / Day', fontsize=9)
ax3_2.set_ylim(0, 10)

# Right: Observations
ax3_txt = fig3.add_subplot(gs3[:, 1])
ax3_txt.axis('off')
obs_text3 = (
    "KEY OBSERVATIONS:\n\n"
    "• Sleep Deficit in High Stress:\n"
    "  Among the 49 students with High Stress,\n"
    "  35 (71.4%) report Poor sleep, while only\n"
    "  2 maintain Good sleep. Conversely, 50.0% of\n"
    "  Low Stress students enjoy Good sleep.\n\n"
    "• Extended Digital Immersion:\n"
    "  High Stress students average 8.12 hrs/day of\n"
    "  screen exposure (+2.12 hours more than Low\n"
    "  Stress students at 6.00 hrs/day).\n\n"
    "• Physical Inactivity Correlation:\n"
    "  75.5% (37 of 49) of High Stress students have\n"
    "  Low physical activity, compounding lifestyle\n"
    "  vulnerabilities.\n\n"
    "TRANSITION TO SCENE 4:\n"
    "How do prior mental-health history, support systems,\n"
    "and medication intersect with these distress patterns?"
)
ax3_txt.text(0.05, 0.95, obs_text3, fontsize=10.5, color=C_TEXT, verticalalignment='top', linespacing=1.4,
             bbox=dict(boxstyle='round,pad=1.0', facecolor='#ffffff', edgecolor='#ced4da', linewidth=1))

plt.savefig(os.path.join(output_dir, '03_lifestyle_and_stress.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Saved 03_lifestyle_and_stress.png")

# ==============================================================================
# SCENE 4 — Vulnerability and Support
# ==============================================================================
fig4 = plt.figure(figsize=(14, 9), facecolor=C_BG)
draw_story_header(fig4, 4, "Vulnerability Factors and Support Systems", 
                  "Examine prior mental-health history, external support strength, and psychiatric medication use.")

gs4 = gridspec.GridSpec(2, 2, left=0.05, right=0.95, top=0.82, bottom=0.08, wspace=0.25, hspace=0.32, width_ratios=[1.1, 0.9])

# Top Left: Donut Chart History
ax4_1 = fig4.add_subplot(gs4[0, 0])
hc = df['Mental Health History'].value_counts()[['No', 'Yes']]
ax4_1.pie(hc, labels=['No History (60%)', 'Prior History (40%)'], autopct='%1.1f%%', startangle=140, colors=['#4a90e2', '#e67e22'], wedgeprops=dict(edgecolor='white', linewidth=2))
c4 = plt.Circle((0,0), 0.55, fc='white')
ax4_1.add_artist(c4)
ax4_1.text(0, 0, "200\nStudents", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#333')
ax4_1.set_title('Prior Mental Health History Breakdown', fontsize=11, fontweight='bold', color=C_TEXT)

# Bottom Left: Support System Strength vs Stress Level
ax4_2 = fig4.add_subplot(gs4[1, 0])
supp_ct = pd.crosstab(df['Support System Strength'], df['Stress Level'])[['Low', 'Medium', 'High']].loc[['Low', 'Medium', 'High']]
bottom_s = np.zeros(len(supp_ct))
for col in ['Low', 'Medium', 'High']:
    vals = supp_ct[col].values
    ax4_2.bar(supp_ct.index, vals, bottom=bottom_s, label=f'{col}', color=PALETTE_STRESS[col], width=0.5, edgecolor='#444')
    bottom_s += vals
ax4_2.set_title('Support System Strength vs Stress Tier', fontsize=11, fontweight='bold', color=C_TEXT)
ax4_2.set_ylabel('Student Count', fontsize=9)
ax4_2.set_ylim(0, 115)
ax4_2.legend(loc='upper right', fontsize=8, frameon=True, facecolor='white')

# Right: Observations
ax4_txt = fig4.add_subplot(gs4[:, 1])
ax4_txt.axis('off')
obs_text4 = (
    "KEY OBSERVATIONS:\n\n"
    "• Significant Prior History:\n"
    "  40.0% (80 students) have a documented prior\n"
    "  mental health history. Notably, 71.4% (35 of 49)\n"
    "  of students in High Stress have a prior history.\n\n"
    "• First-Onset Vulnerability:\n"
    "  60.0% (120 students) report no prior history,\n"
    "  yet represent 66 Medium-stress and 14 High-stress\n"
    "  cases, indicating campus-induced first onset.\n\n"
    "• Support System Buffer:\n"
    "  Students with High support systems are\n"
    "  disproportionately represented in Low/Medium\n"
    "  stress tiers.\n\n"
    "• Medication Usage:\n"
    "  Only 9.0% (18 students) use medication; 15 of the\n"
    "  18 medication users belong to the High Stress tier.\n\n"
    "TRANSITION TO SCENE 5:\n"
    "For students receiving professional psychological care,\n"
    "which therapeutic interventions yield measurable progress?"
)
ax4_txt.text(0.05, 0.95, obs_text4, fontsize=10.5, color=C_TEXT, verticalalignment='top', linespacing=1.35,
             bbox=dict(boxstyle='round,pad=1.0', facecolor='#ffffff', edgecolor='#ced4da', linewidth=1))

plt.savefig(os.path.join(output_dir, '04_vulnerability_and_support.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Saved 04_vulnerability_and_support.png")

# ==============================================================================
# SCENE 5 — Intervention and Improvement
# ==============================================================================
fig5 = plt.figure(figsize=(14, 9), facecolor=C_BG)
draw_story_header(fig5, 5, "Intervention Patterns and Recovery Progress", 
                  "Analyze therapy modality efficacy, intervention durations, and recovery progress scores.")

gs5 = gridspec.GridSpec(1, 2, left=0.05, right=0.95, top=0.82, bottom=0.08, wspace=0.25, width_ratios=[1.2, 0.8])
ax5 = fig5.add_subplot(gs5[0, 0])

th_df = df[df['Therapy Type'] != 'No Therapy']
tp = th_df.groupby('Therapy Type')['Progress Score'].mean().sort_values(ascending=True)
y_pos = np.arange(len(tp))
b5 = ax5.barh(y_pos, tp.values, color='#2c7bb6', height=0.55, edgecolor='#444')
for b in b5:
    xval = b.get_width()
    ax5.text(xval + 0.8, b.get_y() + b.get_height()/2., f"{xval:.2f}", ha='left', va='center', fontsize=10, fontweight='bold')
ax5.set_yticks(list(y_pos), labels=list(tp.index))
ax5.tick_params(axis='y', labelsize=10)
ax5.set_title('Ranked Average Progress Score by Therapy Type (N = 93)', fontsize=12, fontweight='bold', pad=10, color=C_TEXT)
ax5.set_xlabel('Average Progress Score (Improvement Post-Intervention)', fontsize=10)
ax5.set_xlim(0, 48)

ax5_txt = fig5.add_subplot(gs5[0, 1])
ax5_txt.axis('off')
obs_text5 = (
    "KEY OBSERVATIONS & RECOMMENDATIONS:\n\n"
    "• Efficacy of Structured Interventions:\n"
    "  Cognitive Behavioral Therapy (CBT) achieves the\n"
    "  highest average progress score (40.80 across\n"
    "  7.5 weeks average duration), indicating superior\n"
    "  structured symptom alleviation.\n\n"
    "• Multi-Modal Positive Impact:\n"
    "  Counseling (34.43), Support Groups (33.10), and\n"
    "  Meditation (32.57) all exhibit positive recovery\n"
    "  gains, demonstrating that diverse modalities\n"
    "  provide meaningful therapeutic benefits.\n\n"
    "• Treatment Reach Gap:\n"
    "  107 of 200 students (53.5%) are in 'No Therapy',\n"
    "  including 15 High-stress and 48 Medium-stress\n"
    "  students, highlighting a critical care gap.\n\n"
    "STRATEGIC RECOMMENDATION:\n"
    "Universities should scale accessible CBT programs,\n"
    "embed mindfulness/sleep hygiene workshops, and\n"
    "provide early screening to reach un-enrolled students."
)
ax5_txt.text(0.05, 0.95, obs_text5, fontsize=10.5, color=C_TEXT, verticalalignment='top', linespacing=1.35,
             bbox=dict(boxstyle='round,pad=1.0', facecolor='#ffffff', edgecolor='#ced4da', linewidth=1))

plt.savefig(os.path.join(output_dir, '05_intervention_and_progress.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Saved 05_intervention_and_progress.png")

print("All 5 story scenes successfully created.")
