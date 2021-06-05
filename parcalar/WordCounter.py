# bir url al onun içindeki kelimelerin sayılarını bul

import requests
from pprint import pprint 
from collections import Counter

url = "https://ybgirgin3.github.io/"

r = requests.get(url)
# ret = r.content
kaynak_kodu = r.text
#print(ret)

kelime_listesi = kaynak_kodu.split()

kelime_freq = []
for kelime in kelime_listesi:
    kelime_freq.append(kelime_listesi.count(kelime))


# kelimeler ve sayıları
#ret = str(list(zip(kelime_listesi, kelime_freq)))
ret = list(zip(kelime_listesi, kelime_freq))
pprint(Counter(ret))
