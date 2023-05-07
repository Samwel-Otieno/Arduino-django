from django.urls import path
from . import views

app_name='webapp'

urlpatterns=[
    path('index/', views.index, name='index'),  
    
]