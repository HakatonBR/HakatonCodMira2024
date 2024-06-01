import os
from pdf2docx import Converter
from docx import Document
import string
import re
import spacy
import docx2txt
import win32com.client

nlp = spacy.load("ru_core_news_sm")


def validate_email(email):
    if re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
        return email


def validate_phone_number(phone_number):
    match = re.search(re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}"), phone_number)
    if match:
        return phone_number


def doc_to_txt(doc_file, txt_file):
    # import docx2txt
    try:
        text = docx2txt.process(doc_file)
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Успешно сконвертировано: {doc_file} -> {txt_file}")
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")


def rtf_to_txt(rtf_file, txt_file):
    # import win32com.client
    # pip install pywin32
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


def checkLeftLastName(lastword, lastnames):
    for lastName in lastnames.split():
        if lastword == lastName:
            return lastName


def findCompetitionSystemAnalytic(resume, competitions):
    listOfNeedsCompetition = []
    for word in resume:
        for competition in competitions:
            if competition == word:
                listOfNeedsCompetition.append(word)
    return listOfNeedsCompetition


def extract_info(text):
    entities = {
        'NAME': '',
        'EDUCATION': '',
        'SKILLS': '',
        'EXPERIENCE': ''
    }

    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PER" and not entities['NAME']:
            entities['NAME'] = ent.text
        elif ent.label_ in ["ORG", "GPE"] and any(
                keyword in ent.text.lower() for keyword in ["университет", "институт", "образование"]):
            entities['EDUCATION'] += ent.text + "\n"

    skill_keywords = ["навыки", "умения", "ключевые навыки"]
    experience_keywords = ["опыт работы", "работал", "работала", "работы", "должность"]
    education_keywords = ["университет", "институт", "образование"]

    lines = text.split('\n')
    current_section = None
    for line in lines:
        line = line.strip()
        if any(keyword in line.lower() for keyword in skill_keywords):
            current_section = 'SKILLS'
            continue
        elif any(keyword in line.lower() for keyword in experience_keywords):
            current_section = 'EXPERIENCE'
            continue
        elif any(keyword in line.lower() for keyword in education_keywords):
            current_section = 'EDUCATION'
            continue

        if current_section == 'SKILLS':
            entities['SKILLS'] += line + "\n"
        elif current_section == 'EXPERIENCE':
            entities['EXPERIENCE'] += line + "\n"
        elif current_section == 'EDUCATION':
            entities['EDUCATION'] += line + "\n"

    return entities


def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def parse_resume(text, names, lastNames, competitions):
    data = (re.compile('[%s]' % re.escape(string.punctuation))
            .sub('', text.replace('\n', ' ')).split())

    first_name = ''
    last_name = ''
    surname = ''
    age = None
    education = set()
    skills = set()
    experience = set()
    languages = set()
    email = ''
    phone = ''
    sex = 'NO_SELECTED'
    army_status = 'NO_SELECTED'
    comments = ''

    lastWord = 'Test'
    for word in data:
        for name in names.split():
            if word == name:
                result = checkLeftLastName(lastWord, lastNames)
                if result is not None:
                    last_name, first_name, surname = result, name, data[data.index(word) + 1]
                else:
                    index = data.index(word) + 1
                    last_name, first_name, surname = data[index], name, data[index + 1]
        lastWord = word

    entities = extract_info(text)

    education.update(entities['EDUCATION'].strip().split('\n'))
    skills.update(entities['SKILLS'].strip().split('\n'))
    experience.update(entities['EXPERIENCE'].strip().split('\n'))

    language_keywords = ["Английский", "Русский", "Французский", "Немецкий"]
    for keyword in language_keywords:
        if keyword in text:
            languages.add(keyword)

    age_match = re.search(r'\bВозраст[:\s](\d{1,2})\b', text)
    if age_match:
        age = int(age_match.group(1))

    email = validate_email(text)
    phone = validate_phone_number(text)

    candidate_data = {
        "first_name": first_name,
        "last_name": last_name,
        "surname": surname,
        "age": age,
        "education": education,
        "skills": skills,
        "experience": experience,
        "languages": languages,
        "email": email,
        "phone": phone,
        "sex": sex,
        "army_status": army_status,
        "comments": comments
    }

    return candidate_data


def format_candidate_data(candidate_data):
    formatted_data = []
    for key, value in candidate_data.items():
        if isinstance(value, set):
            formatted_data.append(f"{key.capitalize()}: {'; '.join(value)}")
        else:
            formatted_data.append(f"{key.capitalize()}: {value}")
    return '\n'.join(formatted_data)


