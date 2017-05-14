from django.core.management.base import BaseCommand
from finance.models import Providers
from finance.Services.cur_handler import CurrencyHandler
from django.db.utils import IntegrityError


class Command(BaseCommand, CurrencyHandler):
    def __init__(self):
        CurrencyHandler.__init__(self)

    def add_arguments(self, parser):
        parser.add_argument('--c', type=str)

    help = 'Adding new providers to model'

    def handle(self, *args, **options):
        currency = options['c']
        info = CurrencyHandler.get_data(self, currency)
        for bankName in info:
            try:
                newBank = Providers(provider=bankName)
                newBank.save()
                print('Successfully inserted new provider', bankName)
            except IntegrityError:
               print('Already has provider', bankName, 'NO INSERT')
