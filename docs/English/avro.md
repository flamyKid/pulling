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