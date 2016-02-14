from xml.dom import minidom
import urllib
import rates

class Currency(object):
    """
    A class representing a currency downloaded from npb.pl xml generated file.

    It contains attributes:

        Currency.name - currency's 3 letters abbreviation
        Currency.rate - exchange rate (related to PLN)
        Currency.multiply - default value is 1
    """

    def __init__(self, XXX, date):
        self.name = XXX.upper()
        self.path = date
        if self.name != 'PLN':
            self.__getRate()
        else:
            self.rate = 1
            self.multiply = 1

    def __getRate(self):
        ratesDate = rates.Rates(self.path)
        try:
            self.file =  ratesDate.link
            link = "".join(('http://www.nbp.pl/kursy/xml/', ratesDate.link, '.xml'))
        except(AttributeError):
            print 'Something went wrong, please contact the master'
            link = 'http://www.nbp.pl/kursy/xml/a001z160104.xml'

        url = urllib.urlopen(link)
        xml = minidom.parse(url)
        url.close()

        nodes = xml.getElementsByTagName('pozycja')

        for ele in nodes:
            if ele.childNodes[5].firstChild.data == self.name:
                self.rate = float((ele.childNodes[7].firstChild.data).replace(',','.'))
                self.multiply = int(ele.childNodes[3].firstChild.data)


        return (self.rate, self.multiply)
