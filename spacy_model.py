import spacy

# Загрузка модели SpaCy для русского языка
nlp = spacy.load("ru_core_news_sm")


def extract_subject_verb(text):
    # Обработка текста с помощью SpaCy
    doc = nlp(text)

    facts = []

    # Извлечение подлежащего (существительного) и сказуемого (глагола) из каждого предложения в тексте
    for sent in doc.sents:
        subject = ""
        verb = ""
        for token in sent:
            if token.dep_ == "nsubj" and token.pos_ == "NOUN":   # nsubj - указывает на подлежащее
                subject = token.text
            elif token.dep_ == "ROOT" and token.pos_ == "VERB":   # ROOT - указывает на корень
                verb = token.lemma_
        if subject and verb:
            facts.append((subject, verb))

    return facts

def extracting_facts (text):

    # Извлечение фактов из текста
    facts = extract_subject_verb(text)

    # Вывод извлеченных фактов
    if facts:
        # print("Извлеченные факты:")
        return facts
    else:
       return ("Факты не найдены.")

