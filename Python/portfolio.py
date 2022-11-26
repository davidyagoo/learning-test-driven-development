import operator
import functools
from money import Money

class Portfolio:
  def __init__(self):
    self.moneys = []
    self.euro_to_usd = 1.2
  
  def add(self, *moneys):
    self.moneys.extend(moneys)
  
  def evaluate(self, currency):
    total = functools.reduce(operator.add, map(lambda m: self.__convert(m, currency), self.moneys), 0)
    return Money(total, currency)
  
  def __convert(self, money, currency):
    if money.currency == currency:
      return money.amount
    else:
      return money.amount * self.euro_to_usd
