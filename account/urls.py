from django.urls import path

from account import views as account_views

app_name = 'account'

urlpatterns = [
    path('register/', account_views.SignUp.as_view(), name='create_user_account'),
]
