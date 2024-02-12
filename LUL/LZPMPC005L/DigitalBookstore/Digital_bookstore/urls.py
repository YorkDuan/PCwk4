from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='digitalbookstore-home'),
    path('about/', views.about,name='digitalbookstore-about'),
]