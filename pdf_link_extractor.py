import fitz  # PyMuPDF
import os
import pandas as pd

folder_path = r"C:\Users\elgha\OneDrive\Desktop\healthcare-facilities-extractor"
results = []

print("Scanning folder:", folder_path)

for file_name in os.listdir(folder_path):
    if file_name.endswith(".pdf"):
        file_path = os.path.join(folder_path, file_name)
        print("Reading:", file_name)

        doc = fitz.open(file_path)

        for page_num, page in enumerate(doc, start=1):
            links = page.get_links()
            for link in links:
                uri = link.get("uri", None)
                if uri:
                    results.append({
                        "file": file_name,
                        "page": page_num,
                        "url": uri
                    })

        doc.close()

print("Extraction complete.")

if results:
    df = pd.DataFrame(results)
    output_path = os.path.join(os.getcwd(), "Extracted_PDF_Links.csv")
    df.to_csv(output_path, index=False)
    print("Links saved to:", output_path)
else:
    print("No hyperlinks found.")