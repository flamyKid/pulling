# Формат .avro
Вызов функций этого формата:

> **import pulling.Avro as avro**
>
> **avro.функция(аргументы)**
## Возможные методы:
**get_data(** *path*, *schema* **)** - функция, которая возвращает данные из файла, в виде списка, где элементы списка - это словари в файле.

 - *path* - путь к нужному файлу.

 - *schema* - схема, описывающая сериализуемую\десериализуемую структуру данных.


**find_data(** *path*, *schema*, *pattern_list* **)** - функция, которая возвращает совпадения из данных файла в виде словаря, где ключ - это шаблон поиска, а значение - это список с найденными совпадениями.

 - *path* - путь до нужного файла.

 - *schema* - схема, описывающая сериализуемую\десериализуемую структуру данных.

 - *pattern_list* - список с шаблонами, где каждый шаблон является отдельным элементом списка.


**write_data(** *path*, *schema*, *data_list*, *mode='wb'* **)** - функция, которая записывает данные в файл и сохраняет его.

 - *path* - путь файла в который надо записать данные.

 - *data_list* - список со словарями данных, которые нужно сохранить в файле.


**replace_data(** *path*, *schema*, *new_path*, *replacement_dict* **)** - функция, которая принимает словарь с данными, заменяет данные, сохраняет эти изменения в новом файле и возвращает новую схему.

 - *path* - путь файла из которого надо взять данные.

 - *schema* - схема, описывающая сериализуемую\десериализуемую структуру данных.

 - *new_path* - путь файла, в который надо записать изменения. Если ввести тот же путь, то изменения сохранятся в этом файле.

 - *replacement_dict* - словарь с данными, где ключи словаря - это значение, которое надо заменить, а значение элементов словаря - данные на которые надо заменить.
## Пример кода
> import pulling.Avro as avro
>
> path = 'path\\file.avro'
> 
> data = {
>
>       'doc': 'A weather reading.', 
>
>       'name': 'Weather', 
> 
>       'namespace': 'test', 
> 
>       'type': 'record', 
> 
>       'fields': [ { 'name': 'station', 'type': 'string' }, 
> 
>                   { 'name': 'time', 'type': 'long' }, 
>
>                   { 'name': 'temp', 'type': 'int' } ]
> 
> }
>
> records = [
> 
>       { 'station': '1', 'time': 1433269388, 'temp': 0 }, 
>
>       { 'station': '2', 'time': 1433270389, 'temp': 22 }, 
>
>       { 'station': '3', 'time': 1433273379, 'temp': -11 }, 
>
>       { 'station': '4', 'time': 1433275478, 'temp': 111 }
>
> ]

> json.write_data(path, schema, records)
>> Writing complete.

> found_data = json.find_data(path, schema, ['3'])
> 
> print(found_data)
>> { 3: { 'station': '3', 'time': 1433273379, 'temp': -11 } }

> new_schema = json.replace_data(path, schema, path, {'1': 'one', 'temp': 'key'})
> 
> print(new_schema)
>> Writing complete.
>>
>> {
>>
>> 'doc': 'A weather reading.', 
>>
>> 'name': 'Weather', 
>> 
>> 'namespace': 'test', 
>> 
>> 'type': 'record', 
>> 
>> 'fields': [ { 'name': 'station', 'type': 'string' }, 
>> 
>>           { 'name': 'time', 'type': 'long' }, 
>> 
>>           { 'name': 'key', 'type': 'int' } ]
>> 
>> }

> result_data = json.get_data(path, schema)
> print(result_data)
>> [
>> 
>> { 'station': 'one', 'time': 1433269388, 'key': 0 }, 
>>
>> { 'station': '2', 'time': 1433270389, 'key': 22 }, 
>>
>> { 'station': '3', 'time': 1433273379, 'key': -11 }, 
>>
>> { 'station': '4', 'time': 1433275478, 'key': 111 }
>>
>> ]