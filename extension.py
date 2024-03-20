import PyPDF2               # Для работы с pdf-файлами
from docx import Document   # Для работы с docx-файлами


# Чтение txt-файла
def read_text_file(file_name):
    content = file_name.read().decode('utf-8')
    return content

# Чтение pdf-файла
def read_pdf(file_name):
    with open(file_name, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

# Чтение docx-файла
def read_docx(file_name):
    doc = Document(file_name)
    content = " ".join([paragraph.text for paragraph in doc.paragraphs])
    return content