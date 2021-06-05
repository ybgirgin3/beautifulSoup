import json
from collections import Counter
def percBetween(dict1, dict2):
    # merged_file içindeki freq kısmındaki iki elemanı da oku
    #dict1 = liste[0]['freq']
    #dict2 = liste[1]['freq']

    
    # en çok kullanılan 10 elemanın içinde benzerlik ara
    counter1 = Counter(dict(dict1)).most_common(10)
    counter2 = Counter(dict(dict2)).most_common(10)

    # iki listede de en çok kullanılan ortak kelimelerin
    ret = len(set(counter1) & set(counter2)) / float(len(set(counter1) | set(counter2))) * 100
    d = dict()
    d['percBetween'] = ret
    return d

# herbir linkin ayrı oluşturulan json dosyalarını tek bir json dosyası haline getir
def mergeJsons():
    import glob
    read_files = glob.glob("textFiles/*.json")
    output_list = []

    for f in read_files:
        with open(f, "r") as infile:
            output_list.append(json.load(infile))

    #print(type(output_list[0]['freq']))
    toAdd = percBetween(output_list[0]['freq'], output_list[1]['freq'])
    #toAdd = percBetween(output_list)
    #print(toAdd)
    output_list.append(toAdd)


    with open("textFiles/merged_file.json", "w") as outfile:
        json.dump(output_list, outfile, ensure_ascii=False)

    def readJ():
        with open('textFiles/merged_file.json', 'r') as f:
            ret = f.read()
            data = json.loads(ret)
            return data


    return readJ()
