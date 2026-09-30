from expenses.models import Income
from expenses.repositories.incomeRepository import IncomeRepository
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.serializers.incomeSerializer import IncomeSerializer

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all().order_by("id")
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]
    repo = IncomeRepository()

    def get_queryset(self):
        return self.repo.get_by_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
