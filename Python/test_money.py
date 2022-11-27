import unittest

from money import Money
from portfolio import Portfolio

class TestMoney(unittest.TestCase):

  def test_multiplication(self):
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

  def test_addition_of_dollars_and_euros(self):
    fiveDollars = Money(5, 'USD')
    tenEuros = Money(10, 'EUR')
    portfolio = Portfolio()
    portfolio.add(fiveDollars, tenEuros)
    expectedValue = Money(17, 'USD')
    actualValue = portfolio.evaluate('USD')
    self.assertEqual(expectedValue, actualValue, '%s != %s' % (expectedValue, actualValue))

  def test_addition_of_dollars_and_wons(self):
    oneDollar = Money(1, 'USD')
    elevenHundredWons = Money(1100, 'KRW')
    portfolio = Portfolio()
    portfolio.add(oneDollar, elevenHundredWons)
    expectedValue = Money(2200, 'KRW')
    actualValue = portfolio.evaluate('KRW')
    self.assertEqual(expectedValue, actualValue, '%s != %s' % (expectedValue, actualValue))

if __name__ == '__main__':
  unittest.main()