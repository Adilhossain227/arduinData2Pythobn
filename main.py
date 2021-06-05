import serial
import time
#ser = serial.Serial('COM8', 9600)
ser = serial.Serial('COM8', 9600, timeout=0, parity=serial.PARITY_NONE,

                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
Y='LOADING'
while True:
    nbytes = ser.inWaiting()
    x = str(ser.readline(nbytes))
    x = x.lstrip("b")
    x = x.strip("'")
    x = x.rstrip("\\r\\n")
    #print(x)        #to print what python has received
    y=x.split(',') # to split the received string into , delimeter separated array
    print(y[0]) # print the first char in array as value
    ser.flushInput()
    time.sleep(0.6)
ser.close()
