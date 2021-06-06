import serial
import time
#ser = serial.Serial('COM8', 9600)
ser = serial.Serial('COM8', 9600, timeout=0, parity=serial.PARITY_NONE,

                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
var1=''
var2=''
var3=''
var4=''
var5=''
while True:
    count =0
    nbytes = ser.inWaiting()
    x = str(ser.readline(nbytes))
    x = x.lstrip("b")
    x = x.strip("'")
    x = x.rstrip("\\r\\n")
    #print(x)
    y=x.split(',')
    for a in y[0:1]:
        var1=a
    for a in y[1:2]:
        var2=a
    for a in y[2:3]:
        var3=a
    for a in y[3:4]:
        var4=a
    for a in y[4:5]:
        var5=a
    print(var1,var2,var3,var4,var5)
    ser.flushInput()
    time.sleep(0.5)
ser.close()
