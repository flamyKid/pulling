# Text parsing
Call the function to parse data from web pages:

**pulling.parsing.function(s) **
## Possible methods:
**get_text(url)** is a function that returns text from a page as a list where list elements are information from tags (h, p, a, img, span). Elements with links have addresses saved in the dictionary, which is also added from the list.

url - the address of the desired page.


**find_text(url, pattern_list)** - a function that returns matches from page tags as a dictionary, where the key is a match, and the value is a search pattern by which a match or a link contained in a tag was found.

url is the address of the required page.

pattern_list - a list with templates where each template is a separate element.