from django.urls import path
from django.contrib import admin
from django.urls import path
from base import views
from .views import *




urlpatterns = [

    path('', views.indexpage, name='index'),
    path('ncr21/', views.Ncr21, name='ncr21'),
    path('ncr27/', views.Ncr27, name='ncr27'),
    path('ncr61/', views.Ncr61, name='ncr61'),
    path('ncr64/', views.Ncr64, name='ncr64'),
    path('ncrSE/', views.NcrSE, name='ncrSE'),


]