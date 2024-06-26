from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home, name='home'),
    path('balance/', views.balance, name='balance'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('deposit/', views.deposit, name='deposit'),
    path('transfer/', views.transfer, name='transfer'),
]
