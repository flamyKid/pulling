import re
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile


def get_text(path):
    # возвращаемый список с текстом
    text_list = list()

    word_namespace = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    para = word_namespace + 'p'
    text = word_namespace + 't'

    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)

    raw_text_list = list()
    for paragraph in tree.iter(para):
        texts = [node.text for node in paragraph.iter(text) if node.text]
        if texts:
            raw_text_list.append(''.join(texts))

    all_text = '\n\n'.join(raw_text_list)  # весь текст в одной строке

    strings = all_text.split('. ')  # разбиение по предложениям
    for line in strings:
        lines = line.split('\n')  # разбиение по абзацам
        for string in lines:
            if string:
                text_list.append(string)

    return text_list


def find_text(path, pattern_list):
    # возвращаемый словарь с совпадениями
    match_dict = dict()

    # получение текста из файла
    text_list = get_text(path)

    for string in text_list:
        for pattern in pattern_list:
            match = re.search(pattern.lower(), string.lower())
            if match:
                try:  # если совпадений на этот шаблон есть
                    match_dict[pattern].append(string)
                except KeyError:  # если совпадений на этот шаблон нет
                    match_dict[pattern] = [string]

    return match_dict
