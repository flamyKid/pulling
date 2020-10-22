import re
import requests
from bs4 import BeautifulSoup


def get_text(url):
    # возвращаемый список с текстом
    text_list = list()

    img_src_list = list()
    video_src_list = list()
    audio_src_list = list()
    href_dict = dict()  # словарь с ссылками

    tags_list = ['p', 'h', 'b', 'big', 'small', 'i', 'strong', 'sub', 'sup', 'ins', 'del', 'th']  # теги, содержащие текст

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ СОДЕРЖАЩИХ ТЕКСТ
    for elem in tags_list:
        for tag in soup.findAll(elem):
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
    for a in soup.findAll('a'):
        if tag.string:
            href_dict[a.string] = a.get('href')

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ <audio>
    for audio in soup.findAll('audio'):
        if audio:
            audio_tag = BeautifulSoup(str(audio), 'html.parser')  # что бы искал внутри тега
            if audio.get('src'):
                audio_src_list.append(audio.get('src'))
            for source in audio_tag.findAll('source'):  # для тега <source>
                if source and source.get('src'):
                    audio_src_list.append(source.get('src'))

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ <video>
    for video in soup.findAll('video'):
        if video:
            video_tag = BeautifulSoup(str(video), 'html.parser')  # что бы искал внутри тега
            if video.get('src'):
                video_src_list.append(video.get('src'))
            for source in video_tag.findAll('source'):   # для тега <source>
                if source and source.get('src'):
                    video_src_list.append(source.get('src'))

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ <img>
    for img in soup.find_all('img'):
        try:
            alt = img.attrs['alt']
            if alt == '':  # для таких тегов как alt=""
                img_src_list.append(img.get('src'))
        except KeyError:  # на случай, если alt не существует
            img_src_list.append(img.get('src'))
        else:  # если существует
            href_dict[alt] = img.get('src')

    href_dict['img'] = img_src_list
    href_dict['audio'] = audio_src_list
    href_dict['video'] = video_src_list

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ <span>
    for span in soup.find_all('span'):
        text_list.append(span.string)

    return text_list, href_dict


def find_text(url, pattern_list):
    # возвращаемый словарь с совпадениями
    match_dict = dict()

    text_list, href_dict = get_text(url)

    for elem in text_list:
        if elem:
            for pattern in pattern_list:
                match = re.search(pattern.lower(), elem.lower())
                if match:
                    match_dict[elem] = pattern

    for tag, href in href_dict.items():
        if tag:
            for pattern in pattern_list:
                match = re.search(pattern.lower(), tag.lower())
                if match:
                    match_dict[tag] = href

    return match_dict
