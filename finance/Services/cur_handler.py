from finance.Services.cur_scrap import CurrencyScrapper


class CurrencyHandler(CurrencyScrapper):
    def __init__(self):
        super().__init__()

    def get_data(self, currency='usd'):
        parsedUsd = CurrencyScrapper.main(self, currency)
        return parsedUsd
