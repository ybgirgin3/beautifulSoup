from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter
from lxml import etree
from urlNameCreator import fileNameCreate
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


    ret = list(flatten(commonWordCount))
    ret2 = []
    for i in ret:
        ret2.append(i.strip())

    # en çok kullanılan 10 tane kelimeyi almıştık
    mostUsedWords = [item for item, count in Counter(ret2).items() if count > 1]
    #print(mostUsedWords)

    perc = (len(mostUsedWords) / 10) * 100
    # print(perc)
    return perc


""""
def intersection_(filename, asama2 = None):
    import json
    # json reading inner func
    if asama2:
        jsonName = []
        for item in os.listdir("textFiles"):
            if item != "merged_file.json":
                jsonName.append(item)


        def calcPerc(filename):
            with open(f"textFiles/{filename}", "r") as f:
                ret = f.read()

            return json.loads(ret)


        json1 = calcPerc(jsonName[0])
        json2 = calcPerc(jsonName[1])

        json1C = Counter(json1['freq'])
        json2C = Counter(json2['freq'])


        json1Most = json1C.most_common(10)
        json2Most = json2C.most_common(10)

        #allFreq = len(json1Most) + len(json2Most)

        data = len(set(json1Most)&set(json2Most)) / float(len(set(json1Most) | set(json2Most))) * 100

        return data

    if not asama2:
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


        ret = list(flatten(commonWordCount))
        ret2 = []
        for i in ret:
            ret2.append(i.strip())

        # en çok kullanılan 10 tane kelimeyi almıştık
        mostUsedWords = [item for item, count in Counter(ret2).items() if count > 1]
        #print(mostUsedWords)

        perc = (len(mostUsedWords) / 10) * 100
        # print(perc)
        return perc



"""







def printingTree(url, subUrl, wordFreq, perc):

    # siteyi ve benzerlik oranını dosyaya kaydet
    toWrite = f"urls: {url} => score: {perc}\n"
    with open(os.path.join("textFiles", "intersectionScores.txt"), "a") as f:
        f.write(toWrite)

    #print(wordFreq)
    # site içinde geçen tüm kelimeleri istiyor
    #wordFreq = wordFreq.most_common(10)

    retList = [url, subUrl, perc, wordFreq]
    return retList


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


    #perc = intersection_(fileName, asama2 = None)
    perc = intersection_()
    #percBetween = intersection_(fileName, asama2 = True)

    ret = printingTree(url, allSubs, freq, perc)



    allInformation = {
        "ana_url": url,
        "alt_urller": allSubs,
        "freq": freq,
        "perc": perc,
        #"percBetween": percBetween
        }

    jsonFile = json.dumps(allInformation, indent=4, ensure_ascii=False)
    with open(f"textFiles/{fileName}.json", "w") as f:
        f.write(jsonFile)
    if ret:
        return jsonFile
    if not ret:
        pass
