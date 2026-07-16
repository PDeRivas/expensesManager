from expenses.models import Income
from rest_framework import serializers

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'amount', 'date', 'user']
        read_only_fields = ['user'] 