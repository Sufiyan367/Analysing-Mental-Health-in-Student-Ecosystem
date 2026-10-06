"""
Generate 8 Unique Dataset-Grounded Visualizations for Mental Health in Student Ecosystem
Using exclusively data/cleaned/mental_health_student_ecosystem_cleaned.csv
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set style aesthetics
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

# Ensure output directory exists
output_dir = 'evidence/visualizations'
os.makedirs(output_dir, exist_ok=True)

# Load dataset
csv_path = 'data/cleaned/mental_health_student_ecosystem_cleaned.csv'
df = pd.read_csv(csv_path)
print(f"Loaded dataset: {df.shape[0]} rows, {df.shape[1]} columns.")

# Colors
PRIMARY = '#2b5c8f'
ACCENT_HIGH = '#d9534f'
ACCENT_MED = '#f0ad4e'
ACCENT_LOW = '#5cb85c'
PALETTE_STRESS = {'Low': ACCENT_LOW, 'Medium': ACCENT_MED, 'High': ACCENT_HIGH}

# ==============================================================================
# Visualization 1: Stress Level Distribution
# ==============================================================================
plt.figure(figsize=(8, 5))
stress_counts = df['Stress Level'].value_counts()[['Low', 'Medium', 'High']]
bars = plt.bar(stress_counts.index, stress_counts.values, color=[PALETTE_STRESS[x] for x in stress_counts.index], width=0.55, edgecolor='#333333', linewidth=0.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f'{yval} ({yval/len(df)*100:.1f}%)', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.title('Visualization 1: Stress Level Distribution Across Student Cohort', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Stress Level', fontsize=11, fontweight='bold')
plt.ylabel('Student Count (Count of User ID)', fontsize=11, fontweight='bold')
plt.ylim(0, max(stress_counts.values) + 15)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '01_stress_level_distribution.png'), dpi=300)
plt.close()
print("Saved 01_stress_level_distribution.png")

# ==============================================================================
# Visualization 2: Stress Level vs Anxiety Score
# ==============================================================================
plt.figure(figsize=(8, 5))
stress_anxiety = df.groupby('Stress Level')['Anxiety Score'].mean().loc[['Low', 'Medium', 'High']]
bars = plt.bar(stress_anxiety.index, stress_anxiety.values, color=[PALETTE_STRESS[x] for x in stress_anxiety.index], width=0.55, edgecolor='#333333', linewidth=0.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1.2, f'{yval:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.title('Visualization 2: Average Anxiety Score by Stress Level', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Stress Level', fontsize=11, fontweight='bold')
plt.ylabel('Average Anxiety Score (Scale 0–100)', fontsize=11, fontweight='bold')
plt.ylim(0, 85)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '02_stress_vs_anxiety.png'), dpi=300)
plt.close()
print("Saved 02_stress_vs_anxiety.png")

# ==============================================================================
# Visualization 3: Stress Level vs Depression Score
# ==============================================================================
plt.figure(figsize=(8, 5))
stress_depression = df.groupby('Stress Level')['Depression Score'].mean().loc[['Low', 'Medium', 'High']]
bars = plt.bar(stress_depression.index, stress_depression.values, color=[PALETTE_STRESS[x] for x in stress_depression.index], width=0.55, edgecolor='#333333', linewidth=0.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1.2, f'{yval:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.title('Visualization 3: Average Depression Score by Stress Level', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Stress Level', fontsize=11, fontweight='bold')
plt.ylabel('Average Depression Score (Scale 0–100)', fontsize=11, fontweight='bold')
plt.ylim(0, 80)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '03_stress_vs_depression.png'), dpi=300)
plt.close()
print("Saved 03_stress_vs_depression.png")

# ==============================================================================
# Visualization 4: Average Stress Level / Mental Health Scores by Gender
# ==============================================================================
plt.figure(figsize=(9, 5))
gender_metrics = df.groupby('Gender')[['Anxiety Score', 'Depression Score']].mean()
# Ensure ordered: Female, Male, Other
gender_order = [g for g in ['Female', 'Male', 'Other'] if g in gender_metrics.index]
gender_metrics = gender_metrics.loc[gender_order]

x = np.arange(len(gender_order))
width = 0.35

rects1 = plt.bar(x - width/2, gender_metrics['Anxiety Score'], width, label='Average Anxiety Score', color='#3470a3', edgecolor='#333333', linewidth=0.5)
rects2 = plt.bar(x + width/2, gender_metrics['Depression Score'], width, label='Average Depression Score', color='#e06d53', edgecolor='#333333', linewidth=0.5)

for bar in rects1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1.0, f'{yval:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
for bar in rects2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1.0, f'{yval:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.title('Visualization 4: Mental Health Burden Comparison by Gender', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Gender Identity', fontsize=11, fontweight='bold')
plt.ylabel('Average Psychometric Score', fontsize=11, fontweight='bold')
plt.xticks(x, gender_order, fontsize=11)
plt.ylim(0, 65)
plt.legend(frameon=True, facecolor='white', loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '04_gender_mental_health_comparison.png'), dpi=300)
plt.close()
print("Saved 04_gender_mental_health_comparison.png")

# ==============================================================================
# Visualization 5: Sleep Quality vs Stress Level
# ==============================================================================
plt.figure(figsize=(9, 5.5))
ct = pd.crosstab(df['Sleep Quality'], df['Stress Level'])[['Low', 'Medium', 'High']].loc[['Good', 'Average', 'Poor']]

bottom = np.zeros(len(ct))
colors_list = [ACCENT_LOW, ACCENT_MED, ACCENT_HIGH]
labels = ['Low Stress', 'Medium Stress', 'High Stress']

for i, col in enumerate(['Low', 'Medium', 'High']):
    values = ct[col].values
    bars = plt.bar(ct.index, values, bottom=bottom, label=labels[i], color=colors_list[i], width=0.5, edgecolor='#333333', linewidth=0.5)
    for j, (val, b) in enumerate(zip(values, bottom)):
        if val > 0:
            plt.text(j, b + val/2.0, f'{val}', ha='center', va='center', color='white' if col == 'High' else '#222222', fontweight='bold', fontsize=11)
    bottom += values

plt.title('Visualization 5: Sleep Quality vs Stress Level Distribution (Stacked Bar)', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Sleep Quality Category', fontsize=11, fontweight='bold')
plt.ylabel('Student Count (Count of User ID)', fontsize=11, fontweight='bold')
plt.ylim(0, 105)
plt.legend(title='Stress Tier', frameon=True, facecolor='white', loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '05_sleep_quality_vs_stress.png'), dpi=300)
plt.close()
print("Saved 05_sleep_quality_vs_stress.png")

# ==============================================================================
# Visualization 6: Screen Time vs Stress Level
# ==============================================================================
plt.figure(figsize=(8, 5))
stress_screen = df.groupby('Stress Level')['Daily Screen Time (hrs)'].mean().loc[['Low', 'Medium', 'High']]
bars = plt.bar(stress_screen.index, stress_screen.values, color=[PALETTE_STRESS[x] for x in stress_screen.index], width=0.55, edgecolor='#333333', linewidth=0.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.15, f'{yval:.2f} hrs', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.title('Visualization 6: Average Daily Screen Time by Stress Level', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Stress Level', fontsize=11, fontweight='bold')
plt.ylabel('Average Daily Screen Time (Hours/Day)', fontsize=11, fontweight='bold')
plt.ylim(0, 10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '06_screen_time_vs_stress.png'), dpi=300)
plt.close()
print("Saved 06_screen_time_vs_stress.png")

# ==============================================================================
# Visualization 7: Mental Health History Distribution
# ==============================================================================
plt.figure(figsize=(7, 6))
history_counts = df['Mental Health History'].value_counts()[['No', 'Yes']]
colors = ['#4a90e2', '#e67e22']
wedges, texts, autotexts = plt.pie(
    history_counts, 
    labels=['No Prior History', 'Has Prior History'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'antialiased': True},
    pctdistance=0.75,
    textprops={'fontsize': 11, 'fontweight': 'bold'}
)

# Draw circle for Donut chart
centre_circle = plt.Circle((0,0), 0.55, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Label inside donut
plt.text(0, 0, f"Total\n{len(df)}\nStudents", ha='center', va='center', fontsize=11, fontweight='bold', color='#333333')

plt.title('Visualization 7: Mental Health History Prevalence (Donut Chart)', fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '07_mental_health_history_distribution.png'), dpi=300)
plt.close()
print("Saved 07_mental_health_history_distribution.png")

# ==============================================================================
# Visualization 8: Therapy Type vs Progress Score
# ==============================================================================
plt.figure(figsize=(9, 5.5))
therapy_df = df[df['Therapy Type'] != 'No Therapy']
therapy_progress = therapy_df.groupby('Therapy Type')['Progress Score'].mean().sort_values(ascending=True)

y_pos = np.arange(len(therapy_progress))
bars = plt.barh(y_pos, therapy_progress.values, color='#2c7bb6', height=0.55, edgecolor='#333333', linewidth=0.5)

for bar in bars:
    xval = bar.get_width()
    plt.text(xval + 0.8, bar.get_y() + bar.get_height()/2.0, f'{xval:.2f}', ha='left', va='center', fontsize=11, fontweight='bold')

plt.yticks(y_pos, therapy_progress.index, fontsize=11, fontweight='bold')
plt.title('Visualization 8: Ranked Therapy Efficacy by Average Progress Score', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Average Progress Score (Improvement Post-Intervention)', fontsize=11, fontweight='bold')
plt.ylabel('Therapeutic Intervention Type', fontsize=11, fontweight='bold')
plt.xlim(0, 48)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '08_therapy_type_vs_progress.png'), dpi=300)
plt.close()
print("Saved 08_therapy_type_vs_progress.png")

print("All 8 visualizations successfully generated.")
