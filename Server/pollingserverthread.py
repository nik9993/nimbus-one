##################################################################
#                    Polling Server Thread                       #
##################################################################
#*****
#* Purpose: This is the polling server thread that will recieve
#*           all of the discovery packets from the clients
#*****
from clientthread import Client
from libs.common import *
import threading
import socket

threads = []

class PollingServer(threading.Thread):
    """This Thread is the Main Polling Thread of the Server"""
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port_number = port
        self.host = 'localhost'

    def open_socket(self):
        """Function called once a clients connects to the host on correct socket."""
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Binding host: " + self.host + " Port: " + str(self.port_number))
            self.server.bind((self.host, self.port_number))
            self.server.listen(5)
            print("Polling Server Listening for connection...")
        except socket.error as err:
            if self.server:
                self.server.close()
            print("Could not open Server Socket because of error: " + str(err))
            print("Please try again")
            sys.exit(1)
            return

    def run(self):
        poll_sock = self.open_socket()
        poll_sock.bind((host, port_number))
    
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
