# Формат .pdf
Вызов функций этого формата:

> **import pulling.Pdf as pdf**
>
> **pdf.функция(аргументы)**
##Возможные методы:
**get_text(** *path* **)** - функция, которая возвращает текст из файла, в виде списка, где элементы списка - это предложения в файле.

 - *path* - путь к нужному файлу.


**find_text(** *path*, *pattern_list* **)** - функция, которая возвращает совпадения из текста файла в виде словаря, где ключ - это шаблон поиска, а значение - это список с найденными совпадениями.

 - *path* - путь до нужного файла.

 - *pattern_list* - список с шаблонами, где каждый шаблон является отдельным элементом списка.
## Пример кода
> import pulling.Pdf as pdf
> 
> path = 'path\\file.pdf'

> result_text = pdf.get_text(path)
> 
> print(result_text)
>> [ 'Hello World', 'It is the ItYaS' ]

> found_text = pdf.find_text(path, ['ItYaS'])
> 
> print(found_text)
>> { 'ItYaS': [ 'It is the ItYaS' ] }