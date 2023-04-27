import random
import urllib.request

names = []


def download_jpg(url):
    name_number = random.randrange(1, 100)
    name = str(name_number) + ".jpg"
    for f in names:
        if f == name:
            name = str(name_number) + name
    urllib.request.urlretrieve(url, name)
    names.append(name)


for i in range(1, 100):
    try:
        download_jpg("https://ukrlib.com.ua/my/images/full/sent-ekziuperi-antuan-de---malenkyy-prynt_30.jpg")
        print(names)
    except:
        print("Find another picture, please!")

