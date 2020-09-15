import re
import requests
from bs4 import BeautifulSoup


def get_text(url):
    # возвращаемый список с текстом
    text_list = list()

    href_dict = dict()  # словарь с ссылками и тегами <a> и <img>

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ <p>
    for tag in soup.findAll('p'):
        if tag.string:
            strings = tag.string
            lines = strings.split('. ')
            for line in lines:  # это предложение
                text_list.append(line)

    # ВЫТАСКИВАНИЕ ТЕКСТОВ ИЗ ТЕГОВ <h>
    for h in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        for tag in soup.findAll(h):
            text_list.append(tag.string)

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ <a>
    for tag in soup.findAll('a'):
        if tag.string:
            href_dict[tag.string] = tag.get('href')

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ <img>
    for img in soup.find_all('img'):
        try:
            alt = img.attrs['alt']
        except KeyError:
            continue
        else:
            href_dict[alt] = img.attrs['src']

    text_list.append(href_dict)

    for span in soup.find_all('span'):
        text_list.append(span.string)

    return text_list


def find_text(url, pattern_list):
    # возвращаемый словарь с совпадениями
    match_dict = dict()

    # получение текста из файла
    text_list = get_text(url)

    for elem in text_list:
        type_elem = isinstance(elem, str)
        if type_elem:
            for pattern in pattern_list:
                match = re.search(pattern.lower(), elem.lower())
                if match:
                    match_dict[elem] = pattern
        else:
            type_elem = isinstance(elem, dict)
            if type_elem:
                if elem:
                    for tag, href in elem.items():
                        for pattern in pattern_list:
                            match = re.search(pattern.lower(), tag.lower())
                            if match:
                                match_dict[tag] = href

    return match_dict
