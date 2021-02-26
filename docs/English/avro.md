# The .avro format
Call the functions of this format:

> **import pulling.Avro as avro**
>
> **avro.function(arguments)**
## Possible methods:
**get_data(** *path*, *schema* **)** is a function that returns data from a file as a list, where list elements are dictionaries in the file.

 - *path* is the path to the desired file.

 - *schema* - scheme, which describes data structure.


**find_data(** *path*, *schema*, *pattern_list* **)** - a function that returns matches from a file as a dictionary, where the key is a search template and the value is a list with the found matches.

 - *path* - is the path to the required file.

 - *schema* - a scheme describing data structure.

 - *pattern_list* - a list with templates, where each template is a separate list element.


**write_data(** *path*, *schema*, *data_list*, *mode='wb'* **)** - a function that writes data to a file and saves it.

 - *path* - the path of the file to which data should be written.

 - *data_list* - a list with data dictionaries, which should be saved to the file.


**replace_data(** *path*, *schema*, *new_path*, *replacement_dict* **)** - a function that accepts dictionary with data, replaces data, saves these changes in a new file and returns a new scheme.

 - *path* - the path of the file from which the data should be taken.

 - *schema* - scheme, which describes data structure.

 - *new_path* - path of the file, in which the changes should be written. If you enter the same path, the changes will be saved in this file.

 - *replacement_dict* - data dictionary, where dictionary keys are the value to be replaced, and the value of dictionary elements are the data to be replaced.
## Code sample
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
>       { 'station': '011990-99999', 'time': 1433269388, 'temp': 0 }, 
>
>       { 'station': '011990-99999', 'time': 1433270389, 'temp': 22 }, 
>
>       { 'station': '011990-99999', 'time': 1433273379, 'temp': -11 }, 
>
>       { 'station': '011990-99999', 'time': 1433275478, 'temp': 111 }
>
> ]

> avro.write_data(path, schema, records)
>> Writing complete.

> found_data = json.find_data(path, schema, [ '011990-99999' ])
> 
> print(found_data)
>> { '-11': { 'station': '011990-99999', 'time': 1433273379, 'temp': -11 } }

> new_schema = avro.replace_data(path, schema, path, { '011990-99999': '..numbers..', 'temp': 'key' })
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

> result_data = avro.get_data(path, schema)
> print(result_data)
>> [
>> 
>> { 'station': '..numbers..', 'time': 1433269388, 'key': 0 }, 
>>
>> { 'station': '..numbers..', 'time': 1433270389, 'key': 22 }, 
>>
>> { 'station': '..numbers..', 'time': 1433273379, 'key': -11 }, 
>>
>> { 'station': '..numbers..', 'time': 1433275478, 'key': 111 }
>>
>> ]
