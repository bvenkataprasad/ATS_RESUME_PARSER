# ATS Resume Parser (PDF Only)

This is a Streamlit web app that extracts key information from PDF resumes and evaluates their compatibility with Applicant Tracking Systems (ATS).  
Upload your PDF resume to see extracted text and get insights on improving your job application success.

## Features

- Upload PDF resumes for analysis  
- Extracts text from all pages  
- Provides a clean, easy-to-read output  
- Helps identify ATS-friendly formatting  

## How to Use

1. Click **Browse files** to upload your PDF resume.  
2. Wait for the app to extract and display the text.  
3. Review the extracted content to check how well your resume will be parsed by ATS software.

## Technologies Used

- Python  
- Streamlit  
- pdfplumber (for PDF text extraction)  

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
