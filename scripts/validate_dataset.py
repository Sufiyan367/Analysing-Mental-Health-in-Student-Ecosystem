import pandas as pd
import json

file_path = "data/raw/mental_health_student_ecosystem.csv"
df = pd.read_csv(file_path)

print("=" * 60)
print("PROGRAMMATIC DATASET VALIDATION REPORT")
print("=" * 60)

# 1. Row count & 2. Column count
rows, cols = df.shape
print(f"1. Row Count: {rows}")
print(f"2. Column Count: {cols}")

# 3. Missing values
missing = df.isnull().sum()
total_missing = missing.sum()
print(f"3. Total Missing Values: {total_missing}")
if total_missing > 0:
    print(missing[missing > 0])

# 4. Duplicate User IDs
dup_ids = df["User ID"].duplicated().sum()
print(f"4. Duplicate User IDs: {dup_ids}")

# 5. Data Types
print("\n5. Column Data Types:")
for col, dtype in df.dtypes.items():
    print(f"   - {col:32}: {dtype}")

# 6. Numerical Ranges
print("\n6. Numerical Ranges:")
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
for col in num_cols:
    min_v = df[col].min()
    max_v = df[col].max()
    mean_v = df[col].mean()
    print(f"   - {col:32}: Min = {min_v:6.1f}, Max = {max_v:6.1f}, Mean = {mean_v:6.1f}")

# 7. Category Values
print("\n7. Categorical Column Unique Values:")
cat_cols = df.select_dtypes(include=["object"]).columns
for col in cat_cols:
    if col != "User ID":
        vals = df[col].unique().tolist()
        print(f"   - {col:32}: {vals}")

# 8. Validation Result
is_valid = (
    rows >= 100
    and cols == 18
    and total_missing == 0
    and dup_ids == 0
    and "User ID" in df.columns
)

print("\n" + "=" * 60)
print(f"8. OVERALL VALIDATION STATUS: {'PASSED (100% VALID)' if is_valid else 'FAILED'}")
print("=" * 60)
