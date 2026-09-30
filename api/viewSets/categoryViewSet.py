from expenses.models import Category
from expenses.repositories.categoryRepository import CategoryRepository
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from api.serializers.expenseSerializer import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    repo = CategoryRepository()

    def get_queryset(self):
        return self.repo.get_all()
    