if __name__ == "__main__":
    resume_path = 'C:/Z/CV/'

    file_names = [
        "031ff12d4bcf3dde16eec0cdf4850b11.docx",
        "0a4f89e0ece12af482aaaa8fefc0b2de.docx",
        "0a7d3618b1f556993778b027e4c1e812.docx",
        "111c2540180386389df6cf674ce328aa.docx",
        "155a73b3884413a12acde78c056cc6d5.docx",
        "17cfbd85a6106201d0f94ac6f5fde1b3.docx",
        "1a8f99835e5d0f3c68c28e4a556519b6.docx",
        "1f70554e4f5ddedf1ba813665e4461af.docx",
        "2518b8ebdb9075cc0d620904dd811a3f.docx",
        "282740691613d50fd824d7a291e57436.docx",
        "28294d007cf690ea8f6e486e2d2f9e0e.rtf",
        "2d8739b005dc52b5dfcc043fd59ca770.doc",
        "2f0f8126b1a77f7897e838c7de724020.rtf",
        "328c1704dd2822602ebad98115e00df5.docx",
        "3dc5f4cf947d63197c1cf917189e7ef0.docx",
        "4435fbe2f18bc2de212a29c5c175d282.rtf",
        "5e6c0a291ba6a12a833ae806bb743462.docx",
        "617adcc734b845a31922b5949faafa71.docx",
        "62fe24a7c8d06d89da049ba4c97cb08f.docx",
        "6633b376178241107f8bcfb299a961ce.docx",
        "66f285191cca0d7e150c0eca2cbb6cbe.rtf",
        "681d2f7f67078a5013a59a8ca468cccb.docx",
        "6a76ca3fec776cfc525e18c24c1da837.doc",
        "6cc7c3e6f69efc4d7811a1ac58a24663.docx",
        "6f8ea5d1492babf4d05e8de90d1bbf08.doc",
        "7503fa0a8806c063251929528c4f11cc.docx",
        "7b0905696fa3321ad19b102a2a5ff0c1.rtf",
        "7d6f9c4bba76456fc28eae634fd135b1.doc",
        "7dd248d2c26049cd2849b923fc3ccb65.docx",
        "84da38e09786ff6448e0918edddaaf37.docx",
        "86b8f15854d5fc4f4d6580e8b4e93ba7.docx",
        "8ba9fa1a6da0f07433f2f91bf51f9ee4.docx",
        "8ef22661825bd5808daa6f909c4c2faa.docx",
        "9263aede2b21218d29e55526232fbaaa.docx",
        "93f7371359ed553ebb429562f7b68457.docx",
        "984282a690d36465d56b5db8ce4241dc.docx",
        "98567dc9b886b9fe20f90786a4545b55.rtf",
        "9a21477c80affaf67cc485704fdc8c00.docx",
        "a110c9094807379b9433cf41ff9924b2.docx",
        "a19fb3c66e28a1e6898851bcd59e1baa.pdf",
        "a518b8ebdb9075cc0d620904dd811a3f.pdf",
        "a55a73b3884413a12acde78c056cc6d5.pdf",
        "a6b8cc0b687923ee3147ba8023af480c.docx",
        "b19595a3b9a70836ad0af4584eb62a7d.rtf",
        "b3e7814c168f4c69212fa2f6a11e3e01.rtf",
        "b4691b03dc6dd1d6c0523d0b3dfb0da1.docx",
        "b8b81205272ed7e97751f9624db8c21f.docx",
        "bb3269be9acfc588e26a182a5bf6e966.odt",
        "bf800bc830b3621248cf951d76f62e3d.docx",
        "c4398da183a1dde986e16ea7e1f58978.docx",
        "c63a7786eb8ac56498a4878e0f28eb97.rtf",
        "c6c245d7bea2d3d9b5c234fecbb0765a.docx",
        "cd7c66c745c699db275eeeb5ea0cbf5a.docx",
        "d87ba4eedb679e8544adff29db65f65d.docx",
        "de84902668c9de625c62e30df0f31528.docx",
        "e1786ce1b5b2a81d3e00c4658ea4e8fb.rtf",
        "e19fb3c66e28a1e6898851bcd59e1baa.docx",
        "f7e2f12f0e6ed50f48879048eecdc93e.docx",
        "f96d85ac4e4ca05a98e7ffbe9fb8e0a0.docx"
    ]

    path_Names = 'Names.txt'
    path_LastNames = 'LastNames.txt'
    path_SurNames = 'SurNames.txt'
    path_competitions = "Competentions.txt"

    with open(path_Names, 'r', encoding='utf-8') as file:
        names = file.read()
    with open(path_LastNames, 'r', encoding='utf-8') as file:
        lastNames = file.read()
    with open(path_SurNames, 'r', encoding='utf-8') as file:
        surNames = file.read()
    with open(path_competitions, 'r', encoding='utf-8') as file:
        competitions = file.read()

    for file_name in file_names:
        file_path = os.path.join(resume_path, file_name)

        if file_path.endswith('.docx'):
            docx_to_txt(file_path, "temp.txt")
        elif file_path.endswith('.pdf'):
            pdf_to_docx(file_path, "temp.docx")
            docx_to_txt("temp.docx", "temp.txt")
        elif file_path.endswith('.rtf'):
            rtf_to_txt(file_path, "temp.txt")
        elif file_path.endswith('.doc'):
            doc_to_txt(file_path, "temp.txt")
        else:
            continue

        text = read_text_from_file("temp.txt")

        candidate_data = parse_resume(text, names, lastNames, competitions)
        formatted_candidate_data = format_candidate_data(candidate_data)
        print("\nStructured Candidate Data for file:", file_path)
        print(formatted_candidate_data)
