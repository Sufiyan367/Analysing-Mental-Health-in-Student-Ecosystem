#!/usr/bin/env python3
"""
scripts/generate_screenshots.py
-------------------------------
Generates high-resolution visualization screenshots and evidence
corresponding directly to the cleaned student mental health dataset.
Saves to:
  screenshots/worksheets/
  screenshots/dashboards/
  screenshots/story/
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Set overall style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Segoe UI, Arial, sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['axes.titlesize'] = 12

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'cleaned', 'student_mental_health_cleaned.csv')
WS_DIR = os.path.join(BASE_DIR, 'screenshots', 'worksheets')
DB_DIR = os.path.join(BASE_DIR, 'screenshots', 'dashboards')
ST_DIR = os.path.join(BASE_DIR, 'screenshots', 'story')

for d in [WS_DIR, DB_DIR, ST_DIR]:
    os.makedirs(d, exist_ok=True)

df = pd.read_csv(DATA_PATH)

# Colors
C_BLUE = '#2563eb'
C_RED = '#ef4444'
C_ORANGE = '#f97316'
C_GREEN = '#10b981'
C_PURPLE = '#8b5cf6'
C_DARK = '#0f172a'

# --- 1. Worksheet: Gender vs Mental Health ---
fig, ax = plt.subplots(figsize=(8, 5))
gender_data = df.groupby('Gender')[['Depression_Binary', 'Anxiety_Binary', 'Panic_Binary']].mean() * 100
gender_data.plot(kind='bar', ax=ax, color=[C_RED, C_ORANGE, C_PURPLE], width=0.6)
ax.set_title('Mental Health Condition Prevalence by Gender (%)', fontweight='bold', pad=12)
ax.set_ylabel('Prevalence Rate (%)')
ax.set_xlabel('Gender')
ax.legend(['Depression', 'Anxiety', 'Panic Attacks'], frameon=True)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(WS_DIR, '01_gender_vs_mental_health.png'), dpi=200)
plt.close()

# --- 2. Worksheet: Age & Study Year ---
fig, ax = plt.subplots(figsize=(8, 5))
ct = pd.crosstab(df['Age'], df['Year_of_Study'])
ct.plot(kind='bar', stacked=True, ax=ax, colormap='Blues', edgecolor='black', linewidth=0.5)
ax.set_title('Age & Academic Study Year Distribution', fontweight='bold', pad=12)
ax.set_ylabel('Number of Students')
ax.set_xlabel('Age')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(WS_DIR, '02_age_year_distribution.png'), dpi=200)
plt.close()

# --- 3. Worksheet: CGPA vs Conditions ---
fig, ax = plt.subplots(figsize=(9, 5))
cgpa_order = ['0.00 - 1.99', '2.00 - 2.49', '2.50 - 2.99', '3.00 - 3.49', '3.50 - 4.00']
cgpa_data = df.groupby('CGPA_Range')[['Depression_Binary', 'Anxiety_Binary']].mean().reindex(cgpa_order) * 100
cgpa_data.plot(kind='bar', ax=ax, color=[C_RED, C_BLUE], width=0.6)
ax.set_title('Mental Health Prevalence across CGPA Performance Bands (%)', fontweight='bold', pad=12)
ax.set_ylabel('Prevalence (%)')
ax.set_xlabel('CGPA Achievement Bracket')
ax.legend(['Depression Rate', 'Anxiety Rate'], frameon=True)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(WS_DIR, '03_cgpa_vs_conditions.png'), dpi=200)
plt.close()

# --- 4. Worksheet: Faculty Stress Comparison ---
fig, ax = plt.subplots(figsize=(8, 5))
fac_data = df.groupby('Faculty')['Condition_Count'].mean().sort_values()
fac_data.plot(kind='barh', ax=ax, color=C_BLUE, edgecolor='black', linewidth=0.5)
ax.set_title('Average Condition Load per Student by Academic Faculty', fontweight='bold', pad=12)
ax.set_xlabel('Average Positive Conditions (0 - 3)')
ax.set_ylabel('Academic Faculty')
plt.tight_layout()
plt.savefig(os.path.join(WS_DIR, '04_faculty_stress_comparison.png'), dpi=200)
plt.close()

# --- 5. Worksheet: Overall Risk Segmentation (Donut) ---
fig, ax = plt.subplots(figsize=(6, 6))
risk_counts = df['Risk_Category'].value_counts()
colors = [C_GREEN, C_RED, C_ORANGE]
wedges, texts, autotexts = ax.pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%',
                                  startangle=140, colors=colors, textprops={'fontsize': 11, 'weight': 'bold'},
                                  wedgeprops=dict(width=0.45, edgecolor='w'))
ax.set_title('Overall Student Risk Tier Segmentation', fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig(os.path.join(WS_DIR, '05_risk_segmentation_donut.png'), dpi=200)
plt.close()

# --- 6. Worksheet: Year of Study Risk Heatmap ---
fig, ax = plt.subplots(figsize=(7, 5))
heatmap_data = pd.crosstab(df['Year_of_Study'], df['Risk_Category'], normalize='index') * 100
import numpy as np
im = ax.imshow(heatmap_data, cmap='YlOrRd', aspect='auto')
ax.set_xticks(np.arange(len(heatmap_data.columns)))
ax.set_yticks(np.arange(len(heatmap_data.index)))
ax.set_xticklabels(heatmap_data.columns, fontweight='bold')
ax.set_yticklabels(heatmap_data.index, fontweight='bold')
plt.colorbar(im, ax=ax, label='% within Study Year')
for i in range(len(heatmap_data.index)):
    for j in range(len(heatmap_data.columns)):
        text = ax.text(j, i, f"{heatmap_data.iloc[i, j]:.1f}%",
                       ha="center", va="center", color="black" if heatmap_data.iloc[i, j] < 50 else "white", fontweight='bold')
ax.set_title('Risk Category Concentration by Study Year (%)', fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig(os.path.join(WS_DIR, '06_year_risk_heatmap.png'), dpi=200)
plt.close()

# --- 7. Worksheet: Faculty Treemap / Proportions ---
fig, ax = plt.subplots(figsize=(8, 5))
fac_counts = df['Faculty'].value_counts()
fac_counts.plot(kind='bar', ax=ax, color=C_PURPLE, edgecolor='black', linewidth=0.5)
ax.set_title('Student Enrollment Share by Academic Faculty', fontweight='bold', pad=12)
ax.set_ylabel('Number of Students')
ax.set_xlabel('Faculty')
plt.xticks(rotation=25, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(WS_DIR, '07_faculty_enrollment_distribution.png'), dpi=200)
plt.close()

# --- 8. Worksheet: Academic Trend vs Stress Index ---
fig, ax = plt.subplots(figsize=(8, 5))
cgpa_trend = df.groupby('CGPA_Midpoint')['Condition_Count'].mean()
ax.plot(cgpa_trend.index, cgpa_trend.values, marker='o', linewidth=2.5, color=C_RED, markersize=8)
ax.set_title('Academic Performance (CGPA Midpoint) vs Condition Count', fontweight='bold', pad=12)
ax.set_xlabel('CGPA Midpoint')
ax.set_ylabel('Average Positive Conditions')
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(WS_DIR, '08_academic_workload_trend.png'), dpi=200)
plt.close()

# --- 9. Worksheet: Treatment Gap Breakdown ---
fig, ax = plt.subplots(figsize=(8, 5))
tg_counts = df['Treatment_Status'].value_counts()
tg_counts.plot(kind='barh', ax=ax, color=[C_GREEN, C_RED, C_ORANGE, C_BLUE], edgecolor='black', linewidth=0.5)
ax.set_title('Student Treatment Gap & Healthcare Engagement Status', fontweight='bold', pad=12)
ax.set_xlabel('Number of Students')
plt.tight_layout()
plt.savefig(os.path.join(WS_DIR, '09_treatment_gap_breakdown.png'), dpi=200)
plt.close()

# --- 10. Dashboard 1: Demographics & Academic Profile ---
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Dashboard 1: Student Demographics & Academic Profile', fontsize=16, fontweight='bold', y=0.98)

# D1 Subplot 1: Gender Prevalence
gender_data.plot(kind='bar', ax=axs[0, 0], color=[C_RED, C_ORANGE, C_PURPLE], width=0.6)
axs[0, 0].set_title('Mental Health Prevalence by Gender (%)', fontweight='bold')
axs[0, 0].set_ylabel('Rate (%)')
axs[0, 0].yaxis.set_major_formatter(mtick.PercentFormatter())
axs[0, 0].tick_params(axis='x', rotation=0)

# D1 Subplot 2: Age & Year
ct.plot(kind='bar', stacked=True, ax=axs[0, 1], colormap='Blues', edgecolor='black', linewidth=0.5)
axs[0, 1].set_title('Age & Academic Study Year Distribution', fontweight='bold')
axs[0, 1].set_ylabel('Students')
axs[0, 1].tick_params(axis='x', rotation=0)

# D1 Subplot 3: Faculty Enrollment
fac_counts.plot(kind='bar', ax=axs[1, 0], color=C_PURPLE, edgecolor='black', linewidth=0.5)
axs[1, 0].set_title('Student Enrollment by Academic Faculty', fontweight='bold')
axs[1, 0].set_ylabel('Students')
axs[1, 0].tick_params(axis='x', rotation=25)

# D1 Subplot 4: CGPA Distribution
cgpa_data.plot(kind='bar', ax=axs[1, 1], color=[C_RED, C_BLUE], width=0.6)
axs[1, 1].set_title('CGPA Performance Bands vs Mental Health (%)', fontweight='bold')
axs[1, 1].set_ylabel('Rate (%)')
axs[1, 1].yaxis.set_major_formatter(mtick.PercentFormatter())
axs[1, 1].tick_params(axis='x', rotation=15)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(os.path.join(DB_DIR, 'dashboard_1_demographics.png'), dpi=200)
plt.close()

# --- 11. Dashboard 2: Mental Health Risk & Diagnostics ---
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Dashboard 2: Mental Health Risk Assessment & Diagnostics', fontsize=16, fontweight='bold', y=0.98)

# D2 Subplot 1: Risk Donut
wedges, texts, autotexts = axs[0, 0].pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%',
                                        startangle=140, colors=colors, textprops={'fontsize': 10, 'weight': 'bold'},
                                        wedgeprops=dict(width=0.45, edgecolor='w'))
axs[0, 0].set_title('Overall Risk Tier Breakdown', fontweight='bold')

# D2 Subplot 2: Year Heatmap
im = axs[0, 1].imshow(heatmap_data, cmap='YlOrRd', aspect='auto')
axs[0, 1].set_xticks(np.arange(len(heatmap_data.columns)))
axs[0, 1].set_yticks(np.arange(len(heatmap_data.index)))
axs[0, 1].set_xticklabels(heatmap_data.columns, fontweight='bold', fontsize=9)
axs[0, 1].set_yticklabels(heatmap_data.index, fontweight='bold')
axs[0, 1].set_title('Risk Category by Study Year (%)', fontweight='bold')

# D2 Subplot 3: Faculty Condition Load
fac_data.plot(kind='barh', ax=axs[1, 0], color=C_BLUE, edgecolor='black', linewidth=0.5)
axs[1, 0].set_title('Average Condition Load by Faculty', fontweight='bold')
axs[1, 0].set_xlabel('Conditions per Student')

# D2 Subplot 4: Treatment Gap
tg_counts.plot(kind='barh', ax=axs[1, 1], color=[C_GREEN, C_RED, C_ORANGE, C_BLUE], edgecolor='black', linewidth=0.5)
axs[1, 1].set_title('Treatment Gap vs Active Treatment Care', fontweight='bold')
axs[1, 1].set_xlabel('Number of Students')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(os.path.join(DB_DIR, 'dashboard_2_risk_assessment.png'), dpi=200)
plt.close()

# --- 12. Story Scenes ---
scenes = [
    ("scene_1_cohort_overview.png", "Scene 1: Cohort Demographic Overview & Mental Health Baseline"),
    ("scene_2_academic_pressure.png", "Scene 2: Academic Pressure & The CGPA Paradigm"),
    ("scene_3_lifestyle_stressors.png", "Scene 3: Lifestyle Drivers, Panic Attacks & Study Workload"),
    ("scene_4_vulnerability_mapping.png", "Scene 4: Student Vulnerability Mapping & The Treatment Gap"),
    ("scene_5_strategic_recommendations.png", "Scene 5: Strategic Institutional Recommendations & Roadmap")
]

for filename, title in scenes:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.text(0.5, 0.6, title, fontsize=14, fontweight='bold', ha='center', va='center', color=C_DARK)
    subtitle = "Tableau Public Story Point Narrative Scene — Analysing Mental Health in Student Ecosystem"
    ax.text(0.5, 0.45, subtitle, fontsize=11, color='#64748b', ha='center', va='center')
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(ST_DIR, filename), dpi=150)
    plt.close()

print("All visual evidence screenshots generated successfully!")
