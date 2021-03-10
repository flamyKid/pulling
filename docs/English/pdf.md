# The .pdf format
Call the functions of this format:

```python
import pulling.Pdf as pdf

pdf.function(arguments)
```
## Possible methods:
**get_text(** *path* **)** is a function that returns text from a file as a list, where list elements are sentences in the file.

 - *path* - the path to the desired file.


**find_text(** *path*, *pattern_list* **)** - a function that returns matches from a file text as a dictionary, where the key is a search pattern and the value is a list of found matches.

 - *path* - is the path to the required file.

 - *pattern_list* - a list with templates, where each template is a separate list element.