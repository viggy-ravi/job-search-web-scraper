'''
web_scraper_test.py
Example HTML reader/parser
References: 
https://www.dataquest.io/blog/web-scraping-tutorial-python/
https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
https://www.dataquest.io/blog/python-api-tutorial/
'''

import requests
from bs4 import BeautifulSoup

'''
# get request
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
 
# Status Codes
## 1xx - informational response
## 2xx - success
## 3xx - redirection
## 4xx - client error
## 5xx - server error
print(page.status_code)
print('\n')
 
# Print content - not pretty
print(page.content)
print('\n')
 
# bs4 is a HTML/XML parser
soup = BeautifulSoup(page.content, 'html.parser')

# Print content - pretty
print(soup.prettify()) 
print('\n')
 
# Tells us there are 2 tags: <!DOCTYPE html> and <html>
print(list(soup.children))
print('\n')
 
# Tells us the type (class) of each element in the list
## Doctype object: contains info about the type of the document
## NavigableString object: represents TEXT found in the HTML document
## Tag object (most important): allows us to navigate through an HTML document
print([type(item) for item in list(soup.children)])
print('\n')
 
# Select html tag and get all it's children
html = list(soup.children)[2]
print(list(html.children))
print('\n')
 
# Get paragraph in body
body = list(html.children)[3]
print(list(body.children))
print('\n')
 
# Isolate paragraph
p = list(body.children)[1]
print(p.get_text)
print('\n')
 
# Final all instances of a tag at once - can loop through and use .get_text to extract text
# use soup.find() to find first instance of tag
print(soup.find_all('p'))
print('\n')
'''


# NEW HTML FILE
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
print('\n')

# Find by class
print(soup.find_all('p', class_='outer-text'))
print('\n')

# Find by ID
print(soup.find_all(id='first'))
print('\n')

# CSS Selectors - select ~ find/find_all
print(soup.select("div p"))
print('\n')

