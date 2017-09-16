##################################################################
#                       Client Thread                            #
##################################################################
#*****
#* Purpose: This thread will be created everytime a new client
#*           send a discovery packet to the polling server
#*****

class Client(threading.Thread):
    """The Thread that initiates once a client connects to the server"""
    def __init__(self, address):
        threading.Thread.__init__(self)
        self.address = address
    def run(self):
        print("Hello, Client!")
