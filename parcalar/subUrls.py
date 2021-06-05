import requests
from bs4 import BeautifulSoup
 
 
url = 'https://www.geeksforgeeks.org/'
#url = "https://ybgirgin3.github.io/"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    if link.get('href').startswith("https://www"):
        urls.append(link.get('href'))

print(urls[:3])