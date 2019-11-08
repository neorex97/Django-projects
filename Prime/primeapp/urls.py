from django.urls import path

from primeapp import views

urlpatterns = [
    path('', views.index),
    path('eval/', views.getform, name='eval'),
]


