import sys
import time
#from time import *
# import RPi.GPIO as GPIO
from xmlrpc.server import SimpleXMLRPCServer


""" Constants """
myIP = "127.0.0.1"
myPORT = int(sys.argv[1])


""" Function Implementations """
def hello():
        return "Hello, this is gert"

def getCounter():
        global counter
        temp = counter
        counter = 0
        return temp

def initServer(ip, port):
        return SimpleXMLRPCServer((ip, port))


def setCounter(count=5):
        global counter
        counter = count
        return True


""" Main """
def main():
        global server
        server = initServer(myIP, myPORT)
        server.register_function(hello)
        server.register_function(getCounter)
        server.register_function(setCounter)                    ## Added for Testing purposes



if __name__=="__main__":
        # Declare and initialize global counter
        global counter
        counter = 0 

        #Declare global server instance
        global server

        # Run the main function when the file is executed
        main()

        # Tell the serve to serve indefinately
        print("Serving forever at port: " + str (myPORT))


        global quit
        server.serve_forever()