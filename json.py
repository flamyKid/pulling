import re
import json


def get_data(path):
    with open(path, 'r') as file:
        data = json.load(file)

        file.close()

    return data


def find_data(path, pattern_list):
    # возвращаемый словарь с совпадениями
    match_dict = dict()

    def check_dict(Dict):
        for key, value in Dict.items():
            check_type(key, Dict)
            check_type(value, Dict)

    def check_list(List):
        for elem in List:
            check_type(elem, List)

    # добавление элементов в словарь
    def add_to_dict(elem, parent):
        for pattern in pattern_list:
            match = re.search(pattern.lower, str(elem).lower())
            if match:
                if parent:
                    match_dict[elem] = parent
                else:  # если родитель - изначальный словарь
                    match_dict[key] = value

    def check_type(elem, parent):  # аргумент parent для того, что бы не копировать словарь из функции get_data
        if isinstance(elem, (int, float)):
            add_to_dict(elem, parent)
        elif isinstance(elem, list):
            check_list(elem)
        elif isinstance(elem, dict):
            check_dict(elem)
        else:
            add_to_dict(elem, parent)

    data = get_data(path)  # данные полученные из файла

    for key, value in data.items():
        check_type(key, None)
        check_type(value, None)

    return match_dict


def write_data(path, data, mode='w'):
    with open(path, mode) as file:
        json.dump(data, file)

        print('Writing complete')

        file.close()


def replace_data(path, new_path, data_dict, mode='w'):

    # проверка элементов внутренних словарей
    def check_dict(Dict):
        for old_value, new_value in data_dict.items():
            for key, value in Dict.copy().items():  # .copy() для избежания RuntimeError
                if isinstance(value, list):
                    check_type(value)
                elif isinstance(value, dict):
                    check_type(value)
                else:  # если без вложенностей
                    if value == old_value:
                        Dict[key] = new_value  # замена значения на новое
                    elif key == old_value:
                        Dict[new_value] = Dict.pop(key)  # замена ключа

    # проверка элементов внутренних списков
    def check_list(List):
        for elem in List:
            if isinstance(elem, dict):
                check_type(elem)
            elif isinstance(elem, list):
                check_type(elem)
            else:  # если без вложенностей
                for old_value, new_value in data_dict.items():
                    if elem == old_value:
                        index = List.index(elem)
                        List[index] = new_value

    # для значений изначального словаря без вложенностей
    def replace(elem):
        for old_value, new_value in data_dict.items():
            if elem == value:
                if elem == old_value:
                    data[key] = new_value  # замена значения на новое
            elif elem == key:
                if key == old_value:
                    data[new_value] = data.pop(key)  # замена ключа

    # проверка на тип
    def check_type(elem):
        if isinstance(elem, (int, float)):
            replace(elem)
        elif isinstance(elem, list):
            check_list(elem)
        elif isinstance(elem, dict):
            check_dict(elem)
        else:
            replace(elem)

    data = get_data(path)  # данные полученные из файла

    for key, value in data.copy().items():  # .copy() для избежания RuntimeError
        check_type(key)
        check_type(value)

    write_data(new_path, data, mode)
