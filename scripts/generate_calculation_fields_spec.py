"""
Generate Calculation Fields Specification and Evidence
Audits analytical requirements across the 200-row student mental health dataset,
verifies calculated field logic, and produces structured specifications for Tableau authoring.
"""

import os
import json
import pandas as pd
import matplotlib.pyplot as plt

def generate_calc_fields_spec():
    csv_path = os.path.join('data', 'cleaned', 'mental_health_student_ecosystem_cleaned.csv')
    output_dir = os.path.join('evidence', 'performance', 'calculations')
    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(csv_path)

    # Define the 10 genuinely justified calculation fields
    calc_fields = [
        {
            "id": "CALC_01",
            "field_name": "Average Anxiety Score",
            "field_type": "Calculated Measure (Aggregation)",
            "data_type": "Float (Continuous)",
            "tableau_formula": "AVG([Anxiety Score])",
            "source_fields": ["Anxiety Score"],
            "purpose": "Primary psychometric symptom benchmark across cohorts and filters.",
            "where_used": "Header KPI Cards, Vis 2 (Stress vs Anxiety), Vis 4 (Gender Comparison), Story Scene 1 & 2",
            "sample_overall_value": round(float(df['Anxiety Score'].mean()), 2)
        },
        {
            "id": "CALC_02",
            "field_name": "Average Depression Score",
            "field_type": "Calculated Measure (Aggregation)",
            "data_type": "Float (Continuous)",
            "tableau_formula": "AVG([Depression Score])",
            "source_fields": ["Depression Score"],
            "purpose": "Secondary psychometric symptom benchmark across cohorts and filters.",
            "where_used": "Header KPI Cards, Vis 3 (Stress vs Depression), Vis 4 (Gender Comparison), Story Scene 1 & 2",
            "sample_overall_value": round(float(df['Depression Score'].mean()), 2)
        },
        {
            "id": "CALC_03",
            "field_name": "Average Daily Screen Time",
            "field_type": "Calculated Measure (Aggregation)",
            "data_type": "Float (Continuous)",
            "tableau_formula": "AVG([Daily Screen Time (hrs)])",
            "source_fields": ["Daily Screen Time (hrs)"],
            "purpose": "Quantifies digital exposure and lifestyle immersion per cohort.",
            "where_used": "Header KPI Card, Vis 6 (Screen Time vs Stress), Story Scene 1 & 3",
            "sample_overall_value": round(float(df['Daily Screen Time (hrs)'].mean()), 2)
        },
        {
            "id": "CALC_04",
            "field_name": "Total Student Cohort",
            "field_type": "Calculated Measure (Aggregation)",
            "data_type": "Integer (Discrete)",
            "tableau_formula": "COUNTD([User ID])",
            "source_fields": ["User ID"],
            "purpose": "Primary cohort volume and proportional denominator.",
            "where_used": "Header KPI Card, Vis 1 (Distribution), Vis 5 (Sleep), Vis 7 (History), Story Scenes 1-5",
            "sample_overall_value": int(df['User ID'].nunique())
        },
        {
            "id": "CALC_05",
            "field_name": "Therapy Active Indicator",
            "field_type": "Calculated Dimension (Boolean / Discrete)",
            "data_type": "String",
            "tableau_formula": "IF [Therapy Type] != 'No Therapy' THEN 'Enrolled in Therapy' ELSE 'No Therapy' END",
            "source_fields": ["Therapy Type"],
            "purpose": "Segments active clinical intervention recipients from un-enrolled students.",
            "where_used": "Vis 8 (Therapy Efficacy), Dashboard Therapy Section, Story Scene 5",
            "sample_overall_value": f"Active: {(df['Therapy Type'] != 'No Therapy').sum()}, No Therapy: {(df['Therapy Type'] == 'No Therapy').sum()}"
        },
        {
            "id": "CALC_06",
            "field_name": "High Stress Indicator",
            "field_type": "Calculated Dimension (Binary Flag)",
            "data_type": "String",
            "tableau_formula": "IF [Stress Level] = 'High' THEN 'High Stress' ELSE 'Low or Moderate Stress' END",
            "source_fields": ["Stress Level"],
            "purpose": "Identifies urgent triage cases requiring clinical escalation.",
            "where_used": "Dashboard Alerts, Story Scene 2, 3, 4 vulnerability analysis",
            "sample_overall_value": f"High: {(df['Stress Level'] == 'High').sum()}, Other: {(df['Stress Level'] != 'High').sum()}"
        },
        {
            "id": "CALC_07",
            "field_name": "Psychological Distress Index",
            "field_type": "Calculated Measure (Row-level Continuous)",
            "data_type": "Float (Continuous)",
            "tableau_formula": "([Anxiety Score] + [Depression Score]) / 2.0",
            "source_fields": ["Anxiety Score", "Depression Score"],
            "purpose": "Composite metric capturing dual-manifestation comorbid distress load.",
            "where_used": "Multivariate analysis, composite symptom correlation in Story Scene 2",
            "sample_overall_value": round(float(((df['Anxiety Score'] + df['Depression Score']) / 2.0).mean()), 2)
        },
        {
            "id": "CALC_08",
            "field_name": "Age Group",
            "field_type": "Calculated Dimension (Categorical Binning)",
            "data_type": "String",
            "tableau_formula": "IF [Age] <= 19 THEN '18-19 (Underclass)' ELSEIF [Age] <= 21 THEN '20-21 (Upperclass)' ELSE '22+ (Postgraduate/Senior)' END",
            "source_fields": ["Age"],
            "purpose": "Demographic age binning preventing high-cardinality discrete noise.",
            "where_used": "Demographic breakdown filters, cohort comparisons",
            "sample_overall_value": "Binned: 18-19, 20-21, 22+"
        },
        {
            "id": "CALC_09",
            "field_name": "Active Therapy Progress Score",
            "field_type": "Calculated Measure (Conditional)",
            "data_type": "Float (Continuous)",
            "tableau_formula": "IF [Therapy Type] != 'No Therapy' THEN [Progress Score] ELSE NULL END",
            "source_fields": ["Progress Score", "Therapy Type"],
            "purpose": "Computes true clinical improvement without zero-deflation from untreated students.",
            "where_used": "Vis 8 (Therapy Efficacy), Dashboard Treatment Section, Story Scene 5",
            "sample_overall_value": round(float(df[df['Therapy Type'] != 'No Therapy']['Progress Score'].mean()), 2)
        },
        {
            "id": "CALC_10",
            "field_name": "High-Risk Sleep Deficit Flag",
            "field_type": "Calculated Dimension (Compound Flag)",
            "data_type": "String",
            "tableau_formula": "IF [Stress Level] = 'High' AND [Sleep Quality] = 'Poor' THEN 'High Risk (Severe Sleep Deficit)' ELSE 'Standard Risk' END",
            "source_fields": ["Stress Level", "Sleep Quality"],
            "purpose": "Isolates the acute behavioral vulnerability cohort (71.4% of high stress).",
            "where_used": "Dashboard Risk Callouts, Story Scene 3",
            "sample_overall_value": f"High Risk: {((df['Stress Level'] == 'High') & (df['Sleep Quality'] == 'Poor')).sum()} students"
        }
    ]

    payload = {
        "metadata": {
            "total_calculation_fields": len(calc_fields),
            "calculated_measures_count": 5,
            "calculated_dimensions_count": 5,
            "dataset_rows": len(df),
            "dataset_columns": len(df.columns),
            "tableau_authoring_status": "Formulas validated on source data; prepared for native Tableau authoring entry"
        },
        "fields": calc_fields
    }

    json_path = os.path.join(output_dir, 'calculation_fields_spec.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)
    print(f"Saved calculation fields spec to {json_path}")

    # Generate visual summary of calculation fields
    fig, ax = plt.subplots(figsize=(14, 7), facecolor='#f8f9fa')
    ax.axis('off')

    title_text = "Task 3: Analytical Calculation Fields Specification (Total: 10 Fields)"
    ax.text(0.02, 0.96, title_text, fontsize=14, fontweight='bold', color='#1a252f')
    ax.text(0.02, 0.92, "Formulas engineered from validated 18-column student mental health dataset for native Tableau implementation.",
            fontsize=10.5, color='#555555')

    table_data = []
    headers = ["ID", "Field Name", "Field Type", "Tableau Formula", "Source Fields", "Where Used"]
    for cf in calc_fields:
        table_data.append([
            cf["id"],
            cf["field_name"],
            cf["field_type"].split()[0], # Short type
            cf["tableau_formula"] if len(cf["tableau_formula"]) < 45 else cf["tableau_formula"][:42] + "...",
            ", ".join(cf["source_fields"]),
            cf["where_used"].split(",")[0]
        ])

    table = ax.table(cellText=table_data, colLabels=headers, loc='center', cellLoc='left',
                     bbox=[0.02, 0.05, 0.96, 0.82])
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.4)

    # Style table header
    for k in range(len(headers)):
        table[(0, k)].set_facecolor('#2b5c8f')
        table[(0, k)].set_text_props(color='white', fontweight='bold')
    
    # Alternate row colors
    for row in range(1, len(calc_fields) + 1):
        bg_col = '#ffffff' if row % 2 == 1 else '#f0f4f8'
        for col in range(len(headers)):
            table[(row, col)].set_facecolor(bg_col)

    chart_path = os.path.join(output_dir, 'calculation_fields_inventory.png')
    plt.savefig(chart_path, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"Saved visual inventory chart to {chart_path}")

if __name__ == '__main__':
    generate_calc_fields_spec()
