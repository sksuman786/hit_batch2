from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('signup/',views.singup,name='signup'),
    path('login/',views.login,name='login'),
    
]
