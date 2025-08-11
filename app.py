from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import base64
import io
from PIL import Image
import pdf2image
from pdf2image import convert_from_path

import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="AIzaSyCTIa_zcApRGgtaKHFK0FMbb97KJmudmxo")

# Set your Poppler path
POPPLER_PATH = r"C:\Users\venkataprasadbathula\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin"

# Gemini Vision Function
def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('models/gemini-2.5-pro')
    response = model.generate_content([input_text, pdf_content, prompt])
    return response.text

# PDF -> Image Conversion
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=POPPLER_PATH)
        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_part = {
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byte_arr).decode()
        }
        return pdf_part
    else:
        raise FileNotFoundError("No file uploaded")
import google.generativeai as genai




# --- Streamlit App UI ---
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Resume Analyzer with Gemini AI")

input_text = st.text_area("Paste Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully!")

# Define prompts
input_prompt1 = """You are a resume analysis expert. Extract technical skills, soft skills, education, and experience/project information from this resume. Only include explicitly stated info."""
input_prompt2 = """You are an ATS expert. Analyze the resume and the job description. Identify missing keywords from the job description in the resume and suggest ways to integrate them."""
input_prompt3 = """Compare the resume to the job description. Generate a score (0–100%) and show a breakdown of matching skills, missing skills, and how to improve alignment."""

# Buttons
submit1 = st.button("📄 Tell me about the Resume")
submit2 = st.button("🔧 How can I Improve the Resume?")
submit3 = st.button("📊 Percentage Match with JD")

# Handler
if submit1 or submit2 or submit3:
    if uploaded_file is None:
        st.error("Please upload a PDF resume first.")
    else:
        try:
            pdf_content = input_pdf_setup(uploaded_file)
            prompt = ""

            if submit1:
                prompt = input_prompt1
            elif submit2:
                prompt = input_prompt2
            elif submit3:
                prompt = input_prompt3

            with st.spinner("Analyzing with Gemini..."):
                response = get_gemini_response(input_text, pdf_content, prompt)
                st.subheader("Gemini's Response:")
                st.write(response)

        except Exception as e:
            st.error(f"Error: {str(e)}")
