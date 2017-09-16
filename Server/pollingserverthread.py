##################################################################
#                    Polling Server Thread                       #
##################################################################
#*****
#* Purpose: This is the polling server thread that will recieve
#*           all of the discovery packets from the clients
#*****
from clientthread import Client
import threading
import socket

threads = []

class PollingServer(threading.Thread):
    """This Thread is the Main Polling Thread of the Server"""
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.portNumber = port
    
    def open_socket(self):
        """Function called once a clients connects to the host on correct socket."""
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
            print("Polling Server Listening for connection...")
        except socket.error:# as (value, message):
            if self.server:
                self.server.close()
            print("Could not open Server Socket: " + message)
            print("Please try again")
            sys.exit(1)
            return

    def run(self):
        poll_sock = self.open_socket()
        poll_sock.bind((host, port))
    
        poll_sock.listen(1)
        try:
            print("Hello, World!")
            while 1:
                conn = poll_sock.server.accept()
                c = Client(*conn)
                c.start()
                threads.append(c)
			
        except KeyboardInterrupt:
            print ("^C received, shutting down the polling server")
