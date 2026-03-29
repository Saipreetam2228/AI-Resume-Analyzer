import pdfplumber


def extract_text_from_pdf(file_path):
    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        print("Error reading PDF:", e)

    return text


# 🔹 Test block (runs only when this file is executed directly)
if __name__ == "__main__":
    file_path = "sample.pdf"  # Make sure this file exists in your folder

    extracted_text = extract_text_from_pdf(file_path)

    if extracted_text:
        print("✅ Extracted Text (first 500 characters):\n")
        print(extracted_text[:500])
    else:
        print("❌ No text extracted. Check the PDF file.")