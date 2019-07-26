from django.urls import path
from .views import sellers, commissions, month_commission, vendedores, check_commission, create_user

urlpatterns = [
    path('sellers/', sellers),
    path('commissions/', commissions),
    path('month_commission/', month_commission),
    path('vendedores/<int:month>/', vendedores),
    path('check_commission/', check_commission),
    path('users/', create_user, name='create-user'),
]
