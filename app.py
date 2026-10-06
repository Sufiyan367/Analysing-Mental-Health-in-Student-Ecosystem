#!/usr/bin/env python3
"""
app.py
------
Flask Web Application for 'Analysing Mental Health in Student Ecosystem'.
Hosts interactive Tableau Public Dashboards, Guided 5-Scene Data Story,
and dataset diagnostic metrics.
"""

import os
import pandas as pd
from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

# Base Paths & Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'cleaned', 'mental_health_student_ecosystem_cleaned.csv')
EVIDENCE_DIR = os.path.join(BASE_DIR, 'evidence')

# Tableau Public Configuration
TABLEAU_PROFILE_URL = os.environ.get(
    'TABLEAU_PROFILE_URL', 
    'https://public.tableau.com/app/profile/sufiyansurve333'
)
# Configurable Tableau embed URLs (empty by default until workbook publication)
TABLEAU_DASHBOARD_URL = os.environ.get('TABLEAU_DASHBOARD_URL', '').strip()
TABLEAU_STORY_URL = os.environ.get('TABLEAU_STORY_URL', '').strip()

def get_summary_metrics():
    """Compute summary KPIs directly from validated 18-column dataset."""
    if os.path.exists(DATA_PATH):
        try:
            df = pd.read_csv(DATA_PATH)
            total = len(df)
            avg_anxiety = round(float(df['Anxiety Score'].mean()), 2)
            avg_depression = round(float(df['Depression Score'].mean()), 2)
            avg_screen_time = round(float(df['Daily Screen Time (hrs)'].mean()), 2)
            high_stress_count = int((df['Stress Level'] == 'High').sum())
            high_stress_pct = round((high_stress_count / total) * 100.0, 1)
            med_stress_count = int((df['Stress Level'] == 'Medium').sum())
            med_stress_pct = round((med_stress_count / total) * 100.0, 1)
            therapy_active_count = int((df['Therapy Type'] != 'No Therapy').sum())
            therapy_active_pct = round((therapy_active_count / total) * 100.0, 1)
            high_risk_sleep_count = int(((df['Stress Level'] == 'High') & (df['Sleep Quality'] == 'Poor')).sum())

            return {
                'total_students': total,
                'avg_anxiety': avg_anxiety,
                'avg_depression': avg_depression,
                'avg_screen_time': avg_screen_time,
                'high_stress_count': high_stress_count,
                'high_stress_pct': high_stress_pct,
                'med_stress_count': med_stress_count,
                'med_stress_pct': med_stress_pct,
                'therapy_active_count': therapy_active_count,
                'therapy_active_pct': therapy_active_pct,
                'high_risk_sleep_count': high_risk_sleep_count
            }
        except Exception as e:
            print(f"Error computing dataset metrics: {e}")

    # Verified fallback values from validation_summary.json
    return {
        'total_students': 200,
        'avg_anxiety': 52.59,
        'avg_depression': 48.09,
        'avg_screen_time': 7.10,
        'high_stress_count': 49,
        'high_stress_pct': 24.5,
        'med_stress_count': 107,
        'med_stress_pct': 53.5,
        'therapy_active_count': 93,
        'therapy_active_pct': 46.5,
        'high_risk_sleep_count': 35
    }

@app.route('/')
def home():
    metrics = get_summary_metrics()
    return render_template(
        'index.html',
        active_page='home',
        tableau_profile_url=TABLEAU_PROFILE_URL,
        tableau_dashboard_url=TABLEAU_DASHBOARD_URL,
        tableau_story_url=TABLEAU_STORY_URL,
        **metrics
    )

@app.route('/dashboard')
def dashboard():
    metrics = get_summary_metrics()
    return render_template(
        'dashboard.html',
        active_page='dashboard',
        tableau_profile_url=TABLEAU_PROFILE_URL,
        tableau_dashboard_url=TABLEAU_DASHBOARD_URL,
        **metrics
    )

@app.route('/story')
def story():
    metrics = get_summary_metrics()
    return render_template(
        'story.html',
        active_page='story',
        tableau_profile_url=TABLEAU_PROFILE_URL,
        tableau_story_url=TABLEAU_STORY_URL,
        **metrics
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        active_page='about',
        tableau_profile_url=TABLEAU_PROFILE_URL
    )

@app.route('/evidence/<path:filename>')
def serve_evidence(filename):
    """Serve evidence visualization and prototype files."""
    return send_from_directory(EVIDENCE_DIR, filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
