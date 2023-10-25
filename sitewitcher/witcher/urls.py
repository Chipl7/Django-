from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index),  # http://127.0.0.1:8000
    path('witchers_school/<int:witcher_school_id>/', views.categories),  # http://127.0.0.1:8000/witchers_school/2/
    path('witchers_school/<slug:witcher_school_slug>/', views.categories_by_slug),  # http://127.0.0.1:8000/witchers_school/asdqwe/
    path('archive/<year4:year>/', views.archive)
]
