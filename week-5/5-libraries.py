#what are modules and libraries in python?
#Modules are files containing Python code. A module can define functions, classes, and variables.
#A library "Package" is a collection of modules that provide specific functionality.
#import: bu pythonda libraries import etmek icin kullanilir.

lists = ["adana","maraş","hatay"]

import random #tüm random library import edildi. Bunun sayesinde random içinde olan tüm fonskiyonları kullanabilirsin.
#random.choice() methodu ve diğerleri kullanılabilir.
coin = random.choice(["heads","tails"])# * random.choice() methodu verilen listeden rastgele 'bir' eleman seçer.
print(coin)

coin = random.choices(["heads","tails","muhammet"], k=2)
# * yukarıdaki kullanımda k=2 yazarak bana rastgele iki adet listeden eleman seç demiş olursun.
# * burada choices kullanımda k=2 yaptığın zaman aynı şeyleri seçebilir. ["heads", "heads"] gibi

coin = random.sample(["heads","tails","muhammet"], k=2)
# * yukarıda ise sample ile aynı iki elemanın gelmesini engelledik choices'dan farklı olarak


choice = random.choices(lists, weights=[100, 0, 0], k=2)
"""
weights sayesinde çıkma oranlarını değiştirebilirsin. Liste şeklinde oran vermen lazım liste eleman sayısı lists
ile aynı olmalı 0-100 arasında yüzde verirsin ve bu yüzdelerin toplamı 100 olmalı. yukarıda 0. indeks her zaman seçilecek.
"""

random.seed(0) #hep aynı sonucu gösterecek artık o sayıyı sabitledik
#bununla senin sistem saatine bağlı olarak değişen rastgelelikte hesaplamada kullanılan sayıyı ayarlayabilirsin.


#from: bu pythonda libraries import etmek icin kullanilir. from ile sadece belirli bir methodu import edebiliriz.
from random import choice #sadece choice methodunu import ettik. random yazmaya gerek yok.
coin = choice(["heads","tails"]) #random dan sadece choice import edildiği için başa random yazman gerekmiyor.
print(coin)


random_number = random.randint(1, 10) #random.randint() methodu verilen aralıkta rastgele bir sayı üretir.
print(random_number)


cards = random.shuffle([1, 2, 3, 4, 5]) #random.shuffle(list) methodu verilen listeyi rastgele karıştırır.
print(cards)


cards = ["Queen", "King", "Jack", "Ace"]
random.shuffle(cards) #random.shuffle(list) methodu verilen listeyi rastgele karıştırır
print(cards) #illa asingment yapmak zorunda değilsin. random.shuffle() methodu listeyi direkt olarak değiştirir.


import statistics #statistics library import edildi. statistics.mean() methodu ve diğerleri kullanılabilir.
grades = [90, 80, 70, 60, 50]
mean = statistics.mean(grades) #statistics.mean(list) methodu verilen listenin ortalamasını hesaplar.
print(mean)


import sys
print("hello, ",sys.argv[1]) #burada sys library argv modülü sayesinde cli'da python name.py Muhammet yazarsan
#1. indeks olan Muhammet kısmını alır 0. indes ise dosya adıdır


if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print(sys.argv[1])
#python name.py "Muhammet Çınkır" #burada "" içindeki iafdeyi listenin bir elemanı olarak alıgılayacak yani indeks 1


#burada sys.exit print yapar var cli'dan çıkış yapar ondan sonraki kod satırları işlenmez
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
print(sys.argv[1])


if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for name in sys.argv: #sys.argv içinde file name de var onu unutma
    print(name)


#Slices: subset of data structure bunun sayesinde listeyi sublistler haline getirebilirisin
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for name in sys.argv[1:]: #sys.argv içinde şimdi file name (0. index) yok slice yapmış oldun
    print(name)



#thirt party libraries pythonın popüler olmasında sebepler arasında (pypi.org adresiden erişebilirsin)
#cowsay:
#pip: package manager, install falan için usage: pip install cowsay. bunu yaptıktan sonra cowsay import edebilirsin

import cowsay
import sys
if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1]) #komik bir library
    cowsay.trex("hello, " + sys.argv[1]) #bunda ise trex basıyor


#requests: web request, internet request
#pip install request


#APIs or “application program interfaces” allow you to connect to the code of others.
#It turns out that Apple iTunes has its own API that you can access in your programs.
#In your internet browser, you can visit https://itunes.apple.com/search?entity=song&limit=1&term=weezer and a text file will be downloaded.
#David constructed this URL by reading Apple’s API documentation. Notice how this query is looking for a song, with a limit of one result, that relates to the term called weezer.
#Looking at this text file that is downloaded, you might find the format to be similar to that we’ve programmed previously in Python.
#sende olmayan bilgilere erişemeni sağlar başka yerde depolanmıştır api sayesinde oradan sen bilgiler alırsın
#istersen parametre vererek özelleştirme yapabilirsin

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
#yukarıda respons içinde json dosyası yok galiba içinde 200'lü bir şey olabilir
#argv[1] ksımında weezer yazıyor yani cli'da yazman lazım ne istediğini
print(response.json())
# * yukarıda .json() sayesinde jason haline çevirip erkana yazma yapabildin



import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2)) #indent 2 spaces anlamında
#Notice that json.dumps is implemented such that it utilizes indent to make the output more readable.



import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#limit 50 yapıldı fark ettiysen

content = response.json()
for result in content["results"]: #results valueları üzerinde harekt edilir burada
    print(result["trackName"]) #valuelardan key'i trackName olanları basar

response.raise_for_status() #used to automatically throw an exception if an HTTP request fails.




#STYLE:
# * PEP8 python için belirlenen bir style denilebilir


