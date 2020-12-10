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
                    try:  # если цифр не будет
                        match = re.search(pattern.lower(), elem.lower())
                        if match:
                            try:  # если совпадений на этот шаблон есть
                                match_dict[pattern].append(value_dict)
                            except KeyError:  # если совпадений на этот шаблон нет
                                match_dict[pattern] = [value_dict]
                    except:  # если попадется цифра
                        match = re.search(pattern.lower(), str(elem))
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
            for key, val in key_dict.items():
                if val == old_key:
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


if __name__ == '__main__':
    schema = {
        'doc': 'A weather reading.',
        'name': 'Weather',
        'namespace': 'test',
        'type': 'record',
        'fields': [
            {'name': 'station', 'type': 'string'},
            {'name': 'time', 'type': 'long'},
            {'name': 'temp', 'type': 'int'},
        ],
    }

    records = [
        {'station': '011990-99999', 'temp': 0, 'time': 1433269388},
        {'station': '011990-99999', 'temp': 22, 'time': 1433270389},
        {'station': '011990-99999', 'temp': -11, 'time': 1433273379},
        {'station': '012650-99999', 'temp': 111, 'time': 1433275478},
    ]

    path = 'test\\test.avro'

    write_data(path, schema, records)

    print('__________')
    found_data = find_data(path, schema, ['011990-99999'])
    for k, v in found_data.items():
        print(f'{k}: {v}')
    print('__________')

    new_schema = replace_data(path, schema, path, {'011990-99999': '..numbers..', 'temp': 'key'})
    print(new_schema)

    result_data = get_data(path, schema)
    print(result_data)
