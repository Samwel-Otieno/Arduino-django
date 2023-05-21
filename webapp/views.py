from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *
import serial
# Create your views here.
@login_required
def index(request):
    if (request.method=='POST'):
        arduino_data= serial.Serial('com4',9600)
        while(True):
            if(arduino_data.in_waiting > 0):
                raw_data=arduino_data.readline()
                samples=float(raw_data)
                print(samples)
                #save the data samples and the name of the person streaming the data
                streamed_data=Streamer(data_stream=samples,operator=request.user)
                streamed_data.save()   
    return render(request, 'webapp/index.html')