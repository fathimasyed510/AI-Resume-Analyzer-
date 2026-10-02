from pypdf import PdfReader

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    return '\n'.join(page.extract_text() or '' for page in reader.pages)
