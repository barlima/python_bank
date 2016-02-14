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
        if re.search(r'(\d{1,2})\D+(\d{1,2})\D+(\d{4})', date):
            self.__getDate(date)
        else:
            import datetime
            today = datetime.datetime.now()
            (self.day, self.month, self.year) = (today.day, today.month, today.year)
            if int(self.day) < 10:
                self.day = "".join(('0', str(self.month)))
            if int(self.month) < 10:
                self.month = "".join(('0', str(self.month)))

        self.__getMostCurrent()


    def __getDate(self, date):
        datePattern = re.compile(r'(\d{1,2})\D+(\d{1,2})\D+(\d{4})')
        try:
            (self.day, self.month, self.year) = datePattern.match(date).groups()

        except(AttributeError):
            print "Wrong date format"

    def __getMostCurrent(self):
        url = urllib.urlopen('http://www.nbp.pl/kursy/xml/dir.txt')
        url.read(3)

        for line in url:
            searchDate = int(str(self.year)[2:4] + str(self.month) + str(self.day))
            if re.search( r'^a\d{3}z(\d{2}\d{2}\d{2})', line):
                if searchDate >= int(line[5:]):
                    self.link = str(line[0:11])

        url.close()
#
