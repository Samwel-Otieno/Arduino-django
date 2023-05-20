from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import serial
# Create your views here.
@login_required
def index(request):
    # arduino_data= serial.Serial('com4',9600)
    # while(True):
    #     if(arduino_data.in_waiting > 0):
    #         raw_data=arduino_data.readline()
    #         samples=float(raw_data)
    #         print(samples)
    #         streamed_data=Streamer(data_stream=samples)
    #         streamed_data.save()
    #         return HttpResponse(samples)     
        return render(request, 'webapp/index.html')