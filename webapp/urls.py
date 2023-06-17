from django.urls import path
from . import views

app_name='webapp'

urlpatterns=[
    path('home/', views.index, name='home'), 
    path('excelData', views.excelData, name='excelData'),
    
]