# Формат .json
Вызов функций этого формата:

> **import pulling.Json as json**
>
> **json.функция(аргументы)**
## Возможные методы:
**get_data(** *path* **)** - функция, которая возвращает данные из файла, в виде словаря с данными.

 - *path* - путь к нужному файлу.


**find_data(** *path*, *pattern_list* **)** - функция, которая возвращает совпадения из данных файла в виде словаря, где ключ - искомое слово, а значение - это словарь-родитель элемента, если элемент с таким именем один, и список с родителями для всех элементов с искомым именем.

 - *path* - путь до нужного файла.

 - *pattern_list* - список с шаблонами, где каждый шаблон является отдельным элементом списка.


**write_data(** *path*, *data_dict*, *mode='w'* **)** - функция, которая записывает данные в файл и сохраняет его.

 - *path* - путь файла в который надо записать данные.

 - *data_dict* - словарь с данными, которые нужно записать в файл.

 - *mode* - режим открытия файла. По умолчанию стоит режим чтения 'w'.


**replace_data(** *path*, *new_path*, *replacement_dict*, *mode='w'* **)** - функция, которая принимает словарь с данными, заменяет данные и сохраняет эти изменения в новом файле.

 - *path* - путь файла из которого надо взять данные.

 - *new_path* - путь файла, в который надо записать изменения. Если ввести тот же путь, то изменения сохранятся в этом файле.

 - *replacement_dict* - словарь со значениями, где ключи словаря - это значение, которое надо заменить, а значение элемента словаря - значение на которое надо заменить.

 - *mode* - режим открытия файла. По умолчанию стоит режим чтения 'w'.
## Пример кода
> import pulling.Json as json
> 
> path = 'path\\file.json'
> 
> data = {
    'list': [ 1, 2, 3, 4, 5 ], 
    'president': { 'name': 'Zaphod Beeblebrox', 'species': 'Betelgeusian', 'just_number': 2 }
}

> json.write_data(path, data)
>> Writing complete.

> found_data = json.find_data(path, [ 'list', 'Zaphod Beeblebrox' ])
> 
> print(found_data)
>> { 
>>
>> 'child of this element(list)': [ 1, 2, 3, 4, 5 ], 
>>
>> 'Zaphod Beeblebrox': [ { 'name': 'Zaphod Beeblebrox', 'species': 'Betelgeusian', 'just_number': 2 } ] 
>>
>> }

> json.replace_data(path, path, { 2: '2', 'list': 'List' })
>> Writing complete.

> result_data = json.get_data(path)
> 
> print(result_data)
>> { 'president': { 'name': 'Zaphod Beeblebrox', 'species': 'Betelgeusian', 'just_number': '2' }, 'List': [ 1, '2', 3, 4, 5 ] }