# Bu araç @Hilas tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.altinkaynak.com/Doviz/Kur/Guncel")

source = BeautifulSoup(r.content, "html.parser")

ara1 = source.find("span", class_="title")
ara2 = source.find("span", class_="date")
ara3 = source.find("i", class_="time")

print(ara1.text, ara2.text, ara3.text, "", end="")
print("")
print("-" * 31, sep="")

bas = source.find("ul", class_="breadcrumbs").text
print(bas[:-21])

alSat = source.find("th", attrs={"id": "cphMain_cphSubContent_thBuy"})
satAl = source.find("th", attrs={"id": "cphMain_cphSubContent_thSell"})
print(" " * 22, alSat.text, "  ", satAl.text)
print(" " * 20, "-" * 7, "", "-" * 6)

dolar = source.find("tr", attrs={"data-flag": "USD"}).text
dolar1 = source.find("td", attrs={"id": "tdUSDBuy"}).text
dolar2 = source.find("td", attrs={"id": "tdUSDSell"}).text
print(dolar.replace("arrow", " " * 5)[:-14], dolar1[:6], "", dolar2[:])
print("-" * 36)

euro = source.find("tr", attrs={"data-flag": "EUR"}).text
euro1 = source.find("td", attrs={"id": "tdEURBuy"}).text
euro2 = source.find("td", attrs={"id": "tdEURSell"}).text
print(euro.replace("arrow", " " * 5)[:-17], euro1[:6], "", euro2[:])
print("-" * 36)

ifrank = source.find("tr", attrs={"data-flag": "CHF"}).text
ifrank1 = source.find("td", attrs={"id": "tdCHFBuy"}).text
ifrank2 = source.find("td", attrs={"id": "tdCHFSell"}).text
print(ifrank.replace("arrow", " " * 9)[:-17], ifrank1[:6], "", ifrank2[:])
print("-" * 36)

isterlin = source.find("tr", attrs={"data-flag": "GBP"}).text
isterlin1 = source.find("td", attrs={"id": "tdGBPBuy"}).text
isterlin2 = source.find("td", attrs={"id": "tdGBPSell"}).text
print(isterlin.replace("arrow", " " * 7)[:-17], isterlin1[:6], "", isterlin2[:])
print("-" * 36)

dkron = source.find("tr", attrs={"data-flag": "DKK"}).text
dkron1 = source.find("td", attrs={"id": "tdDKKBuy"}).text
dkron2 = source.find("td", attrs={"id": "tdDKKSell"}).text
print(dkron.replace("arrow", " " * 8)[:-17], dkron1[:6], "", dkron2[:])
print("-" * 36)

ikron = source.find("tr", attrs={"data-flag": "SEK"}).text
ikron1 = source.find("td", attrs={"id": "tdSEKBuy"}).text
ikron2 = source.find("td", attrs={"id": "tdSEKSell"}).text
print(ikron.replace("arrow", " " * 12)[:-17], ikron1[:6], "", ikron2[:])
print("-" * 36)

nkron = source.find("tr", attrs={"data-flag": "NOK"}).text
nkron1 = source.find("td", attrs={"id": "tdNOKBuy"}).text
nkron2 = source.find("td", attrs={"id": "tdNOKSell"}).text
print(nkron.replace("arrow", " " * 11)[:-17], nkron1[:6], "", nkron2[:])
print("-" * 36)

jyeni = source.find("tr", attrs={"data-flag": "JPY"}).text
jyeni1 = source.find("td", attrs={"id": "tdJPYBuy"}).text
jyeni2 = source.find("td", attrs={"id": "tdJPYSell"}).text
print(jyeni.replace("arrow", " " * 13)[:-17], jyeni1[:6], "", jyeni2[:])
print("-" * 36)

sriyal = source.find("tr", attrs={"data-flag": "SAR"}).text
sriyal1 = source.find("td", attrs={"id": "tdSARBuy"}).text
sriyal2 = source.find("td", attrs={"id": "tdSARSell"}).text
print(sriyal.replace("arrow", " " * 4)[:-17], sriyal1[:6], "", sriyal2[:])
print("-" * 36)

adolar = source.find("tr", attrs={"data-flag": "AUD"}).text
adolar1 = source.find("td", attrs={"id": "tdAUDBuy"}).text
adolar2 = source.find("td", attrs={"id": "tdAUDSell"}).text
print(adolar.replace("arrow", " " * 6)[:-17], adolar1[:6], "", adolar2[:])
print("-" * 36)

kdolar = source.find("tr", attrs={"data-flag": "CAD"}).text
kdolar1 = source.find("td", attrs={"id": "tdCADBuy"}).text
kdolar2 = source.find("td", attrs={"id": "tdCADSell"}).text
print(kdolar.replace("arrow", " " * 10)[:-17], kdolar1[:6], "", kdolar2[:])
print("-" * 36)

rruble = source.find("tr", attrs={"data-flag": "RUB"}).text
rruble1 = source.find("td", attrs={"id": "tdRUBBuy"}).text
rruble2 = source.find("td", attrs={"id": "tdRUBSell"}).text
print(rruble.replace("arrow", " " * 12)[:-17], rruble1[:6], "", rruble2[:])
print("-" * 36)

amanat = source.find("tr", attrs={"data-flag": "AZN"}).text
amanat1 = source.find("td", attrs={"id": "tdAZNBuy"}).text
amanat2 = source.find("td", attrs={"id": "tdAZNSell"}).text
print(amanat.replace("arrow", " " * 6)[:-17], amanat1[:6], "", amanat2[:])
print("-" * 36)

cyuan = source.find("tr", attrs={"data-flag": "CNY"}).text
cyuan1 = source.find("td", attrs={"id": "tdCNYBuy"}).text
cyuan2 = source.find("td", attrs={"id": "tdCNYSell"}).text
print(cyuan.replace("arrow", " " * 14)[:-17], cyuan1[:6], "", cyuan2[:])
print("-" * 36)

rleyi = source.find("tr", attrs={"data-flag": "RON"}).text
rleyi1 = source.find("td", attrs={"id": "tdRONBuy"}).text
rleyi2 = source.find("td", attrs={"id": "tdRONSell"}).text
print(rleyi.replace("arrow", " " * 11)[:-17], rleyi1[:6], "", rleyi2[:])
print("-" * 36)

baedirhem = source.find("tr", attrs={"data-flag": "AED"}).text
baedirhem1 = source.find("td", attrs={"id": "tdAEDBuy"}).text
baedirhem2 = source.find("td", attrs={"id": "tdAEDSell"}).text
print(baedirhem.replace("arrow", " " * 9)[:-17], baedirhem1[:6], "", baedirhem2[:])
print("-" * 36)

bleva = source.find("tr", attrs={"data-flag": "BGN"}).text
bleva1 = source.find("td", attrs={"id": "tdBGNBuy"}).text
bleva2 = source.find("td", attrs={"id": "tdBGNSell"}).text
print(bleva.replace("arrow", " " * 10)[:-17], bleva1[:6], "", bleva2[:])
print("-" * 36)

kdinar = source.find("tr", attrs={"data-flag": "KWD"}).text
kdinar1 = source.find("td", attrs={"id": "tdKWDBuy"}).text
kdinar2 = source.find("td", attrs={"id": "tdKWDSell"}).text
print(kdinar.replace("arrow", " " * 8)[:-17], kdinar1[:6], "", kdinar2[:6])
print("-" * 36)