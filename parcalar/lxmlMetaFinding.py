import requests as req
from lxml import etree
import re

#url = "https://ybgirgin3.github.io/"
url = "http://www.w3schools.com/XPath/xpath_syntax.asp" 


r = req.get(url).text

tree = etree.HTML(r)
m = tree.xpath( "//meta[@name='Keywords']" )[0].get("content")
print(m)




