from django.urls import path
from . import views

urlpatterns =[
    path('/', views.testing),
    path('', views.homepage)
]