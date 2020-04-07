from django.urls import path

from . import views

urlpatterns = [
    path('index/<pk>/', views.index, name='index'),
]

