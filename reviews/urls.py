from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('media/', views.media),
    path('all/', views.all),
    path('one/', views.one)
]