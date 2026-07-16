from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Sum
from expenses.models import Income, Expense

class BalanceViewSet(viewsets.ViewSet):

    def list(self, request):
        total_income = Income.objects.aggregate(total=Sum('amount'))['total'] or 0
        
        total_expense = Expense.objects.aggregate(total=Sum('amount'))['total'] or 0
        
        net_balance = total_income - total_expense

        return Response({
            'total_income': float(total_income),
            'total_expense': float(total_expense),
            'net_balance': float(net_balance)
        })
