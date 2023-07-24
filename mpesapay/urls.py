from django.urls import path
from .views import *

app_name='mpesapay'

urlpatterns=[
    path('mpesapay/', Mpesapay.as_view(),name='mpesa'),
]