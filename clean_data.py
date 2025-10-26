import pandas as pd
import os

file_path = r"C:\Users\elgha\OneDrive\Desktop\healthcare-facilities-extractor\odhf_v1.1.csv"

print("Checking file:", file_path)

if not os.path.exists(file_path):
    print("File not found.")
else:
    print("File found. Size:", os.path.getsize(file_path), "bytes")

    df = pd.read_csv(file_path, encoding="latin1", low_memory=False)
    print("Loaded successfully.")

    print("Total rows before cleaning:", len(df))
    df = df.drop_duplicates()
    df = df.dropna(subset=["facility_name"])
    df["city"] = df["city"].fillna("Unknown")
    df["province"] = df["province"].fillna("Unknown")

    print("Total rows after cleaning:", len(df))
    print("Missing values by column:")
    print(df.isnull().sum())

    output_path = os.path.join(os.getcwd(), "odhf_cleaned.csv")
    df.to_csv(output_path, index=False)
    print("\nFile cleaned successfully.")
    print("Cleaned file saved to:", output_path)