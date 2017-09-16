##################################################################
#                       Client Thread                            #
##################################################################
#*****
#* Purpose: This thread will be created everytime a new client
#*           send a discovery packet to the polling server
#*****
import threading

class Client(threading.Thread):
    """The Thread that initiates once a client connects to the server"""
    def __init__(self, conn, address):
        threading.Thread.__init__(self)
        self.client_conn = conn
        self.address = address
        self.connected = 1 
        self.running = 1
        self.size = 0
        
    def run(self):
        self.client_conn.setblocking(1) #Set Thread to blocking
        while running:
            if self.connected == 1:
                try:
                    data =  self.client_conn.recv(self.size);
#                   self.client_arg_parcer(data);
                except socket.herror:
                    self.client_conn.send("There has been an error recieving your data, please dissconnect and try again.\r\n");
                    print("There has been an error recieving your data, please dissconnect and try again.\r\n");
                    print("Error Code: " + str(errCode));
                    print("Message: " + str(Message) + "\r\n");
            else:
                if self.con == 1:
                    data = self.client_conn.recv(self.size);
#				self.client_arg_parcer(data);
				#else: must end thread here
				
            time.sleep(0.1);
