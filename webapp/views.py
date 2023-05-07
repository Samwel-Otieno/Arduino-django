from django.shortcuts import render
from . functions import *
from .models import Streamer
# Create your views here.

def index(request):
    stream()
    for samples in data:
        streamed_data=Streamer(data_stream=samples)
        print(streamed_data)
        streamed_data.save()
    return render(request, 'webapp/index.html')