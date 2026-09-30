from expenses.models import Expense
from .categorySerializer import CategorySerializer
from rest_framework import serializers

class ExpenseSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'date', 'categories']