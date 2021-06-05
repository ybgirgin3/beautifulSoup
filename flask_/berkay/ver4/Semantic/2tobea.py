import spacy
import json
from collections import Counter
from termcolor import colored
import time


def SemanticFinder(word1, word2):

    ### 3 tane model var içlerinden bir tanesi seçilmelidir ###.

    # en hızlı model ama verimliliği çok düşük
    #nlp = spacy.load('en_core_web_sm')

    # orta hızdaki model verimlilik tatmin edici
    # kullanılması tavsiye edilen model
    nlp = spacy.load('en_core_web_md')

    # en yavaş model verimlilik mükemmel, (ek olarak pytorch kütüphanesini de indiriyor)
    # ama şöyle bir durumu var ara yüzdelik değerleri göstermiyor 
    # eğer benzerlik %100'den düşükse direk olarak sıfır kabul ediyor
    #nlp = spacy.load('en_core_web_trf')

    # convert the strings to spaCy Token objects
    token1 = nlp(word1)[0]
    token2 = nlp(word2)[0]


    # compute word similarity
    # accepted collector

    simil = token1.similarity(token2)  # returns 0.80168
    accepted = colored("X", "red")
    wordColor = 'yellow'
    if simil > 0.50:
        wordColor = 'green'
        accepted = colored("✓", 'green')

    #print(f"word1: {word1}, word2: {word2}, similarity: {simil}, accept ?: {accepted}")
    print("kelime1: {}, kelime2: {}, benzerlik: {}, kabul?: {}".format(colored(word1, wordColor), colored(word2, wordColor), colored(simil, wordColor), accepted))



def func(liste):
    # listelerdeki elemanların ilk 15 tanesini alma
    dict1 = liste[0]['freq'][15:]
    dict2 = liste[1]['freq'][15:]

    #print(f"dict1: {dict1}, dict2: {dict2}")

    counter1 = Counter(dict(dict1)).most_common(10)
    counter2 = Counter(dict(dict2)).most_common(10)


    #print(type(counter1)) # -> list dönüyor
    #print(counter1)

    # karakterler harf mi onu kontrol et
    # herhangi bir fazlaca kullanılmış olan noktalama işaretinin
    # algoritmayı yanıltmasını engellemek için liste elemanlarının
    # herbirinin alfabetik karakter olması gerekmektedir
    # aynı zamanda herhangi bir tek harflik bir eleman bulunmasına karşılık olarak
    # "a", "I" gibi elemanların herhangi bir benzerlik karşılığı olmayacağından dolayı
    # onları liste içinden atıyorum ve karşılaştırma seansına sokmuyorum.

    # yorum satırı halinde olan printleri tekrardan işleme koyarak yapılan işlemi görebilirsiniz.

    counter1 = [i[0] for i in counter1]
    counter1 = [i for i in counter1 if i.isalpha() and len(i) > 1]

    counter2 = [i[0] for i in counter2]
    counter2 = [i for i in counter2 if i.isalpha() and len(i) > 1]

    #counter1 = [i for i in counter1 if len(i) > 2]

    #print(counter1)
    #print(counter2)

    #print(counter1)
    #print(type(counter1))

    print(f"Birinci site içindeki kelime sayısı: {len(counter1)}")
    print(f"İkinci site içindeki kelime sayısı: {len(counter2)}")
    for i in counter1:
        for k in counter2:
            # aşağıdaki print satırının başındaki # işaretini kaldırdığınızdan karşılaştırılacak olan tüm kelimeleri görebilirsiniz
            #print(i, k)

            SemanticFinder(i, k)




# dosyayı oku
# freq kelimelerini al (most_common(10))
# iki dict'in kelimelerini kendi aralarında kontrol et
# yüzdesi %50 üzerinde olanı yazdır
import glob

# textFiles'in içindeki linkler.txt içine bak ordan sayıları al
read_files = glob.glob("../textFiles/*.json")
read_files = [i for i in read_files if i != '../textFiles/merged_file.json']
print(f"seçilen json dosyaları: {read_files}")

output_list = []

for f in read_files:
    with open(f, "r") as infile:
        output_list.append(json.load(infile))


#print(output_list[0]['freq'])
start = time.time()
ret = func(output_list)
end = time.time()
print(f"işlem süresi: {end - start} sn")










