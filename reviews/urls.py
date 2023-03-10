from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index, name='reviews-home'),
    path('media/', views.media, name='reviews-media'),
    path('all/', views.all, name='reviews-all'),
    path('one/', views.one, name='reviews-one'),
]