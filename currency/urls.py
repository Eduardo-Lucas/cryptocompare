from django.urls import path

from currency import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prices/', views.prices, name='prices'),
    
]
