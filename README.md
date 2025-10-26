Healthcare Facilities Extractor

A Python-based data extraction and cleaning pipeline designed to explore healthcare facility datasets, clean them for analysis, and extract hyperlinks from PDF reports for downstream use in Retrieval-Augmented Generation (RAG) systems.

Setup
1. Clone this repository
git clone https://github.com/mehdighach/healthcare-facilities-extractor.git
cd healthcare-facilities-extractor

2. Create a virtual environment
python -m venv venv
.\venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

Usage
1. Explore the dataset

Run this script to verify the file and preview the first rows:

python explore_data.py


Output Example:

File found. Size: 1514321 bytes
Loaded successfully.
Total rows: 7033
Columns: ['index', 'facility_name', 'source_facility_type', ...]

2. Clean the dataset

This script removes duplicates, handles missing values, and exports a new clean file.

python clean_data.py


Output:

File cleaned successfully.
Cleaned file saved to: odhf_cleaned.csv
Total rows after cleaning: 7033

3. Extract links from PDF documents

Place your PDFs inside the sample_pdfs folder and run:

python pdf_link_extractor.py


# Output:

Scanning folder: sample_pdfs
Reading: ODHF_metadata_v1.1.pdf
Extraction complete.
Links saved to: Extracted_PDF_Links.csv

# Example Outputs
Cleaned Data Example
File cleaned successfully. Cleaned file saved to: odhf_cleaned.csv
Total rows after cleaning: 7033

# Extracted Links Example
Scanning folder: sample_pdfs
Reading: ODHF_metadata_v1.1.pdf
Extraction complete.
Links saved to: Extracted_PDF_Links.csv

# Next Steps

Add regex-based URL detection for non-clickable text links.

Integrate chunking and embedding using:

Chonkie for semantic chunking.

OpenAI text-embedding-3-large for vectorization.

FAISS or Qdrant for vector database storage.

Cohere Rerank 3.5 for improved retrieval quality.

Connect the extraction pipeline to a RAG environment for interactive document search.

# Author

Mehdi El Ghachtoul

# License

MIT License
