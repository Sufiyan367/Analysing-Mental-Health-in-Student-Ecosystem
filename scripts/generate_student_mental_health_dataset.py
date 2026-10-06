import numpy as np
import pandas as pd
import random

# Set random seed for full reproducibility
np.random.seed(42)
random.seed(42)

N = 200

# 1. User ID: Unique identifier
user_ids = [f"STU_{i:04d}" for i in range(1, N + 1)]

# 2. Age: Student ecosystem (undergrad, postgrad, researchers)
# Mean ~21.5, range 18 to 28
ages = np.random.choice(
    [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    size=N,
    p=[0.12, 0.18, 0.22, 0.20, 0.12, 0.06, 0.04, 0.02, 0.02, 0.01, 0.01]
)

# 3. Gender: Male, Female, Other
genders = np.random.choice(["Female", "Male", "Other"], size=N, p=[0.53, 0.43, 0.04])

# 4. Occupation: Realistic student ecosystem roles
occupations = np.random.choice(
    [
        "Undergraduate Student",
        "Postgraduate Student",
        "Doctoral Researcher",
        "Graduate Teaching Assistant",
        "Student Intern"
    ],
    size=N,
    p=[0.55, 0.22, 0.08, 0.07, 0.08]
)

# 5. Daily Screen Time (hrs): 3.0 to 12.0 hours
screen_time = np.round(np.random.normal(loc=7.2, scale=1.8, size=N), 1)
screen_time = np.clip(screen_time, 3.0, 12.0)

# 6. Physical Activity Level: Low, Moderate, High
activity_weights = [0.40, 0.42, 0.18]
activities = np.random.choice(["Low", "Moderate", "High"], size=N, p=activity_weights)

# 7. Sleep Quality: Poor, Average, Good (correlated with screen time and physical activity)
sleep_qualities = []
for st, act in zip(screen_time, activities):
    # base probs
    if st > 8.5 or act == "Low":
        p = [0.55, 0.35, 0.10]
    elif st < 6.0 and act == "High":
        p = [0.10, 0.35, 0.55]
    else:
        p = [0.25, 0.50, 0.25]
    sleep_qualities.append(np.random.choice(["Poor", "Average", "Good"], p=p))

# 8. Mental Health History: Yes/No
history_flags = np.random.choice(["Yes", "No"], size=N, p=[0.38, 0.62])

# 9. Support System Strength: Low, Medium, High
support_systems = np.random.choice(["Low", "Medium", "High"], size=N, p=[0.28, 0.47, 0.25])

# 10. Social Interaction Score: 1 to 10
social_scores = []
for sup in support_systems:
    if sup == "Low":
        s = int(np.clip(np.random.normal(loc=3.8, scale=1.4), 1, 7))
    elif sup == "Medium":
        s = int(np.clip(np.random.normal(loc=6.2, scale=1.3), 3, 9))
    else:
        s = int(np.clip(np.random.normal(loc=8.1, scale=1.1), 5, 10))
    social_scores.append(s)

# 11 & 12. Stress Level, Anxiety Score (0-100), Depression Score (0-100)
stress_levels = []
anxiety_scores = []
depression_scores = []

for sq, act, st, hist, soc in zip(sleep_qualities, activities, screen_time, history_flags, social_scores):
    # Base risk factor calculation
    risk_factor = 0.0
    if sq == "Poor": risk_factor += 24.0
    elif sq == "Average": risk_factor += 10.0
    
    if act == "Low": risk_factor += 12.0
    elif act == "Moderate": risk_factor += 4.0
    
    risk_factor += (st - 5.0) * 2.8
    if hist == "Yes": risk_factor += 16.0
    risk_factor += (10 - soc) * 2.2
    
    # Add random biological/environmental noise
    anx = int(np.clip(risk_factor + np.random.normal(12.0, 7.5), 5, 96))
    dep = int(np.clip(risk_factor * 0.92 + np.random.normal(10.0, 8.0), 4, 94))
    
    # Stress categorization based on composite severity
    composite_distress = (anx + dep) / 2.0
    if composite_distress >= 62.0:
        stress = "High"
    elif composite_distress >= 38.0:
        stress = "Medium"
    else:
        stress = "Low"
        
    anxiety_scores.append(anx)
    depression_scores.append(dep)
    stress_levels.append(stress)

# 13. Work-Life Balance Score: 1 to 10
work_life_scores = []
for stress, st, sq in zip(stress_levels, screen_time, sleep_qualities):
    base_wlb = 8.5
    if stress == "High": base_wlb -= 3.8
    elif stress == "Medium": base_wlb -= 1.8
    
    if st > 8.0: base_wlb -= 1.2
    if sq == "Poor": base_wlb -= 1.4
    elif sq == "Good": base_wlb += 1.0
    
    wlb = int(np.clip(np.random.normal(loc=base_wlb, scale=1.0), 1, 10))
    work_life_scores.append(wlb)

# 14. Therapy Type: CBT, Meditation, Counseling, None (or Support Group)
therapy_types = []
durations = []
progress_scores = []
medication_flags = []

for stress, hist, dep, anx in zip(stress_levels, history_flags, depression_scores, anxiety_scores):
    # Probability of seeking intervention is higher for higher stress/history
    needs_care = (stress == "High") or (hist == "Yes" and (dep > 50 or anx > 50))
    
    if needs_care and np.random.rand() < 0.68:
        # Engaged in care
        t_type = np.random.choice(["CBT", "Counseling", "Meditation", "Support Group"], p=[0.42, 0.32, 0.16, 0.10])
        duration = int(np.random.choice([4, 6, 8, 10, 12, 16], p=[0.15, 0.25, 0.30, 0.15, 0.10, 0.05]))
        # Progress score (1-100 improvement points)
        prog = int(np.clip(np.random.normal(loc=25.0 + duration * 2.2, scale=8.5), 10, 85))
        # Medication usage: more common in High stress with history
        med = "Yes" if (stress == "High" and np.random.rand() < 0.52) else "No"
    elif stress == "Medium" and np.random.rand() < 0.35:
        t_type = np.random.choice(["Counseling", "Meditation", "Support Group"], p=[0.40, 0.40, 0.20])
        duration = int(np.random.choice([2, 4, 6, 8], p=[0.25, 0.40, 0.25, 0.10]))
        prog = int(np.clip(np.random.normal(loc=18.0 + duration * 1.8, scale=6.0), 8, 60))
        med = "Yes" if np.random.rand() < 0.15 else "No"
    else:
        t_type = "No Therapy"
        duration = 0
        prog = 0
        med = "No"
        
    therapy_types.append(t_type)
    durations.append(duration)
    progress_scores.append(prog)
    medication_flags.append(med)

# Construct DataFrame with EXACT 18 columns specified
df = pd.DataFrame({
    "User ID": user_ids,
    "Age": ages,
    "Gender": genders,
    "Occupation": occupations,
    "Stress Level": stress_levels,
    "Anxiety Score": anxiety_scores,
    "Depression Score": depression_scores,
    "Sleep Quality": sleep_qualities,
    "Daily Screen Time (hrs)": screen_time,
    "Physical Activity Level": activities,
    "Social Interaction Score": social_scores,
    "Mental Health History": history_flags,
    "Therapy Type": therapy_types,
    "Intervention Duration (weeks)": durations,
    "Progress Score": progress_scores,
    "Medication Usage": medication_flags,
    "Support System Strength": support_systems,
    "Work-Life Balance Score": work_life_scores
})

# Save to target location
output_path = "data/raw/mental_health_student_ecosystem.csv"
df.to_csv(output_path, index=False)
print(f"Successfully generated and saved {len(df)} records to {output_path}")
