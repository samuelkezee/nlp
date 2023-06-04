import PyPDF2


def read_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        first_page = pdf_reader.pages[0]
        text = first_page.extract_text()
        print(text)


pdf_path = "C:\\Users\\User\\Desktop\\shortstory.pdf"
read_pdf(pdf_path)
