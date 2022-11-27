import operator
import functools
from money import Money

class Portfolio:
  def __init__(self):
    self.moneys = []
  
  def add(self, *moneys):
    self.moneys.extend(moneys)
  
  def evaluate(self, currency):
    total = functools.reduce(operator.add, map(lambda m: self.__convert(m, currency), self.moneys), 0)
    return Money(total, currency)
  
  def __convert(self, money, currency):
    exchange_rates = {
      'EUR->USD': 1.2,
      'USD->KRW': 1100,
    }

    key = '%s->%s' % (money.currency, currency)
    if money.currency == currency:
      return money.amount
    else:
      return money.amount * exchange_rates.get(key)
