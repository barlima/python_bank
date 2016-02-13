import urllib
import re

class Rates(object):
    """
    The class download most current rates from nbp.pl or selected date.

        Syntax:

            Rates(date) - date in format ddmmrrrr, dd.mm.rrrr, dd/mm/rrrr
                          or dd-mm-rrrr. In deafault the date is contemporary.
    """

    def __init__(self, date='today'):
        if date != 'today':
            self.__getDate(date)
        else:
            import datetime
            today = datetime.datetime.now()
            (self.day, self.month, self.year) = (today.day, today.month, today.year)

        self.__getMostCurrent()


    def __getDate(self, date):
        datePattern = re.compile(r'^(\d{1,2})\D+(\d{1,2})\D+(\d{4})$')
        (self.day, self.month, self.year) = datePattern.search(date).groups()
        #print self.day, self.month, self.year

    def __getMostCurrent(self):
        url = urllib.urlopen('http://www.nbp.pl/kursy/xml/dir.txt')
        url.read(3)

        for line in url:
            searchDate = int(self.year[2:4] + self.month + self.day)
            if re.search( r'^a\d{3}z(\d{2}\d{2}\d{2})', line):
                if searchDate >= int(line[5:]):
                    self.link = line

        url.close()
#
