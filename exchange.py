import currency

class Exchange(object):
    """
    The class performs an exchange of two Currencies objects.

    Syntax:

        Exchange(<amount>, <Currency>, <Currency>)

        where:
            amount - of the money to sell
            Currency - Currency object to <sell>, <buy>
    """

    def __init__(self, amount, sell, buy):
        if isinstance(sell, currency.Currency) and isinstance(buy, currency.Currency):
            self.result = float(amount.replace(',','.'))*sell.rate*sell.multiply
            self.result = buy.multiply*self.result/buy.rate
        else:
            self.result = None
