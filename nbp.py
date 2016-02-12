from xml.dom import minidom
import urllib
from sys import argv

urlsource = urllib.urlopen('http://www.nbp.pl/kursy/xml/a001z160104.xml')
xmlsource = minidom.parse(urlsource)

nodes = xmlsource.getElementsByTagName('pozycja')

try:
    money = argv[1]
    code = argv[2]
    changeTo = argv[3]
except(IndexError):
    try:
        money = argv[1]
        code = argv[2]
        changeTo = 'PLN'

    except(IndexError):
        code = 'EUR'
        try:
            money = argv[1]
            print   u"""Blad skladni. Skrypt sluzy do przeliczania walut.

        Skladnia:

            nbp.py -ilosc -kod_waluty

            -ilosc_sprzedazy - ilosc pieniedzy do transakcji
            -kod_waluty_sprzedazy - trzyliterowy kod waluty sprzedawanej
            -kod_waluty_kupowanej - trzyliterowy kod waluty kupowanej

        Domyslnie, kiedy uzytkownik nie poda argumentow, przyjmowana jest
        wartosz 1 EUR PLN.
        Jesli podano tylko jeden argument, program przyjmuje ze jest to wartosc
        ilosc (X) i ostateczny wynik wyniesie X EUR.
        """
        except:
            money = 1

result = 0;

for ele in nodes:
    if code == ele.childNodes[5].firstChild.data:
        price = (ele.childNodes[7].firstChild.data).replace(',','.')
        money = money.replace(',','.')
        result = (float(price)*float(money))/(float(ele.childNodes[3].firstChild.data))

for ele in nodes:
    if changeTo == ele.childNodes[5].firstChild.data:
        result = float(ele.childNodes[3].firstChild.data)*result/float((ele.childNodes[7].firstChild.data).replace(',','.'))

print money, code, "=", result, changeTo
