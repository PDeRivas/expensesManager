from .baseRepository import BaseRepository
from expenses.models import Category, CategoryIncome, CategoryExpense, Income, Expense
from typing import Optional, List
from accounts.models import CustomUser

class CategoryRepository(BaseRepository[Category]):
    def __init__(self):
        super().__init__(Category)

    def set_income_category(self, income: Income, category: Category):
        return CategoryIncome.objects.create(income=Income, category=Category)

    def set_expense_category(self, expense: Expense, category: Category):
        return CategoryExpense.objects.create(expense=Expense, category=Category)
