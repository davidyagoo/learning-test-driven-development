import operator
import functools
from select import select
from money import Money

class Portfolio:
  def __init__(self):
    self.moneys = []
  
  def add(self, *moneys):
    self.moneys.extend(moneys)
  
  def evaluate(self, currency):
    total = 0.0
    failures = []
    for m in self.moneys:
      try:
        total += self.__convert(m, currency)
      except KeyError as ke:
        failures.append(ke)
      except Exception as e:
        print(e)


    if len(failures) == 0:
      return Money(total, currency)

    failureMessage = ','.join(f.args[0] for f in failures)
    raise Exception(f'Missing exchange rate(s): [%s]' % failureMessage)

  def __convert(self, money, currency):
    exchange_rates = {
      'EUR->USD': 1.2,
      'USD->KRW': 1100,
    }

    key = '%s->%s' % (money.currency, currency)
    if money.currency == currency:
      return money.amount
    else:
      return money.amount * exchange_rates[key]
