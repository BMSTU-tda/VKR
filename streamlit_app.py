import streamlit as st
from extension import read_pdf, read_docx, read_text_file
from spacy_model import extracting_facts


def main():
    st.title("Программа для загрузки и вывода содержимого текстовых файлов")

    # Загрузка файла
    uploaded_file = st.file_uploader("Выберите файл", type=["txt", "pdf", "docx"])

    # Вывод содержимого файла в переменную content
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1]
        content = ""

        if file_extension == "txt":
            content = read_text_file(uploaded_file)
        elif file_extension == "pdf":
            content = read_pdf(uploaded_file)
        elif file_extension == "docx":
            content = read_docx(uploaded_file)

        st.header("Содержимое файла:")
        st.text(content)

        # Извлечение фактов (пусть пока фактом назовем связку подлежащее+сказуемое)
        facts = extracting_facts(content)

        st.header("Извлеченные факты:")
        for fact in facts:
            st.text(f"Подлежащее: {fact[0]}, Сказуемое: {fact[1]}")

if __name__ == "__main__":
    main()