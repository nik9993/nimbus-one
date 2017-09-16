##################################################################
#                    Polling Server Thread                       #
##################################################################
#*****
#* Purpose: This is the polling server thread that will recieve
#*           all of the discovery packets from the clients
#*****
from clientthread import Client
import threading

threads = []

class PollingServer(threading.Thread):
    """This Thread is the Main Polling Thread of the Server"""
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.portNumber = port

    def run(self):
        try:
            print("Hello, World!")
			c = Client()
			c.start()
			threads.append(c)
			
        except KeyboardInterrupt:
            print ("^C received, shutting down the polling server")
