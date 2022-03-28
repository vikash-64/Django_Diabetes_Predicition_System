from django.contrib import admin
from django.urls import path 
from DiabitesApp import views

urlpatterns = [
    
    path('' , views.index , name = 'index'),
    path('predict' , views.predict , name = 'predict')
    
]