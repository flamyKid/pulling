# The .rtf format
Call the function of this format:

**pulling.RTF.function(arguments)**
## Possible methods:
**get_text(path, coding='utf-8')** - is a function that returns text from a file as a list where list elements are sentences in the file.

path - the path to the required file.

coding - encoding for decoding. The default encoding is utf-8.


**find_text(path, pattern_list, coding='utf-8')** - a function that returns matches from the text of a file in the form of a dictionary, where the key is a match and the value is a search pattern by which a match was found.

path - the path to the required file.

pattern_list - a list with templates where each template is a separate list element.

coding - encoding for decoding. Encoding is utf-8 by default.


**write_text(path, line_list, mode='w', coding='utf-8')** - a function that writes text to a file and saves it.

path - the path of a file in which text should be written.

line_list - a list with lines to be saved to the file.

mode - open file mode. The default mode is reading 'w'.

coding - encoding for encoding or decoding (depends on the mode). Encoding is utf-8 by default.


**replace_text(path, new_path, replacement_dict, coding='utf-8', new_coding='utf-8')** - function that accepts dictionary with words, substitutes words and saves these changes in new file.

path - the path of the file from which the text should be taken.

new_path - the path of the file where the changes should be written. If you enter the same path, the changes will be saved in this file.

replacement_dict - dictionary with words where key is a word to be replaced and value is a word to be replaced.

coding - encoding for decoding. The default encoding is utf-8.

new_coding - encoding for encoding. The default encoding is utf-8.