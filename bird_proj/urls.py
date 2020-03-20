from django.urls import path

from . import views

urlpatterns = [
    path('index/<site_id>/', views.index, name='index'),
]

