from django.conf import settings
from django.db import models

class Income(models.Model):
    amount = models.IntegerField(help_text='Amount of money added')
    date = models.DateField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='Incomes',
        null=True,
    )

class Expense(models.Model):
    amount = models.IntegerField(help_text='Amount of money spent')
    date = models.DateField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='Expenses',
        null=True,
    )
