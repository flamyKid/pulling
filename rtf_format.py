import re
from striprtf.striprtf import rtf_to_text


def get_text(path, coding='utf-8'):
    # возвращаемый список с текстом
    text_list = list()

    transitional_list = list()
    styles_list = list()

    with open(path, encoding=coding) as file:
        for strings in file:
            string = rtf_to_text(strings)
            try:
                lines = string.split('.')
                if lines[0][0] == lines[0][0].lower():  # добавление старых и соединение новых
                    transitional_list[-1] += lines[0]
                    for elem in lines[1:]:
                        if elem:
                            transitional_list.append(elem)
                elif lines[0][0] != lines[0][0].lower():  # соединение новых предложений
                    for line in lines:
                        transitional_list.append(line)
                else:  # соединение одной буквы
                    transitional_list[-1] += lines[0]
            except:
                del lines

        # отделение стилей от текста
        all_text = ''

        for line in transitional_list:
            match = re.search(';', line)
            if match:
                styles_list.append(line)
                del line
            else:
                line += '.'
                all_text += line

        raw_text_list = all_text.split('. ')  # деление текста на предложения
        for string in raw_text_list:
            lines = string.split('\n.')  # разбиение первых и последних предложений в абзацах
            for line in lines:
                text_list.append(line)

    return text_list, styles_list


def find_text(path, pattern_list, coding='utf-8'):
    # возвращаемый словарь с совпадениями
    match_dict = dict()

    # получение текста из файла
    text_list, styles_list = get_text(path, coding)

    for string in text_list:
        for pattern in pattern_list:
            match = re.search(pattern.lower(), string.lower())
            if match:
                match_dict[string] = pattern

    return match_dict


def write_text(path, line_list, mode='w', coding='utf-8'):

    with open(path, mode, encoding=coding) as file:
        for elem in line_list:
            file.write(elem)

        print('Writing complete')

        file.close()


def replace_text(path, new_path, replacement_dict, coding='utf-8', new_coding='utf-8'):
    text_list, styles_list = get_text(path, coding)

    for string in text_list:
        line = string.rsplit()
        for word in line:
            for old_value, new_value in replacement_dict.items():
                if word == old_value:
                    index = line.index(word)
                    line[index] = new_value

        # соединение слов между собой
        all_text = ''
        for elem in line:
            elem += ' '
            all_text += elem

        edit_line = all_text.strip()  # удаление пробелов в начале и конце предложения
        edit_line += '. '  # добавление точки в конец предложения

        index = text_list.index(string)
        text_list[index] = edit_line  # изменение строки на редактированную строку

    write_text(new_path, text_list, 'w', new_coding)
