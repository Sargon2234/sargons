from django.db import models

class Currencies(models.Model):
    currency = models.CharField(max_length=5)

    def __str__(self):
        return self.currency


class Providers(models.Model):
    provider = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.provider


class CurrencyStatus(models.Model):
    provider_id = models.IntegerField()
    currency_id = models.IntegerField()
    sell = models.DecimalField(max_digits=10, decimal_places=2)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
