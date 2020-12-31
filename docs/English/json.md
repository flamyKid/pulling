# The .json format
Call the functions of this format:

> **import pulling.Json as json**
>
> **json.function(arguments)**
## Possible methods:
**get_data(** *path* **)** is a function that returns data from a file as a data dictionary.

 - *path* is a path to the desired file.


**find_data(** *path*, *pattern_list* **)** - the function that returns matches from the file data as a dictionary, where the key is the searched word and the value is the parent dictionary of the element if the element with such name is the same, and the list with the parents for all elements with the searched name.

 - *path* is the path to the required file.

 - *pattern_list* - a list with templates, where each template is a separate element of the list.


**write_data(** *path*, *data_dict*, *mode='w'* **)** - a function that writes data to a file and saves it.

 - *path* - the path of the file to which the data should be written.

 - *data_dict* - dictionary with data, which should be written to a file.

 - *mode* - file opening mode. The default mode is reading 'w'.


**replace_data(** *path*, *new_path*, *replacement_dict*, *mode='w'* **)** - a function that accepts dictionary with data, replaces data and saves these changes in a new file.

 - *path* - the path of the file from which the data should be taken.

 - *new_path* - path of file, to which changes should be written. If you enter the same path, the changes will be saved in this file.

 - *replacement_dict* - dictionary with values, where dictionary keys are the value to be replaced, and dictionary element value is the value to be replaced.

 - *mode* - file opening mode. The default reading mode is 'w'.
## Code sample
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