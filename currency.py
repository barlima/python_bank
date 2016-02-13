from xml.dom import minidom
import urllib

class Currency(object):
    """
    A class representing a currency downloaded from npb.pl xml generated file.

    It contains attributes:

        Currency.name - currency's 3 letters abbreviation
        Currency.rate - exchange rate (related to PLN)
        Currency.multiply - default value is 1
    """

    def __init__(self, XXX):
        self.name = XXX.upper()
        if self.name != 'PLN':
            self.__getRate()
        else:
            self.rate = 1
            self.multiply = 1

    def __getRate(self):
        url = urllib.urlopen('http://www.nbp.pl/kursy/xml/a001z160104.xml')
        xml = minidom.parse(url)
        url.close()

        nodes = xml.getElementsByTagName('pozycja')

        for ele in nodes:
            if ele.childNodes[5].firstChild.data == self.name:
                self.rate = float((ele.childNodes[7].firstChild.data).replace(',','.'))
                self.multiply = int(ele.childNodes[3].firstChild.data)


        return (self.rate, self.multiply)
