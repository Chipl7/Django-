from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # http://127.0.0.1:8000
    path('witchers_school/', views.categories),  # http://127.0.0.1:8000/witchers_school/
]