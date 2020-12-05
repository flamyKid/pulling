import re
import csv


class CSV:

    def get_data(self, path):
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

    def find_data(self, path, pattern_list):
        # возвращаемый список с совпадениями
        match_list = list()

        data_list = self.get_data(path)  # данные полученные из файла

        for row in data_list:  # строки
            for column in row:  # столбец
                for pattern in pattern_list:
                    match = re.search(pattern.lower(), column.lower())
                    if match:
                        match_list.append(row)

        return match_list

    def write_data(self, path, data_list, mode='w'):

        with open(path, mode, newline='') as file:  # newline для открытия файла в excel без багов
            writer = csv.writer(file, delimiter=';')
            for elem in data_list:
                writer.writerow(elem)

            print('Writing complete')

            file.close()

    def replace_data(self, path, new_path, replacement_dict):
        data_list = self.get_data(path)  # данные полученные из файла

        for row in data_list:  # строки
            for column in row:  # столбец
                for old_value, new_value in replacement_dict.items():
                    if column == old_value:
                        index = row.index(column)
                        row[index] = new_value

        self.write_data(new_path, data_list, 'w')


if __name__ == '__main__':
    data = [['Имя', 'Возраст'], ['ityas', '16'], ['dore', '13']]

    path = 'test/test.csv'
    Csv = CSV()

    Csv.write_data(path, data)

    found_data = Csv.find_data(path, ['ityas'])
    print(found_data)

    Csv.replace_data(path, path, {'dore': 'Dore', '16': '17'})

    result_data = Csv.get_data(path)
    print(result_data)
