from django.urls import path
from . import views

urlpatterns = [
   path('',views.gohome, name='home'),
   path('cre/',views.getform,name='cre'),

]