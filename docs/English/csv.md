# The .csv format
Call the function of this format:

**pulling.CSV.function(arguments)**
## Possible methods:
**get_data(path)** is a function that returns data from a file as a list, where each sublist is a row from the file and the sublist elements are columns in a row.

path - is the path to the desired file.


**find_data(path, pattern_list)** - a function that returns matches from file data in the form of a list, where the elements are the rows that match in the template.

path - the path to the required file.

pattern_list - a list with templates where each template is a separate element in the list.


**write_data(path, data_list, mode='w')** - a function that writes data to a file and saves it.

path - the path of the file in which the data should be written.

data_list - a list, where each sublist is a string, which should be saved to the file. And sublist elements are columns in a row.

mode - file opening mode. The default reading mode is 'w'.



**replace_data(path, new_path, replacement_dict)** - function that accepts dictionary with data, replaces data and saves these changes in a new file.

path - the path of the file from which the data should be taken.

new_path - the path of the file to which the changes should be written. If you enter the same path, the changes will be saved in this file.

replacement_dict - dictionary with data, where dictionary keys are data to be replaced, and dictionary element value is data to be replaced.