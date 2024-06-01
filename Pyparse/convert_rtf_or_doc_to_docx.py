from pdf2docx import Converter
import docx2txt
import os
import win32com.client
from docx import Document


def doc_to_txt(doc_file, txt_file):
    #import docx2txt
    try:
        text = docx2txt.process(doc_file)
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Успешно сконвертировано: {doc_file} -> {txt_file}")
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")


def rtf_to_txt(rtf_file, txt_file):
    #import win32com.client
    #pip install pywin32
    try:
        word = win32com.client.Dispatch("Word.Application")
        doc = word.Documents.Open(rtf_file)
        doc.SaveAs(txt_file, FileFormat=2)

        doc.Close()
        word.Quit()

        print(f"Успешно сконвертировано: {rtf_file} -> {txt_file}")
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")


def pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()
    print(f"Converted {pdf_path} to {docx_path}")


def docx_to_txt(docx_path, txt_path):
    doc = Document(docx_path)
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        for para in doc.paragraphs:
            txt_file.write(para.text + '\n')
    print(f"Converted {docx_path} to {txt_path}")


def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":
    resume_path = 'C:/Z/CV/'

    file_names = [
        "28294d007cf690ea8f6e486e2d2f9e0e.rtf",
        # "2d8739b005dc52b5dfcc043fd59ca770.doc",
        "2f0f8126b1a77f7897e838c7de724020.rtf",
         "4435fbe2f18bc2de212a29c5c175d282.rtf",
         "66f285191cca0d7e150c0eca2cbb6cbe.rtf",
        # "6f8ea5d1492babf4d05e8de90d1bbf08.doc",
         "7b0905696fa3321ad19b102a2a5ff0c1.rtf",
        # "7d6f9c4bba76456fc28eae634fd135b1.doc",
         "98567dc9b886b9fe20f90786a4545b55.rtf",
         "b19595a3b9a70836ad0af4584eb62a7d.rtf",
         "b3e7814c168f4c69212fa2f6a11e3e01.rtf",
        # "bb3269be9acfc588e26a182a5bf6e966.odt",
         "c63a7786eb8ac56498a4878e0f28eb97.rtf",
         "e1786ce1b5b2a81d3e00c4658ea4e8fb.rtf"
    ]

    for file in file_names:
        rtf_to_txt(resume_path + file, resume_path + file + ".txt")
