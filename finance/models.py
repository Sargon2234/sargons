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
    provider_id = models.ForeignKey(Providers, on_delete=models.CASCADE)
    currency_id = models.ForeignKey(Currencies, on_delete=models.CASCADE)
    sell = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField()
