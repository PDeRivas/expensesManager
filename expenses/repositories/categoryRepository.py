from .baseRepository import BaseRepository
from expenses.models import Category, CategoryIncome, CategoryExpense, Income, Expense
from typing import Optional, List
from accounts.models import CustomUser

# Define a custom exception for business logic failures
class InvalidCategoryTypeError(Exception):
    """Raised when a category type does not match the financial transaction type."""
    pass

class CategoryRepository(BaseRepository[Category]):
    def __init__(self):
        super().__init__(Category)

    def set_income_category(self, income: Income, category: Category):
        if category.categoryType == 'INCOME':
            return CategoryIncome.objects.create(income=Income, category=Category)
        else:
            raise InvalidCategoryTypeError(
                f"Cannot assign a '{category.categoryType}' category to an income transaction."
            )

    def set_expense_category(self, expense: Expense, category: Category):
        if category.categoryType == 'EXPENSE':
            return CategoryExpense.objects.create(expense=Expense, category=Category)
        else:
            raise InvalidCategoryTypeError(
                f"Cannot assign a '{category.categoryType}' category to an income transaction."
            )
