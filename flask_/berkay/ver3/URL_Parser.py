from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter
from lxml import etree
from urllib.parse import urlsplit
import json

##import re
import os

def WordsOfWeb(url, process=False):

    nameCounter = len([i for i in os.listdir("textFiles") if i.startswith("url")])
    count_list_name = f"url{nameCounter}"
    #print(count_list_name)
    # list to collect url commons
    filen = os.path.join("textFiles", count_list_name)

    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # alt linkleri al
    # eğer alt link tıklanabilir haldeyse
    # yani "https://www" ile başlıyorsa


    if process:
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        wordList = text.split()

        word_frequency = Counter(wordList)
        #pprint(word_frequency)
        ### birinci madde bitimi ###

        ### ikinci madde başlangıcı ####
        # en çok kullanılan kelimelerden ilk 10 tanesi
        count_list_name_most = word_frequency.most_common(10)

        # first element of tuples
        firstItem = [i[0] for i in count_list_name_most]

        toWrite = open(f"{filen}.txt", "w")
        for item in firstItem:
            #with open(f"{filen}.txt", "w") as f:
            content = f"{item}\n"
            toWrite.write(content)

        nameCounter += 1

        return word_frequency.most_common()

    if not process:
        subUrls = []
        for link in soup.find_all('a'):
            if link.get('href').startswith("https://"):
                subUrls.append(link.get('href'))
        return subUrls[:3]



def intersection_():
    #filename = [i for i in os.listdir("textFiles")]
    #print(filename)
    commonWordCount = []
    fileCount = len([i for i in os.listdir("textFiles") if i.startswith("url")])
    #print(fileCount)
    for time in range(fileCount):
        words = open(f"textFiles/url{time}.txt").readlines()
        commonWordCount.append(words)



    # 3 tane alt url için 3 tane liste oluştu bir commonWordCount.append(words) komutu ile
    # o 3 tane listeyi tek bir liste içine attık ama yine kendi karakterlerine sahipler yani:
    # ([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # bu haldeler alltaki fonksiyon bu karakteri yok edip tek bir liste haline getirecek
    # yani işlemden sonra:
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # haline gelecek
    def flatten(lis):
        from collections.abc import Iterable

        for item in lis:
            if isinstance(item, Iterable) and not isinstance(item, str):
                for x in flatten(item):
                    yield x
            else:
                yield item

    ret = [common.strip() for common in list(flatten(commonWordCount))]
    """"
    ret2 = []
    for i in ret:
        ret2.append(i.strip())
    """

    # en çok kullanılan 10 tane kelimeyi almıştık
    mostUsedWords = [item for item, count in Counter(ret).items() if count > 1]
    #print(mostUsedWords)

    perc = (len(mostUsedWords) / 10) * 100

    return perc


def fileNameCreate(url):
    name = urlsplit(url)[1]
    name = name.split(".")
    if name[0] == "www":
        return name[1]
    else:
        return name[0]




# read and write urls
def readandWrite(url1 = None, url2 = None, file_ = None, R = None):
    if not R:
        with open(f"textFiles/{file_}.txt", "w") as f:
            t = "{},{}".format(url1, url2)
            f.write(t)
        f.close()

    elif R:
        with open(f"textFiles/{file_}.txt", "r") as f:
            liste = f.read()
            liste = liste.split(",")

        return liste




def parser(url, ret = None):
    ### birinci madde başlangıcı ####
    #urls = ["https://belgeler.yazbel.com/"]
    urls = []
    urls.append(url)

    for url in urls:
        allSubs = WordsOfWeb(url, process=False)

    #urls.append(allSubs)

    #print(allSubs)
    for sub in allSubs:
        freq = WordsOfWeb(sub, process=True)

    "aralarıdaki benzerlikleri bul"
    import json
    fileName = fileNameCreate(url)


    perc = intersection_()
    #perc, percBetween = intersection_()
    #percBetween = intersection_(fileName, asama2 = True)



    allInformation = {
        "ana_url": url,
        "alt_urller": allSubs,
        "freq": freq,
        "perc": perc,
        }

    jsonFile = json.dumps(allInformation, indent=4, ensure_ascii=False)
    with open(f"textFiles/{fileName}.json", "w") as f:
        f.write(jsonFile)
    if ret:
        return jsonFile
    if not ret:
        pass
