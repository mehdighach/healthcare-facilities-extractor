# Healthcare Facilities Extractor

This project automates the extraction, cleaning, and analysis of healthcare facility data and metadata (PDFs and CSVs).

---

## Project Structure

healthcare-facilities-extractor/
│
├── explore_data.py → Explore dataset (row count, columns, samples)
├── clean_data.py → Clean duplicates, missing data, and export new CSV
├── pdf_link_extractor.py → Extract clickable links from PDF files
├── sample_pdfs/ → Folder for test PDFs
├── venv/ → Virtual environment
└── README.md


---

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/mehdighach/healthcare-facilities-extractor.git
   cd healthcare-facilities-extractor

2. Create a virtual environment:

python -m venv venv
.\venv\Scripts\activate


3. Install dependencies:

pip install pandas PyMuPDF

sage
1. Explore the dataset

Run this script to verify the file and preview the first rows:

python explore_data.py

2. Clean the dataset

This script removes duplicates, handles missing values, and exports a new clean file.

python clean_data.py


Output: odhf_cleaned.csv

3. Extract links from PDF documents

Place PDFs inside the sample_pdfs folder and run:

python pdf_link_extractor.py


Output: Extracted_PDF_Links.csv containing all detected hyperlinks and page numbers.

Example Outputs

Cleaned Data Example

File cleaned successfully.
Cleaned file saved to: odhf_cleaned.csv
Total rows after cleaning: 7033


Extracted Links Example

Scanning folder: sample_pdfs
Reading: ODHF_metadata_v1.1.pdf
Extraction complete.
Links saved to: Extracted_PDF_Links.csv

Next Steps

Add regex-based URL detection for non-clickable text links.

Integrate chunking and embedding using:

Chonkie for semantic chunking.

OpenAI text-embedding-3-large for vectorization.

FAISS or Qdrant for vector database storage.

Cohere Rerank 3.5 for improved retrieval quality.

Connect the extraction pipeline to a RAG environment for interactive document search.

Author

Mehdi El Ghachtoul

License

This project uses public datasets from Open Canada Data
 and is released for educational and research purposes.