from flask import Flask, render_template, request
from URL_Parser import parser
import time
import json
import os

app = Flask(__name__)


# ikinci link için url1 sayfasında bir tane daha buton oluştur sonra ona basılınca diğer aşamalara geçsin
# linkleri yaz ve sonra oku

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/asama1', methods = ['POST', 'GET'])
def asama1():
    if request.method == 'POST':
        for i in os.listdir("textFiles"):
            filen = "textFiles/{}".format(i)
            os.remove(filen)
      #result = parser(request.form["url1"])
        url1 = request.form.get("url1")
        url2 = request.form.get("url2")
        # urlleri dosyaya yaz
        readandWrite(url1, url2, file_ = "linkler", R = False)
        time.sleep(1)
        firstUrl = readandWrite(file_ = "linkler", R=True)[0]

        # send url and create json file
        processed_value = parser(firstUrl, ret=True)
        processed_value = json.loads(processed_value)

    return render_template("asama1.html", result = processed_value)


@app.route('/asama23', methods = ['POST', 'GET'])
def asama23():
    if request.method == "POST":
        for i in os.listdir("textFiles"):
            if i.startswith("url"):
                filen = "textFiles/{}".format(i)
                os.remove(filen)

        ikinciUrl = readandWrite(file_ = "linkler", R=True)[1]
        parser(ikinciUrl, ret=False)
        processed_value = mergeJsons()



    return render_template("asama23.html", result = processed_value)

def mergeJsons():
    import glob
    read_files = glob.glob("textFiles/*.json")
    output_list = []

    for f in read_files:
        with open(f, "r") as infile:
            output_list.append(json.load(infile))

    with open("textFiles/merged_file.json", "w") as outfile:
        json.dump(output_list, outfile, ensure_ascii=False)

    def readJ():
        with open('textFiles/merged_file.json', 'r') as f:
            ret = f.read()
            data = json.loads(ret)
            return data


    return readJ()


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


if __name__ == '__main__':
   app.run(debug = True)
