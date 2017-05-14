from django.contrib import admin
from finance.models import Currencies, Providers, CurrencyStatus

admin.site.register(Currencies)
admin.site.register(Providers)
admin.site.register(CurrencyStatus)