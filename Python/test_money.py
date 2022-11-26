import operator
import functools
from select import select
import unittest

class Money:
  def __init__(self, amount, currency):
    self.amount = amount
    self.currency = currency

  def __eq__(self, other):
    return self.amount == other.amount and self.currency == other.currency
  
  def times(self, multiplier):
    return Money(self.amount * multiplier, self.currency)
  
  def divide(self, divisor):
    return Money(self.amount / divisor, self.currency)

class Money:
  def __init__(self, amount, currency):
    self.amount = amount
    self.currency = currency

  def __eq__(self, other):
    return self.amount == other.amount and self.currency == other.currency
  
  def times(self, multiplier):
    return Money(self.amount * multiplier, self.currency)
  
  def divide(self, divisor):
    return Money(self.amount / divisor, self.currency)

class Portfolio:
  def __init__(self):
    self.moneys = []
  
  def add(self, *moneys):
    self.moneys.extend(moneys)
  
  def evaluate(self, currency):
    total = functools.reduce(operator.add, map(lambda m: m.amount, self.moneys), 0)
    return Money(total, currency)


class TestMoney(unittest.TestCase):
  def test_multiplication_in_dollars(self):
    fiveDollars = Money(5, 'USD')
    tenDollars = Money(10, 'USD')
    self.assertEqual(tenDollars, fiveDollars.times(2))

  def test_multiplication_in_euros(self):
    tenEuros = Money(10, 'EUR')
    twentyEuros = Money(20, 'EUR')
    self.assertEqual(twentyEuros, tenEuros.times(2))

  def test_division(self):
    originalMoney = Money(4002, 'KRW')
    actualMoneyAfterDivision = originalMoney.divide(4)
    expectedMoneyAfterDivision = Money(1000.5, 'KRW')
    self.assertEqual(expectedMoneyAfterDivision, actualMoneyAfterDivision)

  def test_addition(self):
    fiveDollars = Money(5, 'USD')
    tenDollars = Money(10, 'USD')
    fifteenDollars = Money(15, 'USD')
    portfolio = Portfolio()
    portfolio.add(fiveDollars, tenDollars)
    self.assertEqual(fifteenDollars, portfolio.evaluate('USD'))

if __name__ == '__main__':
  unittest.main()