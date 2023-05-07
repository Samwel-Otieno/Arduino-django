import serial

data=[]
arduino_data= serial.Serial('com4',9600)
while True:
    def stream():
        if(arduino_data.in_waiting > 0):
            raw_data=arduino_data.readline()
            samples=float(raw_data)
            data.append(samples)           
        return data
