from django.contrib import admin
from django.urls import path, include
from cars import views

urlpatterns = [
    path('', views.predict, name='home'),
    path('hyper/', views.hyper, name='hyper'),
    path('result/', views.result, name='result'),
]