"""
Benchmark Filter Utilization and Subsetting Latency
Evaluates analytical filtering performance on the 200-row x 18-column
student mental health dataset across single and multi-dimensional predicates.
"""

import os
import time
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_filter_benchmark():
    csv_path = os.path.join('data', 'cleaned', 'mental_health_student_ecosystem_cleaned.csv')
    output_dir = os.path.join('evidence', 'performance', 'filters')
    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(csv_path)
    total_records = len(df)

    # Define filter scenarios based ONLY on actual fields
    scenarios = [
        {
            "id": "F1_gender_female",
            "name": "Gender = Female",
            "predicate": "Gender == 'Female'",
            "fields": ["Gender"],
            "filter_func": lambda d: d[d['Gender'] == 'Female']
        },
        {
            "id": "F2_stress_high",
            "name": "Stress Level = High",
            "predicate": "Stress Level == 'High'",
            "fields": ["Stress Level"],
            "filter_func": lambda d: d[d['Stress Level'] == 'High']
        },
        {
            "id": "F3_sleep_poor",
            "name": "Sleep Quality = Poor",
            "predicate": "Sleep Quality == 'Poor'",
            "fields": ["Sleep Quality"],
            "filter_func": lambda d: d[d['Sleep Quality'] == 'Poor']
        },
        {
            "id": "F4_female_high_stress",
            "name": "Gender = Female & Stress = High",
            "predicate": "(Gender == 'Female') & (Stress Level == 'High')",
            "fields": ["Gender", "Stress Level"],
            "filter_func": lambda d: d[(d['Gender'] == 'Female') & (d['Stress Level'] == 'High')]
        },
        {
            "id": "F5_triad_stress_sleep_cbt",
            "name": "Stress = High & Sleep = Poor & Therapy = CBT",
            "predicate": "(Stress Level == 'High') & (Sleep Quality == 'Poor') & (Therapy Type == 'CBT')",
            "fields": ["Stress Level", "Sleep Quality", "Therapy Type"],
            "filter_func": lambda d: d[(d['Stress Level'] == 'High') & (d['Sleep Quality'] == 'Poor') & (d['Therapy Type'] == 'CBT')]
        },
        {
            "id": "F6_activity_low",
            "name": "Physical Activity = Low",
            "predicate": "Physical Activity Level == 'Low'",
            "fields": ["Physical Activity Level"],
            "filter_func": lambda d: d[d['Physical Activity Level'] == 'Low']
        },
        {
            "id": "F7_history_high_stress",
            "name": "Mental History = Yes & Stress = High",
            "predicate": "(Mental Health History == 'Yes') & (Stress Level == 'High')",
            "fields": ["Mental Health History", "Stress Level"],
            "filter_func": lambda d: d[(d['Mental Health History'] == 'Yes') & (d['Stress Level'] == 'High')]
        },
        {
            "id": "F8_medication_yes",
            "name": "Medication Usage = Yes",
            "predicate": "Medication Usage == 'Yes'",
            "fields": ["Medication Usage"],
            "filter_func": lambda d: d[d['Medication Usage'] == 'Yes']
        }
    ]

    benchmark_results = []
    iterations = 1000

    for sc in scenarios:
        # Measure filtering latency
        latencies_us = []
        subset = sc['filter_func'](df)
        matched_count = len(subset)
        matched_pct = (matched_count / total_records) * 100.0

        for _ in range(iterations):
            t0 = time.perf_counter()
            _ = sc['filter_func'](df)
            t1 = time.perf_counter()
            latencies_us.append((t1 - t0) * 1_000_000.0) # in microseconds

        res_entry = {
            "id": sc['id'],
            "name": sc['name'],
            "predicate": sc['predicate'],
            "fields_evaluated": sc['fields'],
            "matched_records": matched_count,
            "total_records": total_records,
            "matched_percentage": round(matched_pct, 2),
            "subset_memory_bytes": int(subset.memory_usage(deep=True).sum()),
            "latency_microseconds": {
                "mean": round(float(np.mean(latencies_us)), 2),
                "std": round(float(np.std(latencies_us)), 2),
                "median": round(float(np.median(latencies_us)), 2),
                "min": round(float(np.min(latencies_us)), 2),
                "max": round(float(np.max(latencies_us)), 2),
                "p95": round(float(np.percentile(latencies_us, 95)), 2),
                "iterations": iterations
            },
            "latency_milliseconds": {
                "mean": round(float(np.mean(latencies_us)) / 1000.0, 4),
                "p95": round(float(np.percentile(latencies_us, 95)) / 1000.0, 4)
            }
        }
        benchmark_results.append(res_entry)

    final_payload = {
        "metadata": {
            "dataset_rows": total_records,
            "dataset_columns": len(df.columns),
            "benchmark_iterations_per_scenario": iterations,
            "benchmark_type": "Local Python Subsetting Simulation",
            "tableau_status": "Tableau Native Automation Unautomated (Interactive Web Controls Required)"
        },
        "scenarios": benchmark_results
    }

    json_path = os.path.join(output_dir, 'filter_benchmark_summary.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(final_payload, f, indent=2)
    print(f"Saved filter benchmark JSON to {json_path}")

    # Generate Chart Artifact
    fig, axes = plt.subplots(1, 2, figsize=(15, 6), facecolor='#f8f9fa')
    fig.suptitle('Task 2: Data Filter Utilization & Subsetting Performance Benchmark', fontsize=13, fontweight='bold', y=0.98)

    labels = [s['name'] for s in benchmark_results]
    counts = [s['matched_records'] for s in benchmark_results]
    pcts = [s['matched_percentage'] for s in benchmark_results]
    mean_lat = [s['latency_microseconds']['mean'] for s in benchmark_results]
    p95_lat = [s['latency_microseconds']['p95'] for s in benchmark_results]

    y_pos = np.arange(len(labels))

    # Plot 1: Yield Count & Proportion
    ax1 = axes[0]
    bars1 = ax1.barh(y_pos, counts, color='#2b5c8f', height=0.55, edgecolor='#333')
    for b, pct in zip(bars1, pcts):
        ax1.text(b.get_width() + 1.5, b.get_y() + b.get_height()/2., f"{int(b.get_width())} ({pct:.1f}%)", ha='left', va='center', fontsize=9, fontweight='bold')
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(labels, fontsize=9.5)
    ax1.set_xlabel('Filtered Record Count (out of 200)', fontsize=10)
    ax1.set_title('Filter Scenario Record Yield', fontsize=11, fontweight='bold')
    ax1.set_xlim(0, 120)
    ax1.grid(axis='x', linestyle='--', alpha=0.5)

    # Plot 2: Subsetting Latency (Mean vs P95 in Microseconds)
    ax2 = axes[1]
    h = 0.35
    b_mean = ax2.barh(y_pos - h/2, mean_lat, height=h, color='#41b6c4', label='Mean Latency', edgecolor='#333')
    b_p95 = ax2.barh(y_pos + h/2, p95_lat, height=h, color='#e34a33', label='P95 Latency', edgecolor='#333')
    for b in b_mean:
        ax2.text(b.get_width() + 5, b.get_y() + b.get_height()/2., f"{b.get_width():.0f}µs", ha='left', va='center', fontsize=8, fontweight='bold')
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([])
    ax2.set_xlabel('Latency in Microseconds (µs)', fontsize=10)
    ax2.set_title('Query Subsetting Execution Latency', fontsize=11, fontweight='bold')
    ax2.legend(loc='lower right', frameon=True, facecolor='#ffffff')
    ax2.set_xlim(0, max(p95_lat) * 1.25)
    ax2.grid(axis='x', linestyle='--', alpha=0.5)

    plt.tight_layout()
    chart_path = os.path.join(output_dir, 'filter_performance_benchmark.png')
    plt.savefig(chart_path, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"Saved evidence chart to {chart_path}")

if __name__ == '__main__':
    run_filter_benchmark()
