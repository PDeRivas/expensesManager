from expenses.models import Expense
from expenses.repositories.expenseRepository import ExpenseRepository
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.serializers.expenseSerializer import ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by("date")
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    repo = ExpenseRepository()

    def get_queryset(self):
        return self.repo.get_by_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
