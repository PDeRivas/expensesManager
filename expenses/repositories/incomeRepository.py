from datetime import date
from .baseRepository import BaseRepository
from expenses.models import Income
from typing import Optional, List
from accounts.models import CustomUser

class IncomeRepository(BaseRepository[Income]):
    def __init__(self):
        super().__init__(Income)
    
    def get_by_user(self, user: CustomUser) -> List[Income]:
        return Income.objects.filter(user=user)

    def setDate(self, expense: Income,newDate: date) -> Income:
        pass
