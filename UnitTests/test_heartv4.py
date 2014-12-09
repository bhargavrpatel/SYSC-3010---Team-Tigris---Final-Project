import time
import random
import unittest
import warnings
import _thread as thread
import xmlrpc.client
import heartv4 as heart

class TestSequenceFunctions (unittest.TestCase):

	def setUp(self):	
		# Call the connect method
		# Run the testGert.py file as "sudo python3 boilerplateGERT.py 10000" and in another window... 
		#							  "sudo python3 boilerplateGERT.py 7600"
		self.Client = heart.connect(["127.0.0.1:10000","127.0.0.1:7600"])		

	def tearDown(self):
		print ("\n\nTear down mode\n\n")
		self.Client = []

	def test_connect(self):
		print ("\n\ntest_connect\n============================================")
		print ("Testing if the connection was made by checking the returned arrays\' first elements type")
		print ("type should be of class xmlrpc.client.ServerProxy")
		self.assertTrue(type(self.Client[0]) is xmlrpc.client.ServerProxy)

	def test_calculateMean(self):	
		print ("\n\ntest_calculateMean\n============================================")
		print ("Setting all devices\' count to 15 and calling calculate mean")
		print ("The return of calculate mean is assigned to variable mean")
		print ("assertEqual(mean,15)")
		expectedCount = 15
		
		for client in self.Client:
			client.setCounter(15)

		mean = heart.calculateMean(self.Client)		 # Calculate mean of the two connected devices

		# Check if we have 15 as we set both devices' counter to 15
		self.assertEqual(mean,15)

if __name__ == "__main__":
	unittest.main()