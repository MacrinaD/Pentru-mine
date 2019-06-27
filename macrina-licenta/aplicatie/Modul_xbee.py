import serial
from xbee import XBee
import json

serial_port = serial.Serial('/dev/ttyUSB0', 9600)
xbee = XBee(serial_port)
print("json")
while True:
    try:
        message = ( (xbee.wait_read_frame()))
        print(message)

        f = open("data_out_file.out",'w')
        #f.write(message)
        json.dump(message,f)
        f.close()
    except KeyboardInterrupt:
        break

serial_port.close()
