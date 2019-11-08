from django.urls import path

from userapp import views

urlpatterns = [
    path('',views.home, name="home"),
    path('registration',views.reg,name="reg"),
    path('login/',views.login,name="log"),
]