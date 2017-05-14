from cur_scrap import CurrencyScrapper
from finance.models import Providers


class CurrencyHandler(CurrencyScrapper):
    def process(self):
        data = self.get_data()
        self.insertData(data, True)

    def get_data(self):
        parsedUsd = CurrencyScrapper.main(self, 'usd')
        return parsedUsd

    def insertData(self, data, providers=False):
        if providers:
            for provider in data:
                newProviders = Providers(provider=provider)
                newProviders.save()


a = CurrencyHandler()
a.process()
