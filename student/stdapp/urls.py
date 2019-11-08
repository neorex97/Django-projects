from django.urls import path

from stdapp import views

urlpatterns = [
    path('',views.home,),
    path('reg',views.reg,name="reg")
]