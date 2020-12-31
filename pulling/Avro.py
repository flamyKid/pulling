import re
import fastavro


def get_data(path, schema):
    # возвращаемый список с данными
    data_list = list()

    with open(path, 'rb') as file:
        reader = fastavro.reader(file, schema)

        for elem in reader:
            data_list.append(elem)

    return data_list


def find_data(path, schema, pattern_list):
    # возвращаемый словарь с совпадениями
    match_dict = dict()

    data_list = get_data(path, schema)  # данные полученные из файла

    for value_dict in data_list:
        for pattern in pattern_list:
            for key, value in value_dict.items():
                for elem in (key, value):
                    match = re.search(pattern.lower(), str(elem).lower())
                    if match:
                        try:  # если совпадений на этот шаблон есть
                            match_dict[pattern].append(value_dict)
                        except KeyError:  # если совпадений на этот шаблон нет
                            match_dict[pattern] = [value_dict]

    return match_dict


def write_data(path, schema, data_list, mode='wb'):

    with open(path, mode) as file:
        fastavro.writer(file, schema, data_list)

        print('Writing complete.')

        file.close()


def replace_data(path, schema, new_path, replacement_dict):

    # функция для изменения имени ключа файла в схеме во избежание ValueError
    # если не изменить схему, то поменять имя ключа в файле нельзя будет
    def replace_schema(old_key, new_key):
        for key_dict in schema['fields']:
            for key, value in key_dict.items():
                if value == old_key:
                    key_dict[key] = new_key

    data_list = get_data(path, schema)  # данные полученные из файла

    for value_dict in data_list:
        for old_value, new_value in replacement_dict.items():
            for key, value in value_dict.copy().items():  # .copy() для избежания RuntimeError
                if value == old_value:
                    value_dict[key] = new_value  # замена значения на новое
                if key == old_value:
                    value_dict[new_value] = value_dict.pop(key)  # замена ключа
                    replace_schema(key, new_value)  # замена ключа в файле на новое имя

    write_data(new_path, schema, data_list)

    return schema
