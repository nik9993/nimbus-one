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
        self.poll_sock = None;
        self.port_number = port
        self.host = ''

    def open_socket(self, sock):
        """Function called once a clients connects to the host on correct socket."""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.host, self.port_number))
            self.sock.listen(5)
            print("Polling Server Listening for connection...")
        except socket.error as err:
            if self.sock:
                self.poll.close()
            print("Could not open Server Socket because of error: " + str(err))
            print("Please try again")
            sys.exit(1)
        return

    def run(self):
        self.open_socket(self.poll_sock)
        try:
            while 1:
                conn = self.poll_sock.accept()
                c = Client(*conn)
                c.start()
                threads.append(c)
			
        except KeyboardInterrupt:
            print ("^C received, shutting down the polling server")
