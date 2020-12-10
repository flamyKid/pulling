import re
import json


def get_data(path):
    with open(path, 'r') as file:
        data_dict = json.load(file)

        file.close()

    return data_dict


def find_data(path, pattern_list):
    # возвращаемый словарь с совпадениями
    match_dict = dict()

    # проверка элементов внутренних словарей
    def check_dict(Dict):
        for key, value in Dict.items():
            check_type(key, Dict)
            check_type(value, Dict)

    # проверка элементов внутренних списков
    def check_list(List):
        for elem in List:
            check_type(elem, List)

    # добавление элементов в словарь
    def add_to_dict(elem, parent):

        for pattern in pattern_list:
            match = re.search(pattern.lower(), str(elem).lower())
            if match:
                if parent:
                    # блок try на случай, если элемента с таким именем не было еще
                    try:  # если совпадений на этот шаблон есть
                        match_dict[pattern].append(parent)
                    except KeyError:  # если совпадений на этот шаблон нет
                        match_dict[pattern] = [parent]
                else:  # если родитель - самый первый словарь
                    match_dict[f'child of this element({elem})'] = value

    # проверка на тип и вызов нужных функций
    def check_type(elem, parent):  # аргумент parent для того, что бы не копировать начальный словарь
        if isinstance(elem, (int, float)):
            add_to_dict(elem, parent)
        elif isinstance(elem, list):
            check_list(elem)
        elif isinstance(elem, dict):
            check_dict(elem)
        else:
            add_to_dict(elem, parent)

    data_dict = get_data(path)  # данные полученные из файла

    for key, value in data_dict.items():
        check_type(key, None)
        check_type(value, None)

    return match_dict


def write_data(path, data_dict, mode='w'):
    with open(path, mode) as file:
        json.dump(data_dict, file)

        print('Writing complete.')

        file.close()


def replace_data(path, new_path, replacement_dict, mode='w'):

    # проверка элементов внутренних словарей
    def check_dict(Dict):
        for old_value, new_value in replacement_dict.items():
            for key, value in Dict.copy().items():  # .copy() для избежания RuntimeError
                if isinstance(value, list):
                    check_type(value)
                if isinstance(value, dict):
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
                for old_value, new_value in replacement_dict.items():
                    if elem == old_value:
                        index = List.index(elem)
                        List[index] = new_value

    # проверка на тип и вызов нужных функций
    def check_type(elem):
        if isinstance(elem, list):
            check_list(elem)
        elif isinstance(elem, dict):
            check_dict(elem)

    data_dict = get_data(path)  # данные полученные из файла

    check_type(data_dict)

    write_data(new_path, data_dict, mode)


if __name__ == '__main__':
    data = {
        'list': [1, 2, 3, 4, 5],
        'president': {'name': 'Zaphod Beeblebrox', 'species': 'Betelgeusian', 'list': 5}
            }

    path = 'test\\test.json'

    write_data(path, data)

    print('__________')
    found_data = find_data(path, ['list', 'Zaphod Beeblebrox'])
    for k, v in found_data.items():
        print(f'{k}: {v}')
    print('__________')

    replace_data(path, path, {2: '2', 'list': 'List'})

    result_data = get_data(path)
    print(result_data)
