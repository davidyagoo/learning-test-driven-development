import unittest
from bank import Bank
from money import Money
from portfolio import Portfolio

class TestMoney(unittest.TestCase):

  def setUp(self):
    self.bank = Bank()
    self.bank.add_exchange_rate('EUR', 'USD', 1.2)
    self.bank.add_exchange_rate('USD', 'KRW', 1100)

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
    self.assertEqual(fifteenDollars, portfolio.evaluate(self.bank, 'USD'))

  def test_addition_of_dollars_and_euros(self):
    fiveDollars = Money(5, 'USD')
    tenEuros = Money(10, 'EUR')
    portfolio = Portfolio()
    portfolio.add(fiveDollars, tenEuros)
    expectedValue = Money(17, 'USD')
    actualValue = portfolio.evaluate(self.bank, 'USD')
    self.assertEqual(expectedValue, actualValue, '%s != %s' % (expectedValue, actualValue))

  def test_addition_of_dollars_and_wons(self):
    oneDollar = Money(1, 'USD')
    elevenHundredWons = Money(1100, 'KRW')
    portfolio = Portfolio()
    portfolio.add(oneDollar, elevenHundredWons)
    expectedValue = Money(2200, 'KRW')
    actualValue = portfolio.evaluate(self.bank, 'KRW')
    self.assertEqual(expectedValue, actualValue, '%s != %s' % (expectedValue, actualValue))

  def test_addition_with_multiple_missing_exchange_rates(self):
    oneDollar = Money(1, 'USD')
    oneEuro = Money(1, 'EUR')
    oneWon = Money(1, 'KRW')
    portfolio = Portfolio()
    portfolio.add(oneDollar, oneEuro, oneWon)
    with self.assertRaisesRegex(
      Exception,
      'Missing exchange rate\(s\): \[USD->Kalganid,EUR->Kalganid,KRW->Kalganid\]'
    ):
      portfolio.evaluate(self.bank, 'Kalganid')

  def test_conversion(self):
    bank = Bank()
    bank.add_exchange_rate('EUR', 'USD', 1.2)
    tenEuros = Money(10, 'EUR')
    expectedValue = Money(12, 'USD')
    actualValue = bank.convert(tenEuros, 'USD')
    self.assertEqual(actualValue, expectedValue, '%s != %s' % (expectedValue, actualValue))

  def test_conversion_with_missing_exchange_rate(self):
    bank = Bank()
    tenEuros = Money(10, 'EUR')
    with self.assertRaisesRegex(
      Exception,
      'EUR->Kalganid'
    ):
      bank.convert(tenEuros, 'Kalganid')

if __name__ == '__main__':
  unittest.main()