from django.urls import path
from . import views

urlpatterns = [
    path('user-data/', views.user_data, name='user-data'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('deposit/', views.deposit, name='deposit'),
    path('transfer/', views.transfer, name='transfer'),
    path('accept-transfer/', views.accept_transfer, name='accept-transfer'),
]
