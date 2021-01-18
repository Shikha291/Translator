from django.urls import path
from . import views

urlpatterns=[
    path('', views.translate, name='translate'),
    path('result/', views.result, name='result')
]