from sys import argv
import currency
import exchange

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

        In default, amount is 1, selling currency is EUR and buying is PLN.
        """
            amount = 1

toSell = currency.Currency(sell)
toBuy = currency.Currency(buy)

exch = exchange.Exchange(str(amount), toSell, toBuy)

print exch.result
