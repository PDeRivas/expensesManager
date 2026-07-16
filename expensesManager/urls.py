"""
URL configuration for expensesManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.viewSets.incomeViewSet import IncomeViewSet
from api.viewSets.expenseViewSet import ExpenseViewSet
from api.viewSets.balanceViewSet import BalanceViewSet

from accounts.viewset import UserViewSet

router = routers.DefaultRouter()
router.register(r"/income", IncomeViewSet)
router.register(r"/expense", ExpenseViewSet)
router.register(r"/balance", BalanceViewSet, basename='balance')
router.register(r"/register", UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(router.urls)),
    path("register/", include("rest_framework.urls", namespace="rest_framework",)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
