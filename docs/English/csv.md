# The .csv format
Call the functions of this format:

> **import pulling.Csv as csv**
>
> **csv.function(arguments)**
## Possible methods:
**get_data(** *path* **)** is a function that returns data from a file as a list, where each sublist is a row from the file and the sublist elements are columns in a row.

 - *path* is the path to the required file.


**find_data(** *path*, *pattern_list* **)** - a function that returns matches from file data as a dictionary, where the key is a search pattern and the value is a list with found matches.

 - *path* - is the path to the required file.

 - *pattern_list* - a list with templates, where each template is a separate list element.


**write_data(** *path*, *data_list*, *mode='w'* **)** is a function that writes data to a file and saves it.

 - *path* - the path of the file to which the data should be written.

 - *data_list* - a list, where each sublist is a string to be saved to the file. And sublist elements are columns in a row.

 - *mode* - file opening mode. The default reading mode is 'w'.



**replace_data(** *path*, *new_path*, *replacement_dict* **)** - a function that accepts dictionary with data, replaces data and saves these changes in a new file.

 - *path* - file path from which data should be taken.

 - *new_path* - path of the file, in which the changes should be written. If you enter the same path, the changes will be saved in this file.

 - *replacement_dict* - dictionary with data, where dictionary keys are data to be replaced, and dictionary element value is data to be replaced.
## Code sample
> import pulling.Avro as avro
>
> path = 'path\\file.csv'.
> 
> data = [ ['Name', 'Age'] , ['Seraphim', '16'] , ['Nikolas', '13'] ]. 

> csv.write_data(path, data)
>> Writing complete.

> found_data = csv.find_data(path, ['16', 'Nikolas']).
> 
> print(found_data)
>> {
>>
>> '16': ['Seraphim', '16'], 
>>
>> 'Nikolai': ['Nicholas', '13'] 
>>
>> }


> csv.replace_data(path, path, {'Nikolas': 'Kolya', '16': '17' }).
>> Writing complete.

> result_data = csv.get_data(path)
> 
> print(result_data)
>> [ ['Name', 'Age'], ['Seraphim', '17'], ['Kolya', '13'] ]