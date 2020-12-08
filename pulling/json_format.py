import re
import json


class JSON:

    def get_data(self, path):
        with open(path, 'r') as file:
            data_dict = json.load(file)

            file.close()

        return data_dict

    def find_data(self, path, pattern_list):
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

            # добавление нового словаря в список словарей
            def add_dict_to_list(List, Dict):
                new_elements_list = []

                for dicts in List:
                    new_elements_list.append(dicts)

                new_elements_list.append(Dict)

                return new_elements_list

            for pattern in pattern_list:
                match = re.search(pattern.lower(), str(elem).lower())
                if match:
                    if parent:
                        # блок try на случай, если элемента с таким именем не было еще
                        try:  # если есть несколько ключей с одним именем
                            dict_elem = match_dict[elem]
                            if dict_elem:
                                # проверка, чтобы словарь с несколькими элементами не прошел
                                if isinstance(dict_elem, list) and len(dict_elem) >= 2:
                                    # только для списка со словарями совпадений
                                    elements_list = add_dict_to_list(dict_elem, parent)
                                else:  # если такое имя было, но один раз
                                    elements_list = [dict_elem, parent]  # добавление нового словаря к первому
                                match_dict[elem] = elements_list
                        except KeyError:  # если такого же имени у ключа не было
                            match_dict[elem] = parent
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

        data_dict = self.get_data(path)  # данные полученные из файла

        for key, value in data_dict.items():
            check_type(key, None)
            check_type(value, None)

        return match_dict

    def write_data(self, path, data_dict, mode='w'):
        with open(path, mode) as file:
            json.dump(data_dict, file)

            print('Writing complete')

            file.close()

    def replace_data(self, path, new_path, replacement_dict, mode='w'):

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

        data_dict = self.get_data(path)  # данные полученные из файла

        check_type(data_dict)

        self.write_data(new_path, data_dict, mode)


if __name__ == '__main__':
    data = {
        'int': {'list': 5, 'fl': 4, 'ok!': 555},
        'list': [1, 2, 3,
                 {'str': 'ok!', 'list': [1, 2]}],
        'president': {'name': 'Zaphod Beeblebrox', 'species': 'Betelgeusian', 'list': 5}
            }

    path = 'test/test.json'
    Json = JSON()

    Json.write_data(path, data)

    print('__________')
    found_data = Json.find_data(path, ['president', 'ok!', 'list', 'Zaphod Beeblebrox'])
    for k, v in found_data.items():
        print(f'{k}: {v}')
    print('__________')

    Json.replace_data(path, path, {'int': 'float', 'ok!': 'okay', 2: '2', 'list': 'List'})

    result_data = Json.get_data(path)
    print(result_data)
