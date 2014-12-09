import time
import xmlrpc.client
from twython import Twython

""" Constants """
DEBUG = False
INTERVAL = 10               # Tweet traffic at every 10 minute intervals
HILIMIT = 50                # Mean of traffic is checked against these two flags
MEDLIMIT = 25

""" API RELATED STUFF (IGNORE) """
APP_KEY = "S2gnMCA3Eq1Eo8HXVQKUI7FdO"
APP_SECRET = "TS2nLdBBEOiOJZT9W3L9QlyE3wifbq1qVUMZWChKoUioQlHeUu"
OAUTH_TOKEN = "2834393687-bD2hzsHBiE02eHqHeVfGfWX2LGvq1ngqezZphIS"
OAUTH_TOKEN_SECRET = "CKwRlGSRn35X5pzGbh8MRojrKtlT7OLUvDFoKTdPFp8wu"


# List of all devices along with their listening ports
servers = ["127.0.0.1:10000"]							# Change these to IPs of Gertboard Pis in the Discovery Center.

# Connects to all servers listed in the given array
def connect(list, DEBUG=False):
	result = []
	for l in list:
		result.append(xmlrpc.client.ServerProxy('http://'+l))
		if DEBUG is True: print ("Added " + l + " to list of devices")
	return result

# Calls the hello() method on each server from the list if oneOnly is false
# Calls the hello() method on given index from the list if oneOnly is true
def introduce(list, oneOnly=False, index=0):
	if (oneOnly):
		print ("Will call hello on device #" + str(index))
		print(list[index].hello())
	else: 
		print ("Will call hello method on all connected devices")
		for l in list: 
			print(l.hello())

# Calculates and returns the mean of given list
# Calls getCounter() on all devices, keeps a running sum and returns the mean
def calculateMean(list):
	sum = 0
	for l in list:
		sum += l.getCounter()
	return (sum / len(list))


# Sends the appropriate tweet message
def sendTweet(mean, twythonInstance, high=50, medium=25):
	string = ""
	timeStamp = str(time.ctime(int(time.time())))
	if mean > high:
		print ("Calculated : HIGH " + timeStamp)
		string = "HIGH " + timeStamp
	elif medium > mean > high:
		print ("Calculated : AVERAGE " + timeStamp)
		string = "AVERAGE " + timeStamp
	else:
		print ("Calculated : LOW " + timeStamp)
		string = "LOW " + timeStamp

	try:
		twythonInstance.update_status(status = string)
	except TwythonAuthError:
		print ("Could not send a tweet, got authentication error, check the OAuth keys")
	except TwythonError:
		print ("Could not send a tweet duplicate tweet! Cannot get around this by just timestamp sometimes")



if __name__ == "__main__":

	result = connect(servers)
	try: 
		twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	except TwythonAuthError:
		print ("Could not send a tweet, got authentication error, check the OAuth keys")
		print ("Exiting program, restart after fixing OAuth key")
		sys.exit(1)

	while (True):
		print ("Next set of data will be collected in " + str(INTERVAL * 60) + " seconds from " + str(len(result)) + " sources")
		time.sleep(INTERVAL * 60)
		print ("Determining traffic conditions now...")
		mean = calculateMean(result)
		print ("Average amount of people passing from tunnel: " + str(mean))
		sendTweet (mean, twitter, HILIMIT, MEDLIMIT)