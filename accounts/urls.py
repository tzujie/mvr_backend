from django.urls import path
from .views import register_account, login_account,list_accounts

urlpatterns = [
    path('api/register/', register_account, name='register'), 
    path('api/login/', login_account, name='login'),
    path('api/accounts/', list_accounts, name='account-list'),
]
