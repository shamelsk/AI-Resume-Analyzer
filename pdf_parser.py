import fitz  # PyMuPDF


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF file.

    Args:
        uploaded_file: Streamlit uploaded PDF object.

    Returns:
        str: Extracted text from all pages.
    """

    document = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    document.close()

    return extracted_text.strip()