"""
Generate Responsive Dashboard Prototypes for:
Student Mental Health Analysis Dashboard
Using exclusively data/cleaned/mental_health_student_ecosystem_cleaned.csv
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Set aesthetics
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'

output_dir = 'evidence/dashboard'
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv('data/cleaned/mental_health_student_ecosystem_cleaned.csv')

# Colors
C_BG = '#f4f6f9'
C_CARD = '#ffffff'
C_PRIMARY = '#1f4e79'
C_TEXT = '#2c3e50'
C_MUTED = '#6c757d'
C_LOW = '#28a745'
C_MED = '#ffc107'
C_HIGH = '#dc3545'
PALETTE_STRESS = {'Low': C_LOW, 'Medium': C_MED, 'High': C_HIGH}

# KPIs calculated from data
kpi_total = len(df)
kpi_anxiety = df['Anxiety Score'].mean()
kpi_depression = df['Depression Score'].mean()
kpi_screentime = df['Daily Screen Time (hrs)'].mean()

# ==============================================================================
# 1. DESKTOP DASHBOARD (1920x1080 style / 16:9 ratio, 4 columns grid)
# ==============================================================================
fig = plt.figure(figsize=(18, 11), facecolor=C_BG)

# Title & Subtitle banner
fig.text(0.04, 0.955, "Student Mental Health Analysis Dashboard", fontsize=24, fontweight='bold', color=C_PRIMARY)
fig.text(0.04, 0.932, "Mental health, lifestyle and intervention analysis across the student ecosystem | N = 200 Students", fontsize=13, color=C_MUTED)

# Filter Bar indication
fig.text(0.04, 0.898, "Active Global Filters:  [ Gender: All ]   [ Occupation: All ]   [ Stress Level: All ]   [ Sleep Quality: All ]   [ Therapy Type: All ]", fontsize=11, fontweight='bold', color='#495057', bbox=dict(boxstyle='round,pad=0.5', facecolor='#e9ecef', edgecolor='#ced4da'))

# KPI Cards (Top Row)
kpis = [
    ("TOTAL STUDENTS", f"{kpi_total}", "Full Cohort Sample", C_PRIMARY),
    ("AVG ANXIETY SCORE", f"{kpi_anxiety:.2f}", "Scale: 0–100 (Moderate)", '#e67e22'),
    ("AVG DEPRESSION SCORE", f"{kpi_depression:.2f}", "Scale: 0–100 (Moderate)", '#c0392b'),
    ("AVG DAILY SCREEN TIME", f"{kpi_screentime:.2f} hrs", "Baseline: 3.0–12.0 hrs/day", '#2980b9'),
]

kpi_xs = [0.04, 0.28, 0.52, 0.76]
kpi_w = 0.20

for i, (label, val, sub, col) in enumerate(kpis):
    # draw background box
    fig.patches.extend([plt.Rectangle((kpi_xs[i], 0.805), kpi_w, 0.075, fill=True, facecolor=C_CARD, edgecolor='#dfe6e9', linewidth=1.2, transform=fig.transFigure, zorder=1)])
    fig.text(kpi_xs[i] + 0.015, 0.86, label, fontsize=10, fontweight='bold', color=C_MUTED, transform=fig.transFigure, zorder=2)
    fig.text(kpi_xs[i] + 0.015, 0.825, val, fontsize=20, fontweight='bold', color=col, transform=fig.transFigure, zorder=2)
    fig.text(kpi_xs[i] + 0.015, 0.812, sub, fontsize=9, color='#888888', transform=fig.transFigure, zorder=2)

# Create 2x3 Grid for 6 core visualizations
gs = gridspec.GridSpec(2, 3, left=0.04, right=0.96, top=0.77, bottom=0.05, hspace=0.32, wspace=0.22)

# Chart 1: Stress Level Distribution
ax1 = fig.add_subplot(gs[0, 0])
sc = df['Stress Level'].value_counts()[['Low', 'Medium', 'High']]
b1 = ax1.bar(sc.index, sc.values, color=[PALETTE_STRESS[x] for x in sc.index], width=0.55, edgecolor='#444')
for b in b1:
    y = b.get_height()
    ax1.text(b.get_x() + b.get_width()/2., y + 1.5, f"{y} ({y/200*100:.1f}%)", ha='center', va='bottom', fontsize=9, fontweight='bold')
ax1.set_title('1. Stress Level Distribution', fontsize=12, fontweight='bold', pad=8, color=C_TEXT)
ax1.set_ylabel('Student Count', fontsize=10)
ax1.set_ylim(0, 125)

# Chart 2: Stress vs Anxiety & Depression
ax2 = fig.add_subplot(gs[0, 1])
stress_anx = df.groupby('Stress Level')['Anxiety Score'].mean().loc[['Low', 'Medium', 'High']]
stress_dep = df.groupby('Stress Level')['Depression Score'].mean().loc[['Low', 'Medium', 'High']]
x = np.arange(len(stress_anx))
w = 0.35
r1 = ax2.bar(x - w/2, stress_anx.values, w, label='Avg Anxiety', color='#3470a3', edgecolor='#444')
r2 = ax2.bar(x + w/2, stress_dep.values, w, label='Avg Depression', color='#e06d53', edgecolor='#444')
for b in r1:
    ax2.text(b.get_x() + b.get_width()/2., b.get_height() + 1.2, f"{b.get_height():.1f}", ha='center', fontsize=9, fontweight='bold')
for b in r2:
    ax2.text(b.get_x() + b.get_width()/2., b.get_height() + 1.2, f"{b.get_height():.1f}", ha='center', fontsize=9, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(['Low', 'Medium', 'High'])
ax2.set_title('2. Stress vs Anxiety & Depression Scores', fontsize=12, fontweight='bold', pad=8, color=C_TEXT)
ax2.set_ylabel('Average Score (0–100)', fontsize=10)
ax2.set_ylim(0, 85)
ax2.legend(loc='upper left', fontsize=9, frameon=True, facecolor='white')

# Chart 3: Sleep Quality vs Stress Level
ax3 = fig.add_subplot(gs[0, 2])
ct = pd.crosstab(df['Sleep Quality'], df['Stress Level'])[['Low', 'Medium', 'High']].loc[['Good', 'Average', 'Poor']]
bottom = np.zeros(len(ct))
for col in ['Low', 'Medium', 'High']:
    vals = ct[col].values
    ax3.bar(ct.index, vals, bottom=bottom, label=f'{col} Stress', color=PALETTE_STRESS[col], width=0.5, edgecolor='#444')
    for j, (v, b) in enumerate(zip(vals, bottom)):
        if v > 0:
            ax3.text(j, b + v/2., f"{v}", ha='center', va='center', fontsize=9, fontweight='bold', color='white' if col=='High' else '#222')
    bottom += vals
ax3.set_title('3. Sleep Quality vs Stress Tier', fontsize=12, fontweight='bold', pad=8, color=C_TEXT)
ax3.set_ylabel('Student Count', fontsize=10)
ax3.set_ylim(0, 105)
ax3.legend(loc='upper right', fontsize=8, frameon=True, facecolor='white')

# Chart 4: Screen Time vs Stress Level
ax4 = fig.add_subplot(gs[1, 0])
st = df.groupby('Stress Level')['Daily Screen Time (hrs)'].mean().loc[['Low', 'Medium', 'High']]
b4 = ax4.bar(st.index, st.values, color=[PALETTE_STRESS[x] for x in st.index], width=0.55, edgecolor='#444')
for b in b4:
    y = b.get_height()
    ax4.text(b.get_x() + b.get_width()/2., y + 0.15, f"{y:.2f}h", ha='center', va='bottom', fontsize=9, fontweight='bold')
ax4.set_title('4. Daily Screen Time by Stress Level', fontsize=12, fontweight='bold', pad=8, color=C_TEXT)
ax4.set_ylabel('Avg Screen Time (Hours/Day)', fontsize=10)
ax4.set_ylim(0, 10)

# Chart 5: Mental Health History Prevalence (Donut)
ax5 = fig.add_subplot(gs[1, 1])
hc = df['Mental Health History'].value_counts()[['No', 'Yes']]
wedges, texts, autotexts = ax5.pie(hc, labels=['No History', 'Prior History'], autopct='%1.1f%%', startangle=140, colors=['#4a90e2', '#e67e22'], wedgeprops=dict(edgecolor='white', linewidth=2), pctdistance=0.75)
for at in autotexts:
    at.set_fontsize(9)
    at.set_fontweight('bold')
centre = plt.Circle((0,0), 0.55, fc='white')
ax5.add_artist(centre)
ax5.text(0, 0, f"Total\n200", ha='center', va='center', fontsize=10, fontweight='bold', color='#333')
ax5.set_title('5. Mental Health History Prevalence', fontsize=12, fontweight='bold', pad=8, color=C_TEXT)

# Chart 6: Therapy Type vs Progress Score
ax6 = fig.add_subplot(gs[1, 2])
th_df = df[df['Therapy Type'] != 'No Therapy']
tp = th_df.groupby('Therapy Type')['Progress Score'].mean().sort_values(ascending=True)
y_pos = np.arange(len(tp))
b6 = ax6.barh(y_pos, tp.values, color='#2c7bb6', height=0.55, edgecolor='#444')
for b in b6:
    xval = b.get_width()
    ax6.text(xval + 0.8, b.get_y() + b.get_height()/2., f"{xval:.1f}", ha='left', va='center', fontsize=9, fontweight='bold')
ax6.set_yticks(y_pos)
ax6.set_yticklabels(tp.index, fontsize=9, fontweight='bold')
ax6.set_title('6. Ranked Therapy Efficacy (Progress Score)', fontsize=12, fontweight='bold', pad=8, color=C_TEXT)
ax6.set_xlabel('Average Progress Score (Improvement)', fontsize=10)
ax6.set_xlim(0, 48)

# Save desktop layout
plt.savefig(os.path.join(output_dir, 'desktop_dashboard.png'), dpi=200, bbox_inches='tight')
# Also save as main student_mental_health_dashboard.png
plt.savefig(os.path.join(output_dir, 'student_mental_health_dashboard.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Saved desktop_dashboard.png and student_mental_health_dashboard.png")

# ==============================================================================
# 2. TABLET DASHBOARD (1024x768 portrait / 2-column layout)
# ==============================================================================
fig_tab = plt.figure(figsize=(12, 14), facecolor=C_BG)

fig_tab.text(0.05, 0.965, "Student Mental Health Analysis Dashboard", fontsize=18, fontweight='bold', color=C_PRIMARY)
fig_tab.text(0.05, 0.948, "Tablet View (2-Column Responsive Layout) | N = 200 Students", fontsize=11, color=C_MUTED)

# 2x2 KPI grid for tablet
t_kpis = [
    ("TOTAL STUDENTS", f"{kpi_total}", C_PRIMARY),
    ("AVG ANXIETY", f"{kpi_anxiety:.2f}", '#e67e22'),
    ("AVG DEPRESSION", f"{kpi_depression:.2f}", '#c0392b'),
    ("AVG SCREEN TIME", f"{kpi_screentime:.2f}h", '#2980b9'),
]
for i, (lbl, val, col) in enumerate(t_kpis):
    col_idx = i % 2
    row_idx = i // 2
    x_pos = 0.05 + col_idx * 0.46
    y_pos_kpi = 0.88 - row_idx * 0.055
    fig_tab.patches.extend([plt.Rectangle((x_pos, y_pos_kpi), 0.44, 0.048, fill=True, facecolor=C_CARD, edgecolor='#dfe6e9', linewidth=1, transform=fig_tab.transFigure)])
    fig_tab.text(x_pos + 0.02, y_pos_kpi + 0.026, lbl, fontsize=9, fontweight='bold', color=C_MUTED, transform=fig_tab.transFigure)
    fig_tab.text(x_pos + 0.02, y_pos_kpi + 0.008, val, fontsize=15, fontweight='bold', color=col, transform=fig_tab.transFigure)

gs_tab = gridspec.GridSpec(3, 2, left=0.05, right=0.95, top=0.76, bottom=0.04, hspace=0.35, wspace=0.25)

# C1: Stress Distribution
ax1_t = fig_tab.add_subplot(gs_tab[0, 0])
b1_t = ax1_t.bar(sc.index, sc.values, color=[PALETTE_STRESS[x] for x in sc.index], width=0.55, edgecolor='#444')
for b in b1_t:
    ax1_t.text(b.get_x() + b.get_width()/2., b.get_height() + 1.5, f"{b.get_height()}", ha='center', fontsize=9, fontweight='bold')
ax1_t.set_title('Stress Level Distribution', fontsize=11, fontweight='bold', color=C_TEXT)
ax1_t.set_ylim(0, 125)

# C2: Anxiety & Depression
ax2_t = fig_tab.add_subplot(gs_tab[0, 1])
r1_t = ax2_t.bar(x - w/2, stress_anx.values, w, label='Anxiety', color='#3470a3', edgecolor='#444')
r2_t = ax2_t.bar(x + w/2, stress_dep.values, w, label='Depression', color='#e06d53', edgecolor='#444')
ax2_t.set_xticks(x)
ax2_t.set_xticklabels(['Low', 'Med', 'High'])
ax2_t.set_title('Stress vs Anxiety & Depression', fontsize=11, fontweight='bold', color=C_TEXT)
ax2_t.legend(loc='upper left', fontsize=8)
ax2_t.set_ylim(0, 85)

# C3: Sleep vs Stress
ax3_t = fig_tab.add_subplot(gs_tab[1, 0])
bottom_t = np.zeros(len(ct))
for col in ['Low', 'Medium', 'High']:
    vals = ct[col].values
    ax3_t.bar(ct.index, vals, bottom=bottom_t, label=f'{col}', color=PALETTE_STRESS[col], width=0.5, edgecolor='#444')
    bottom_t += vals
ax3_t.set_title('Sleep Quality vs Stress', fontsize=11, fontweight='bold', color=C_TEXT)
ax3_t.legend(loc='upper right', fontsize=8)
ax3_t.set_ylim(0, 105)

# C4: Screen Time
ax4_t = fig_tab.add_subplot(gs_tab[1, 1])
b4_t = ax4_t.bar(st.index, st.values, color=[PALETTE_STRESS[x] for x in st.index], width=0.55, edgecolor='#444')
for b in b4_t:
    ax4_t.text(b.get_x() + b.get_width()/2., b.get_height() + 0.15, f"{b.get_height():.1f}h", ha='center', fontsize=9, fontweight='bold')
ax4_t.set_title('Screen Time by Stress Tier', fontsize=11, fontweight='bold', color=C_TEXT)
ax4_t.set_ylim(0, 10)

# C5: Mental Health History
ax5_t = fig_tab.add_subplot(gs_tab[2, 0])
ax5_t.pie(hc, labels=['No History', 'Prior History'], autopct='%1.1f%%', startangle=140, colors=['#4a90e2', '#e67e22'], wedgeprops=dict(edgecolor='white', linewidth=2))
centre_t = plt.Circle((0,0), 0.55, fc='white')
ax5_t.add_artist(centre_t)
ax5_t.text(0, 0, "200", ha='center', va='center', fontsize=10, fontweight='bold')
ax5_t.set_title('Mental Health History', fontsize=11, fontweight='bold', color=C_TEXT)

# C6: Therapy Efficacy
ax6_t = fig_tab.add_subplot(gs_tab[2, 1])
ax6_t.barh(y_pos, tp.values, color='#2c7bb6', height=0.55, edgecolor='#444')
ax6_t.set_yticks(list(y_pos), labels=list(tp.index))
ax6_t.tick_params(axis='y', labelsize=8)
ax6_t.set_title('Therapy Efficacy (Progress)', fontsize=11, fontweight='bold', color=C_TEXT)
ax6_t.set_xlim(0, 48)

plt.savefig(os.path.join(output_dir, 'tablet_dashboard.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Saved tablet_dashboard.png")

# ==============================================================================
# 3. MOBILE DASHBOARD (Vertical single-column stacked layout)
# ==============================================================================
fig_mob = plt.figure(figsize=(7, 18), facecolor=C_BG)

fig_mob.text(0.06, 0.975, "Student Mental Health Dashboard", fontsize=15, fontweight='bold', color=C_PRIMARY)
fig_mob.text(0.06, 0.963, "Mobile View (Stacked Layout) | N = 200", fontsize=9, color=C_MUTED)

# Vertical KPI Stack
for i, (lbl, val, col) in enumerate(t_kpis):
    y_pos_k = 0.925 - i * 0.032
    fig_mob.patches.extend([plt.Rectangle((0.06, y_pos_k), 0.88, 0.026, fill=True, facecolor=C_CARD, edgecolor='#dfe6e9', linewidth=1, transform=fig_mob.transFigure)])
    fig_mob.text(0.09, y_pos_k + 0.007, lbl, fontsize=8, fontweight='bold', color=C_MUTED, transform=fig_mob.transFigure)
    fig_mob.text(0.70, y_pos_k + 0.007, val, fontsize=11, fontweight='bold', color=col, transform=fig_mob.transFigure)

gs_mob = gridspec.GridSpec(5, 1, left=0.08, right=0.92, top=0.78, bottom=0.03, hspace=0.45)

# Mobile 1: Stress Distribution
ax1_m = fig_mob.add_subplot(gs_mob[0, 0])
b1_m = ax1_m.bar(sc.index, sc.values, color=[PALETTE_STRESS[x] for x in sc.index], width=0.55, edgecolor='#444')
for b in b1_m:
    ax1_m.text(b.get_x() + b.get_width()/2., b.get_height() + 1.5, f"{b.get_height()}", ha='center', fontsize=8, fontweight='bold')
ax1_m.set_title('1. Stress Level Distribution', fontsize=10, fontweight='bold', color=C_TEXT)
ax1_m.set_ylim(0, 125)

# Mobile 2: Stress vs Anxiety
ax2_m = fig_mob.add_subplot(gs_mob[1, 0])
r1_m = ax2_m.bar(x - w/2, stress_anx.values, w, label='Anxiety', color='#3470a3', edgecolor='#444')
r2_m = ax2_m.bar(x + w/2, stress_dep.values, w, label='Depression', color='#e06d53', edgecolor='#444')
ax2_m.set_xticks(x)
ax2_m.set_xticklabels(['Low', 'Med', 'High'])
ax2_m.set_title('2. Anxiety & Depression by Stress', fontsize=10, fontweight='bold', color=C_TEXT)
ax2_m.set_ylim(0, 85)
ax2_m.legend(fontsize=7, loc='upper left')

# Mobile 3: Sleep Quality
ax3_m = fig_mob.add_subplot(gs_mob[2, 0])
bottom_m = np.zeros(len(ct))
for col in ['Low', 'Medium', 'High']:
    vals = ct[col].values
    ax3_m.bar(ct.index, vals, bottom=bottom_m, label=col, color=PALETTE_STRESS[col], width=0.5, edgecolor='#444')
    bottom_m += vals
ax3_m.set_title('3. Sleep Quality vs Stress Tier', fontsize=10, fontweight='bold', color=C_TEXT)
ax3_m.set_ylim(0, 105)
ax3_m.legend(fontsize=7, loc='upper right')

# Mobile 4: Screen Time
ax4_m = fig_mob.add_subplot(gs_mob[3, 0])
b4_m = ax4_m.bar(st.index, st.values, color=[PALETTE_STRESS[x] for x in st.index], width=0.55, edgecolor='#444')
for b in b4_m:
    ax4_m.text(b.get_x() + b.get_width()/2., b.get_height() + 0.15, f"{b.get_height():.1f}h", ha='center', fontsize=8, fontweight='bold')
ax4_m.set_title('4. Daily Screen Time by Stress', fontsize=10, fontweight='bold', color=C_TEXT)
ax4_m.set_ylim(0, 10)

# Mobile 5: Therapy Progress
ax6_m = fig_mob.add_subplot(gs_mob[4, 0])
ax6_m.barh(y_pos, tp.values, color='#2c7bb6', height=0.55, edgecolor='#444')
ax6_m.set_yticks(list(y_pos), labels=list(tp.index))
ax6_m.tick_params(axis='y', labelsize=8)
ax6_m.set_title('5. Ranked Therapy Efficacy', fontsize=10, fontweight='bold', color=C_TEXT)
ax6_m.set_xlim(0, 48)

plt.savefig(os.path.join(output_dir, 'mobile_dashboard.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Saved mobile_dashboard.png")

print("All responsive dashboard prototypes generated successfully.")
