from datetime import date
from django.conf import settings
from django.db import models

class Income(models.Model):
    amount = models.IntegerField(help_text='Amount of money added')
    date = models.DateField(default=date.today)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='Incomes',
        null=True,
    )

class Expense(models.Model):
    amount = models.IntegerField(help_text='Amount of money spent')
    date = models.DateField(default=date.today)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='Expenses',
        null=True,
    )

class Category(models.Model):
    name = models.TextField(help_text='Category name')

class CategoryIncome(models.Model):
    income = models.ForeignKey(
        to=Income,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
    )

class CategoryExpense(models.Model):
    expense = models.ForeignKey(
        to=Expense,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
    )
