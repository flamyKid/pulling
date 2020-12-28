import re
import csv


def get_data(path):
    # возвращаемый список с данными
    data_list = list()

    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:  # строки
            column = row[0].rsplit(';')  # разбиение по столбикам
            if column[0] != row:
                data_list.append(column)
            else:
                column2 = row[0].rsplit('\t')
                data_list.append(column2)

    return data_list


def find_data(path, pattern_list):
    # возвращаемый список с совпадениями
    match_dict = dict()

    data_list = get_data(path)  # данные полученные из файла

    for row in data_list:  # строки
        for column in row:  # столбец
            for pattern in pattern_list:
                match = re.search(pattern.lower(), column.lower())
                if match:
                    try:  # если совпадений на этот шаблон есть
                        match_dict[pattern].append(row)
                    except KeyError:  # если совпадений на этот шаблон нет
                        match_dict[pattern] = [row]

    return match_dict


def write_data(path, data_list, mode='w'):

    with open(path, mode, newline='') as file:  # newline для открытия файла в excel без багов
        writer = csv.writer(file, delimiter=';')
        for elem in data_list:
            writer.writerow(elem)

        print('Writing complete.')

        file.close()


def replace_data(path, new_path, replacement_dict):
    data_list = get_data(path)  # данные полученные из файла

    for row in data_list:  # строки
        for column in row:  # столбец
            for old_value, new_value in replacement_dict.items():
                if column == old_value:
                    index = row.index(column)
                    row[index] = new_value

    write_data(new_path, data_list, 'w')
