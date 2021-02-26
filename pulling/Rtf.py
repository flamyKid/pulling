import re
from striprtf.striprtf import rtf_to_text


def get_text(path, coding='utf-8'):
    # возвращаемый список с текстом
    text_list = list()

    with open(path, encoding=coding) as file:
        for strings in file:
            string = rtf_to_text(strings)
            try:
                lines = string.split('.')
                if lines[0][0] == lines[0][0].lower():  # добавление старых и соединение новых
                    text_list[-1] += lines[0]
                    for elem in lines[1:]:
                        if elem:
                            text_list.append(elem)
                elif lines[0][0] != lines[0][0].lower():  # соединение новых предложений
                    for line in lines:
                        text_list.append(line)
                else:  # соединение одной буквы
                    text_list[-1] += lines[0]
            except IndexError:
                del lines

    return text_list


def find_text(path, pattern_list, coding='utf-8'):
    # возвращаемый словарь с совпадениями
    match_dict = dict()

    # получение текста из файла
    text_list = get_text(path, coding)

    for string in text_list:
        for pattern in pattern_list:
            match = re.search(pattern.lower(), string.lower())
            if match:
                try:  # если совпадений на этот шаблон есть
                    match_dict[pattern].append(string)
                except KeyError:  # если совпадений на этот шаблон нет
                    match_dict[pattern] = [string]

    return match_dict


def write_text(path, line_list, mode='w', coding='utf-8'):

    with open(path, mode, encoding=coding) as file:
        for elem in line_list:
            file.write(elem)

        print('Writing complete.')

        file.close()


def replace_text(path, new_path, replacement_dict, coding='utf-8', new_coding='utf-8'):
    # получение текста из файла
    text_list = get_text(path, coding)

    for string in text_list:
        line = string.rsplit()  # разбиение строки по пробелам
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
        if edit_line[-1] != '.' and edit_line[-1] != '!' and edit_line[-1] != '?' and edit_line[-1] != ';':
            edit_line += '.'  # добавление точки в конец предложения

        index = text_list.index(string)
        text_list[index] = edit_line  # изменение строки на редактированную строку

    write_text(new_path, text_list, 'w', new_coding)
