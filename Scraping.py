"""
devo estrarre 'URL' del primo '<a', contenuto nel '<div class="yuRUbf">'
"""

from urllib import request
if __name__ == '__main__':
    key = input("Cosa vuoi cercare?: ")
    response = request.urlopen("https://www.google.com/search?client=firefox-b-d&q="+key)
    page_source = response.read().decode('8859')
    print(page_source)