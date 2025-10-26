import os
import pandas as pd
import sys

file_path = os.path.join(os.getcwd(), "odhf_v1.1.csv")

print("Checking file:", file_path)
sys.stdout.flush()

if not os.path.exists(file_path):
    print("File not found.")
    sys.stdout.flush()
    sys.exit(1)

print("File found. Size:", os.path.getsize(file_path), "bytes")
sys.stdout.flush()

try:
    df = pd.read_csv(file_path, encoding="utf-8", low_memory=False)
    print("Loaded successfully with utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding="latin1", low_memory=False)
    print("Loaded successfully with latin1")

print("Total rows:", len(df))
print("Columns:", df.columns.tolist())
print("First 5 rows:")
print(df.head())
sys.stdout.flush()
