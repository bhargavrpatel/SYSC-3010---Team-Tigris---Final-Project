#pi@raspberrypi ~/Desktop/tigris-final-project $ cat gertv4.py 
import time
#from time import *
import RPi.GPIO as GPIO
from xmlrpc.server import SimpleXMLRPCServer


""" Constants """
myIP = "172.17.207.147"
myPORT = 8000


""" Function Implementations """
def hello():
	return "Hello, this is " + myIP

def initServer(ip, port):
	return SimpleXMLRPCServer((ip, port))

def getCounter():
	global counter
#	print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	print("[PETER] Counter was requested by a client. Sending " + str(counter) + " reseting counter to 0")
	temp = counter
	counter = 0 
	return temp

def incCounter(pin):
	global counter
	global time_stamp
	time_now = time.time()
	if ((time_now - time_stamp) >= .3):
		counter+=1
#		print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
		print("[PETER] Incremented counter to " + str(counter))
	time_stamp = time_now
	return True

""" Main """
def main():
	global time_stamp
	time_stamp = time.time()
	global server

	# Setup server
	server = initServer(myIP, myPORT)
	server.register_function(hello)
	server.register_function(getCounter)

	#Setup PORT interrupts
	GPIO.setmode(GPIO.BCM)            		      	 # initialise RPi.GPIO
	for i in range(23,26):                 			 # set up ports 23-25 
		GPIO.setup(i,GPIO.IN,pull_up_down=GPIO.PUD_UP) #as inputs pull$
		#time_stamp = time.time()
		GPIO.add_event_detect(i,GPIO.FALLING,bouncetime=500)		 #Detect Falling Edge
		GPIO.add_event_callback(i,incCounter)	 #Call Method if detected


if __name__=="__main__":
	# Declare and initialize global counter
	global counter
	counter = 0 

	#Declare global server instance
	global server

	# Run the main function when the file is executed
	main()

	# Tell the serve to serve indefinately
	print("Serving forever")
	server.serve_forever()

