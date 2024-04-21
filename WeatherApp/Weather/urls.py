from django.urls import path
from . import views

urlpatterns = [
    path('information/', views.index, name='information'),
    path('home/', views.home, name='home' )
]