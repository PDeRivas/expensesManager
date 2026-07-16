from datetime import date
from .baseRepository import BaseRepository
from expenses.models import Expense
from typing import Optional, List
from accounts.models import CustomUser

class ExpenseRepository(BaseRepository[Expense]):
    def __init__(self):
        super().__init__(Expense)
    
    def get_by_user(self, user: CustomUser) -> List[Expense]:
        return Expense.objects.filter(user=user)

    def setDate(self, expense: Expense,newDate: date) -> Expense:
        pass
