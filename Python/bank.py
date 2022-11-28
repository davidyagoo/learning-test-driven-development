from money import Money

class Bank:
  def __init__(self):
    self.exchange_rates = {}
  
  def add_exchange_rate(self, fromCurrency, toCurrency, rate):
    key = '%s->%s' % (fromCurrency, toCurrency)
    self.exchange_rates[key] = rate

  def convert(self, money, currency):
    if money.currency == currency:
      return Money(money.amount, money.currency)

    key = '%s->%s' % (money.currency, currency)
    if key in self.exchange_rates:
      return Money(money.amount * self.exchange_rates[key], currency)
    raise Exception(key)
