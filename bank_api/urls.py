from django.urls import path
from . import views

urlpatterns = [
    path('withdraw/', views.withdraw, name='withdraw'),
    path('deposit/', views.deposit, name='deposit'),
    path('transfer/', views.transfer, name='transfer'),
]
