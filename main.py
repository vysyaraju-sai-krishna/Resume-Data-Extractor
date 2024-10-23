
# 1. Install Required Libraries:
# pip install PyPDF2 python-docx pyresparser pandas
# first we have to  install these modules
import PyPDF2
from docx import Document
import re

# 2. Extracting Text from Different File Types:
# extract_text_from_pdf function extracts text from pdf file
def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text


# extract_text_from_docx() extracts text from docx file
def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# 3. Using Regular Expressions to Extract Specific Information Like email,phone number,linkedin,github id
def extract_email(text):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)

def extract_phone_number(text):
    phone_pattern = r'\+?\d[\d -]{8,12}\d'
    return re.findall(phone_pattern, text)

def extract_linkedin(text):
    linkedin_pattern = r'https?://(www\.)?linkedin\.com/[a-zA-Z0-9_\-\/]+'
    return re.findall(linkedin_pattern, text)

def extract_github(text):
    github_pattern = r'https?://(www\.)?github\.com/[a-zA-Z0-9_\-]+'
    return re.findall(github_pattern, text)


# 4.extract content from a resume file and return the email, phone number, GitHub, and LinkedIn information:
def extract_content_from_resume(file_path):
    if file_path.endswith('.pdf'):
        resume_text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        resume_text = extract_text_from_docx(file_path)
    else:
        return "Unsupported file format"

    # Extract information using regular expressions
    email = extract_email(resume_text)
    phone = extract_phone_number(resume_text)
    linkedin = extract_linkedin(resume_text)
    github = extract_github(resume_text)

    return {
        "Email": email,
        "Phone": phone,
        "LinkedIn": linkedin,
        "GitHub": github
    }

# Example usage:
file_path = r'C:\Users\vamsi\Downloads\Prajna_Resume.pdf'  # Path to your resume
extracted_data = extract_content_from_resume(file_path)
print(extracted_data)

'''
{'Email': ['prajna.yogish4@gmail.com'], 'Phone': ['947-201-7881'], 'LinkedIn': [], 'GitHub': []}
output looks like this.
'''