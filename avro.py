import re
import fastavro


def get_data(path, schema):
    # возвращаемый список с текстом
    text_list = list()

    with open(path, 'rb') as file:
        reader = fastavro.reader(file, schema)

        for elem in reader:
            text_list.append(elem)

    return text_list


def find_data(path, schema, pattern_list):
    # возвращаемый словарь с совпадениями
    match_dict = dict()

    text_list = get_data(path, schema)
    print(text_list)

    for value_dict in text_list:
        for pattern in pattern_list:
            for key, value in value_dict.items():
                for elem in (key, value):
                    try:  # если цифр не будет
                        match = re.search(pattern.lower(), elem.lower())
                        if match:
                            match_dict[pattern] = value_dict
                    except:  # если попадется цифра
                        match = re.search(pattern.lower(), str(elem))
                        if match:
                            match_dict[pattern] = value_dict

    return match_dict


def write_data(path, schema, data, mode='wb'):

    with open(path, mode) as file:
        fastavro.writer(file, schema, data)

        print('Writing complete')

        file.close()


def replace_data(path, schema, new_path, word_dict):
    text_list = get_data(path, schema)

    for value_dict in text_list:
        for old_value, new_value in word_dict.items():
            for key, value in value_dict.items():
                if value == old_value:
                    value_dict[key] = new_value  # замена значения на новое
                if key == old_value:
                    value_dict[new_value] = value_dict.pop(key)  # замена ключа

    write_data(new_path, schema, text_list)
