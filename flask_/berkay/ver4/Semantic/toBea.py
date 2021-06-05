import spacy
import json
from collections import Counter
from termcolor import colored
import time


def SemanticFinder(word1, word2):
    # load the language model
    nlp = spacy.load('en_core_web_md')

    # convert the strings to spaCy Token objects
    token1 = nlp(word1)[0]
    token2 = nlp(word2)[0]


    # compute word similarity
    simil = token1.similarity(token2)  # returns 0.80168
    accepted = colored("X", "red")
    if simil > 0.50:
        accepted = colored("✓", 'green')

    print(f"word1: {word1}, word2: {word2}, similarity: {simil}, accept ?: {accepted}")



def func(liste):
    dict1 = liste[0]['freq'][15:]
    dict2 = liste[1]['freq'][15:]

    #print(f"dict1: {dict1}, dict2: {dict2}")


    counter1 = Counter(dict(dict1)).most_common(10)
    counter2 = Counter(dict(dict2)).most_common(10)
    
    #print(counter1)
    #print(type(counter1))
    print(f"word count of first list: {len(counter1)}")
    print(f"word count of second list: {len(counter2)}")
    for i, j in counter1:
        for k, v in counter2:
            SemanticFinder(i, k)


# dosyayı oku
# freq kelimelerini al (most_common(10))
# iki dict'in kelimelerini kendi aralarında kontrol et
# yüzdesi %70 üzerinde olanı yazdır
import glob
read_files = glob.glob("../textFiles/*.json")
read_files = [i for i in read_files if i != '../textFiles/merged_file.json']
print(f"seçilen json dosyaları: {read_files}")

for f in read_files:
    with open(f, "r") as infile:
        output_list.append(json.load(infile))




#print(output_list[0]['freq'])
start = time.time()
ret = func(output_list)
print(ret)
end = time.time()
print(end - start)

#print(ret)










