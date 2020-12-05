# The .docx format
Call the function of this format:

**pulling.DOCX.function(arguments)**
## Possible methods:
**get_text(path)** is a function that returns text from a file as a list, where list elements are sentences in the file.

path - the path to the desired file.


**find_text(path, pattern_list)** - a function that returns matches from a file in the form of a dictionary, where the key is a match and the value is a search pattern by which a match was found.

path - the path to the required file.

pattern_list - a list with templates where each template is a separate list element.