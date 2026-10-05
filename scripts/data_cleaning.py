#!/usr/bin/env python3
"""
scripts/data_cleaning.py
------------------------
Reproducible Data Cleaning and Feature Engineering Pipeline
for 'Analysing Mental Health in Student Ecosystem'.

Outputs:
  data/cleaned/student_mental_health_cleaned.csv
"""

import os
import sys
import pandas as pd
import numpy as np

def clean_data(raw_path: str, cleaned_path: str):
    print("=" * 60)
    print("STARTING DATA PREPROCESSING PIPELINE")
    print("=" * 60)

    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw data file not found at: {raw_path}")

    df = pd.read_csv(raw_path)
    initial_rows, initial_cols = df.shape
    print(f"Loaded raw dataset with {initial_rows} rows and {initial_cols} columns.")

    # 1. Rename columns to clean, consistent identifiers
    column_mapping = {
        'Timestamp': 'Timestamp',
        'Choose your gender': 'Gender',
        'Age': 'Age',
        'What is your course?': 'Course',
        'Your current year of Study': 'Year_of_Study',
        'What is your CGPA?': 'CGPA_Range',
        'Marital status': 'Marital_Status',
        'Do you have Depression?': 'Depression',
        'Do you have Anxiety?': 'Anxiety',
        'Do you have Panic attack?': 'Panic_Attacks',
        'Did you seek any specialist for a treatment?': 'Sought_Treatment'
    }
    df = df.rename(columns=column_mapping)

    # 2. Trim string whitespace across all object columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()

    # 3. Handle Missing Values
    # Impute missing Age with median age
    median_age = df['Age'].median()
    df['Age'] = df['Age'].fillna(median_age).astype(int)
    print(f"Imputed missing Age with median value: {int(median_age)}")

    # 4. Standardize Gender (Title Case)
    df['Gender'] = df['Gender'].str.capitalize()

    # 5. Standardize Year of Study (e.g. 'year 1' -> 'Year 1')
    year_map = {
        'year 1': 'Year 1', 'Year 1': 'Year 1',
        'year 2': 'Year 2', 'Year 2': 'Year 2',
        'year 3': 'Year 3', 'Year 3': 'Year 3',
        'year 4': 'Year 4', 'Year 4': 'Year 4'
    }
    df['Year_of_Study'] = df['Year_of_Study'].map(year_map).fillna(df['Year_of_Study'])

    # 6. Standardize CGPA_Range (strip whitespace and unify syntax)
    cgpa_map = {
        '0 - 1.99': '0.00 - 1.99',
        '2.00 - 2.49': '2.00 - 2.49',
        '2.50 - 2.99': '2.50 - 2.99',
        '3.00 - 3.49': '3.00 - 3.49',
        '3.50 - 4.00': '3.50 - 4.00'
    }
    df['CGPA_Range'] = df['CGPA_Range'].map(cgpa_map).fillna(df['CGPA_Range'])

    # Add numeric midpoint for quantitative correlations
    midpoint_map = {
        '0.00 - 1.99': 1.00,
        '2.00 - 2.49': 2.25,
        '2.50 - 2.99': 2.75,
        '3.00 - 3.49': 3.25,
        '3.50 - 4.00': 3.75
    }
    df['CGPA_Midpoint'] = df['CGPA_Range'].map(midpoint_map)

    # 7. Standardize Course Names & Derive Faculty Grouping
    def categorize_faculty(course_str):
        c = course_str.lower()
        if any(k in c for k in ['eng', 'engin', 'engine', 'koe', 'mechanical']):
            return 'Engineering'
        elif any(k in c for k in ['bit', 'bcs', 'it', 'computer', 'information technology']):
            return 'IT & Computer Science'
        elif any(k in c for k in ['law', 'laws']):
            return 'Law'
        elif any(k in c for k in ['kenms', 'econ', 'business', 'accounting', 'banking', 'management']):
            return 'Business & Economics'
        elif any(k in c for k in ['islamic', 'irkhs', 'usuluddin', 'human sciences', 'communication', 'history', 'psychology']):
            return 'Humanities & Social Sciences'
        elif any(k in c for k in ['biomedical', 'nursing', 'pharmacy', 'mathe', 'science', 'biotechnology', 'radiography']):
            return 'Health & Natural Sciences'
        else:
            return 'Other Disciplines'

    df['Course'] = df['Course'].str.title()
    df['Faculty'] = df['Course'].apply(categorize_faculty)

    # 8. Standardize Binary Responses (Yes/No)
    binary_cols = ['Marital_Status', 'Depression', 'Anxiety', 'Panic_Attacks', 'Sought_Treatment']
    for col in binary_cols:
        df[col] = df[col].str.capitalize()
        # validate only Yes / No values
        valid = df[col].isin(['Yes', 'No']).all()
        if not valid:
            print(f"Warning: Unexpected value found in binary column {col}")

    # 9. Feature Engineering: Condition Count & Risk Category
    df['Depression_Binary'] = (df['Depression'] == 'Yes').astype(int)
    df['Anxiety_Binary'] = (df['Anxiety'] == 'Yes').astype(int)
    df['Panic_Binary'] = (df['Panic_Attacks'] == 'Yes').astype(int)
    df['Treatment_Binary'] = (df['Sought_Treatment'] == 'Yes').astype(int)

    df['Condition_Count'] = df['Depression_Binary'] + df['Anxiety_Binary'] + df['Panic_Binary']

    def assign_risk(count):
        if count >= 2:
            return 'High Risk'
        elif count == 1:
            return 'Moderate Risk'
        else:
            return 'Low Risk'

    df['Risk_Category'] = df['Condition_Count'].apply(assign_risk)

    def assign_treatment_gap(row):
        if row['Risk_Category'] == 'High Risk' and row['Sought_Treatment'] == 'No':
            return 'High Risk Treatment Gap'
        elif row['Sought_Treatment'] == 'Yes':
            return 'In Active Treatment'
        elif row['Risk_Category'] == 'Moderate Risk' and row['Sought_Treatment'] == 'No':
            return 'Moderate Risk Untreated'
        else:
            return 'No Serious Symptoms'

    df['Treatment_Status'] = df.apply(assign_treatment_gap, axis=1)

    # 10. Verification and Export
    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
    df.to_csv(cleaned_path, index=False)
    
    final_rows, final_cols = df.shape
    print("\n" + "=" * 60)
    print("DATA CLEANING COMPLETE")
    print("=" * 60)
    print(f"Final shape: {final_rows} rows, {final_cols} columns")
    print(f"Cleaned dataset saved to: {cleaned_path}")
    print("\nSummary Statistics:")
    print(f"- Total Students: {len(df)}")
    print(f"- Depression Rate: {(df['Depression_Binary'].mean()*100):.1f}%")
    print(f"- Anxiety Rate: {(df['Anxiety_Binary'].mean()*100):.1f}%")
    print(f"- Panic Attack Rate: {(df['Panic_Binary'].mean()*100):.1f}%")
    print(f"- Sought Treatment Rate: {(df['Treatment_Binary'].mean()*100):.1f}%")
    print(f"- High Risk Students: {(df['Risk_Category'] == 'High Risk').sum()} ({(df['Risk_Category'] == 'High Risk').mean()*100:.1f}%)")
    print(f"- High Risk Treatment Gap: {(df['Treatment_Status'] == 'High Risk Treatment Gap').sum()}")
    print("=" * 60)

if __name__ == '__main__':
    raw_csv = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'raw', 'student_mental_health_raw.csv')
    cleaned_csv = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'cleaned', 'student_mental_health_cleaned.csv')
    clean_data(raw_csv, cleaned_csv)
