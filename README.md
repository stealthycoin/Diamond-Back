diamond-back
============

n-back implementation in python and javascript.


[N-back wiki page](http://en.wikipedia.org/wiki/N-back)


Example Usage
---------

1. Make alphabet file. Define symbols and the HTML those symbols markup (by default the symbol itself is used as the markup).
2. Use Diamond-Back.py to generate a map.js using the alphabet file. Example: ```python diamond-back.py alphabet-file 20``` gives a sequence of length 20 with distribution defined in the alphabet file.
3. Open main.html in a browser.