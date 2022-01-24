import os.path as op
import urllib.request
from datetime import date

from currency_converter import ECB_URL, CurrencyConverter

class conversion:
    global filename
    filename = f"ecb_{date.today():%Y%m%d}.zip"
    if not op.isfile(filename):
        urllib.request.urlretrieve(ECB_URL, filename)

    def __init__(self):
        pass

    def convert(self, amount, fromCurrency, toCurrency):
        global filename
        c = CurrencyConverter(filename)
        converted_amt = c.convert(amount,fromCurrency,toCurrency)
        return converted_amt

