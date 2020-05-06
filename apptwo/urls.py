from django.urls import path
from apptwo import views

urlpatterns = [

    path('', views.help,name='help'),
    path('', views.index,name='index'),
]
