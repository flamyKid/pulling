import re
from striprtf.striprtf import rtf_to_text


class RTF:

    def get_text(self, path, coding='utf-8'):
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
                except:
                    del lines

        return text_list

    def find_text(self, path, pattern_list, coding='utf-8'):
        # возвращаемый словарь с совпадениями
        match_dict = dict()

        # получение текста из файла
        text_list = self.get_text(path, coding)

        for string in text_list:
            for pattern in pattern_list:
                match = re.search(pattern.lower(), string.lower())
                if match:
                    match_dict[string] = pattern

        return match_dict

    def write_text(self, path, line_list, mode='w', coding='utf-8'):

        with open(path, mode, encoding=coding) as file:
            for elem in line_list:
                file.write(elem)

            print('Writing complete')

            file.close()

    def replace_text(self, path, new_path, replacement_dict, coding='utf-8', new_coding='utf-8'):
        text_list = self.get_text(path, coding)

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

        self.write_text(new_path, text_list, 'w', new_coding)


if __name__ == '__main__':
    text = ['Файл (англ', 'file) — именованная область данных на носителе информации. Работа с файлами реализуется средствами операционных систем',
            'Многие операционные системы приравнивают к файлам и обрабатывают сходным образом и другие ресурсы:\n',
            '\n', 'области данных (необязательно на диске);\n',
            'устройства — как физические, например, порты или принтеры, так и виртуальные;\n',
            'потоки данных (именованный канал);\n', 'сетевые ресурсы, сокеты;\n',
            'прочие объекты операционной системы.']

    path = 'test/test.rtf'
    rtf = RTF()

    rtf.write_text(path, text)

    found_text = rtf.find_text(path, ['file'])
    print(found_text)

    rtf.replace_text(path, path, {'Файл': 'File'})

    result_text = rtf.get_text(path)
    print(result_text)
