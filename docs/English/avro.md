# The .avro format
Call the function of this format:

**pulling.AVRO.function(arguments)**
## Possible methods:
**get_data(path, schema)** is a function that returns data from a file as a list, where list elements are dictionaries in the file.

path - the path to the desired file.

schema - a scheme describing data structure.


**find_data(path, schema, pattern_list)** - a function, which returns coincidences from file data as a dictionary, where the key is a search template and the value is a dictionary from the file, which was found by the template.

path - the path to the required file.

schema - a scheme, describing data structure.

pattern_list - a list with templates where each template is a separate list element.


**write_data(path, schema, data_list, mode='wb')** - a function that writes data to a file and saves it.

path - the path of the file where the data should be written to.

data_list - a list with dictionaries of data to be saved to the file.

mode - file opening mode. You can open it only in binary mode. The default mode is reading 'wb'.


**replace_data(path, schema, new_path, replacement_dict)** - function that accepts dictionary with data, replaces data, saves these changes in a new file and returns the changed schema.

path - the path of the file from which the data should be taken.

schema - a scheme describing data structure.

new_path - the path of the file, in which the changes should be written. If you enter the same path, the changes will be saved in this file.

replacement_dict - dictionary with data, where dictionary keys are the value to be replaced, and the value of dictionary elements are the data to be replaced.