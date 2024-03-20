# Для работы с pdf-файлами
import PyPDF2

# Для работы с docx-файлами
from docx import Document

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
    document = Document(file_name)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text


# Пример использования для pdf-файла
pdf_file = "text_files/document.pdf"
pdf_text = read_pdf(pdf_file)
print(pdf_text)

# Пример использования для docx-файла
docx_file = "твой_файл.docx"
docx_text = read_docx(docx_file)
print(docx_text)


# Открываем файл на чтение
# with open('text.txt', 'r', encoding='utf-8') as file:
#     Читаем содержимое файла
#     content = file.read()

# Выводим содержимое файла в консоль
# print(content)