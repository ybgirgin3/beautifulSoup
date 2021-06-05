import requests as req
from lxml import etree
import re

#url = "https://ybgirgin3.github.io/"
url = "http://www.w3schools.com/XPath/xpath_syntax.asp" 
url2 = "https://www.w3schools.com/js/default.asp"


r1 = req.get(url).text
r2 = req.get(url).text


tree1 = etree.HTML(r1)
tree2 = etree.HTML(r2)

m1 = tree1.xpath( "//meta[@name='Keywords']" )[0].get("content")
m2 = tree2.xpath( "//meta[@name='Keywords']" )[0].get("content")
metaList1 = m1.split(",")
metaList2 = m2.split(",")
#print(metaList1)
#print(metaList2)

# percentage of intersection of meta words
ret = len(set(metaList1) & set(metaList2)) / float(len(set(metaList1) | set(metaList2))) * 100
print(ret)



