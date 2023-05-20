from django.urls import path
from . import views

app_name='useraccounts'

urlpatterns=[
    path('register/', views.Registerview, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),   
]