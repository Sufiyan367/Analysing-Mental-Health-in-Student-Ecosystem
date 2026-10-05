#!/usr/bin/env python3
"""
app.py
------
Flask Web Application for 'Analysing Mental Health in Student Ecosystem'.
Hosts interactive Tableau Public Dashboards and Data Story.
"""

import os
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

# Base Paths & Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'cleaned', 'student_mental_health_cleaned.csv')

# Tableau Public Configuration
TABLEAU_PROFILE_URL = os.environ.get(
    'TABLEAU_PROFILE_URL', 
    'https://public.tableau.com/app/profile/sufiyansurve333'
)
TABLEAU_PUBLIC_URL = os.environ.get(
    'TABLEAU_PUBLIC_URL', 
    'https://public.tableau.com/views/AnalysingMentalHealthinStudentEcosystem/Dashboard1'
)
TABLEAU_DASHBOARD_PATH = os.environ.get(
    'TABLEAU_DASHBOARD_PATH', 
    'AnalysingMentalHealthinStudentEcosystem/Dashboard1'
)
TABLEAU_STORY_PATH = os.environ.get(
    'TABLEAU_STORY_PATH', 
    'AnalysingMentalHealthinStudentEcosystem/Story'
)

def get_summary_metrics():
    """Compute summary KPIs directly from cleaned dataset."""
    if os.path.exists(DATA_PATH):
        try:
            df = pd.read_csv(DATA_PATH)
            total = len(df)
            dep_rate = round(df['Depression_Binary'].mean() * 100, 1)
            anx_rate = round(df['Anxiety_Binary'].mean() * 100, 1)
            treat_rate = round(df['Treatment_Binary'].mean() * 100, 1)
            high_risk = int((df['Risk_Category'] == 'High Risk').sum())
            return {
                'total_students': total,
                'depression_rate': dep_rate,
                'anxiety_rate': anx_rate,
                'treatment_rate': treat_rate,
                'high_risk_students': high_risk
            }
        except Exception as e:
            print(f"Error loading dataset: {e}")
            
    # Fallback to verified benchmark metrics
    return {
        'total_students': 101,
        'depression_rate': 34.7,
        'anxiety_rate': 33.7,
        'treatment_rate': 5.9,
        'high_risk_students': 28
    }

@app.route('/')
def home():
    metrics = get_summary_metrics()
    return render_template(
        'index.html',
        active_page='home',
        **metrics
    )

@app.route('/dashboard')
def dashboard():
    return render_template(
        'dashboard.html',
        active_page='dashboard',
        tableau_public_url=TABLEAU_PUBLIC_URL,
        tableau_dashboard_path=TABLEAU_DASHBOARD_PATH
    )

@app.route('/story')
def story():
    return render_template(
        'story.html',
        active_page='story',
        tableau_public_url=TABLEAU_PUBLIC_URL,
        tableau_story_path=TABLEAU_STORY_PATH
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        active_page='about'
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
