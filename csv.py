import re
import csv


def get_data(path):
    # возвращаемый список с текстом
    text_list = list()

    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:  # строки
            column = row[0].rsplit(';')  # разбиение по столбикам
            if column[0] != row:
                text_list.append(column)
            else:
                column2 = row[0].rsplit('\t')
                text_list.append(column2)

    return text_list


def find_data(path, pattern_list):
    # возвращаемый словарь с совпадениями
    match_list = list()

    # получение текста из файла
    text_list = get_data(path)

    for row in text_list:  # строки
        for column in row:  # столбец
            for pattern in pattern_list:
                match = re.search(pattern.lower(), column.lower())
                if match:
                    match_list.append(row)

    return match_list


def write_data(path, data, mode='w'):

    with open(path, mode, newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for elem in data:
            writer.writerow(elem)

        print('Writing complete')

        file.close()


def replace_data(path, new_path, word_dict):
    text_list = get_data(path)

    for row in text_list:  # строки
        for column in row:  # столбец
            for old_value, new_value in word_dict.items():
                if column == old_value:
                    index = row.index(column)
                    row[index] = new_value

    write_data(new_path, text_list,'w')
