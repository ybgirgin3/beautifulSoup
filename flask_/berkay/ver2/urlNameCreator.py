from urllib.parse import urlsplit

def fileNameCreate(url):
    name = urlsplit(url)[1]
    name = name.split(".")
    if name[0] == "www":
        return name[1]
    else:
        return name[0]
