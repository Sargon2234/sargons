from django.core.management.base import BaseCommand
from finance.models import Providers, Currencies, CurrencyStatus
from finance.Services.cur_handler import CurrencyHandler
from django.db.utils import IntegrityError, DatabaseError
from datetime import datetime

class Command(BaseCommand, CurrencyHandler):
    def __init__(self):
        CurrencyHandler.__init__(self)

    help = 'Adding new currency info to model'

    def add_arguments(self, parser):
        parser.add_argument('--c', type=str)

    def handle(self, *args, **options):
        currency = options['c']
        info = CurrencyHandler.get_data(self, currency)
        for bankName, course in info.items():
            try:
                bank_id = Providers.objects.get(provider=bankName).id
                currency_id = Currencies.objects.get(currency=currency).id
                sell = course[1]
                buy = course[0]
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_info = CurrencyStatus(currency_id=currency_id, provider_id=bank_id, sell=sell, buy=buy, date=date)
                new_info.save()


            except (IntegrityError, DatabaseError) as error:
                print('Some error', error)
