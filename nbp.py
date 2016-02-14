from sys import argv
import currency
import exchange


try:
    date = argv[4]
except(IndexError):
    date = 'today'

try:
    amount = argv[1]
    sell = argv[2]
    buy = argv[3]
except(IndexError):

    try:
        buy = 'PLN'
        amount = argv[1]
        sell = argv[2]

    except(IndexError):
        sell = 'EUR'
        try:
            amount = argv[1]
        except:

            print   u"""
        Syntax error.

        Valid syntax:

            nbp.py <amount> <sell currency code> <buy currency code>

            <amount> - amount of money to sell (default 1)
            <sell currency code> - 3 letters abbreviation of currency to sell
            <buy currency code> - 3 letters abbreviation of currency to buy
            <date> - date, from which rates are being downloaded

        In default, amount is 1, selling currency is EUR, buying is PLN and
        date is contemporary
        """
            amount = 1

toSell = currency.Currency(sell, date)
toBuy = currency.Currency(buy, date)

exch = exchange.Exchange(str(amount), toSell, toBuy)

print ""
print "Based on nbp.pl rates published on: ", "".join((toSell.file[9:11], '.', toSell.file[7:9], '.', toSell.file[5:7]))
print ""
print str(amount), toSell.name, '=', exch.result, toBuy.name
