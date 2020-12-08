# The .json format
Call the function of this format:

**pulling.JSON.function(arguments)**
## Possible methods:
**get_data(path)** is a function that returns data from a file as a data dictionary.

path - the path to the desired file.


**find_data(path, pattern_list)** - a function that returns matches from file data in the form of a dictionary, where the key is the search word, and the value is the parent dictionary of the element, if there is only one element with this name, and a list with parents for all elements with the search name.

path - the path to the required file.

pattern_list - a list with templates where each template is a separate element in the list.


**write_data(path, data_dict, mode='w')** - a function that writes data to a file and saves it.

path - the path of the file to which the data should be written.

data_dict - dictionary with data, which should be written to a file.

mode - open file mode. The default mode is reading 'w'.


**replace_data(path, new_path, replacement_dict, mode='w')** - function that accepts dictionary with data, replaces data and saves these changes in new file.

path - the path of the file from which the data should be taken.

new_path - the path of the file, in which the changes should be written. If you enter the same path, the changes will be saved in this file.

replacement_dict - dictionary with values, where dictionary keys are the value to be replaced, and dictionary element value is the value to be replaced.

mode - file opening mode. The default reading mode is 'w'.
