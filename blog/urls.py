from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shopping-home'),
    path('about/',views.about, name='shopping-about'),
]