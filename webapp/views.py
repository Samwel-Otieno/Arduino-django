from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import *
import serial
from django.http import HttpResponse
import xlwt
from datetime import datetime
from .models import Streamer

# Create your views here.
@login_required
def index(request):
    # if (request.method=='POST'):
    #     arduino_data= serial.Serial('com5',9600)
    #     while(True):
    #         if(arduino_data.in_waiting > 0):
    #             raw_data=arduino_data.readline()
    #             global samples
    #             samples=float(raw_data)
    #             print(samples)
    #             #save the data samples and the name of the person streaming the data
    #             streamed_data=Streamer(data_stream=samples,operator=request.user)
    #             streamed_data.save()   

    # render the data for display
    data=Streamer.objects.all()
    return render(request, 'webapp/index.html',{'data':data})

# Export the data into ana excel spreadsheet
def excelData(request):
    response=HttpResponse(content_type='application/ms-excel')
    # create content disposition and name the file
    response['Content-Disposition']='attachment; filename=data' + str(datetime.now())+ '.xls'
    # create a workbook 
    wb=xlwt.Workbook(encoding='utf-8')
    #create a worksheet
    ws=wb.add_sheet('Sensor data')
    # add row numbers (variable)
    row_num=0
    # add styling for the labels
    font_style=xlwt.XFStyle()
    font_style.font.bold=True # Set font size to bold

    #column labels
    columns=['Date','Sensor_value', 'Operator']

    # append the data into the columns and rows
    for colmn_num in range(len(columns)):
        ws.write(row_num, colmn_num,columns[colmn_num],font_style)

    # reset font style so that only the headers keep it
    font_style=xlwt.XFStyle()

    #create dynamic rows 
    rows=Streamer.objects.filter(operator=request.user).values_list('timestamp','data_stream', 'operator')
    for row in rows:
        row_num+=1

        for colmn_num in range(len(row)):
            ws.write(row_num, colmn_num, str(row[colmn_num]),font_style)
    #add worksheet to workbook
    wb.save(response)
    return response