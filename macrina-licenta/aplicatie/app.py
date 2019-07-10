from flask import Flask, render_template
from threading import Thread
import serial
from xbee import XBee
import time
import sys

app = Flask(__name__, static_url_path='/static')

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/SmartParking')
def SmartParking():
	return render_template('SmartParking.html')

parcare = [1,1,0,0,0]
@app.route('/Interface')
def Interface():
	global parcare
	return render_template('Interface.html' , parcare = parcare)

def read_serial():
	serial_port = serial.Serial('/dev/ttyUSB0', 9600)
	xbee = XBee(serial_port)
	global parcare
	while True:
		try:
			message = ( (xbee.wait_read_frame()))
			message = message['rf_data'].decode().rstrip()
			message = message[1:-1]
			message = message.split(',')
			print (message)
			sys.stdout.flush()
			parcare[0] = int(message[0])
			parcare[1] = int(message[1])
			parcare[2] = int(message[2])
			parcare[3] = int(message[3])
		except serial.serialutil.SerialException:
			print ("ERROR")
			sys.stdout.flush()
		time.sleep(0.01)

if __name__ == '__main__':
	thread_serial_read = Thread(target=read_serial, args=())
	thread_serial_read.daemon = True
	thread_serial_read.start()

	app.run(host='0.0.0.0')
