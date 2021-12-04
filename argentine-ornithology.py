from bs4 import BeautifulSoup
 
soup = BeautifulSoup("<html><p>This is <b>invalid HTML</p></html>", "lxml")

print(soup)