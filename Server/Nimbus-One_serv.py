#!/usr/bin/python3
#*****
#* @(#)Nimbus-One_serve.py
#*
#* Nimbus One Service Launcher
#* 2017(c)Copyright
#*
#* Contributors: 
#*   Allan "Nick" Pedrana
#*
#* @version 0.01 9/10/2017
#*  Alpha Realease Version
#*
#*****
#* Program History:
#*  -9/10/2017: File Created
#*
#*****
#*Coding Guidelines:
#* The PEP 8 Style Guide found here:
#*    https://www.python.org/dev/peps/pep-0008/
#*
#* Please Adhere to these guidelines while coding! It is very important that we conform to a convention.
#* If you have an issue with the guidelines then please bring it up and we might change them,
#* But for now Follow These Rules EVERYWHERE you Code!
#*
#* Naming Styles:
#* 1. GLOBAL_VARIABLES should be all caps and delimited with underscores, usually are constants
#* 2. local_variables should be all lowercase and delimited with underscores
#* 3. ClassNames should be CamelCase
#* 4. function_names should be in all lowercase delimited by an underscore
#* 5. ObjNames should be CamelCase and be an abbreviation of the Class it came from
#*      Example: 
#*         Class Name: PollingServer, Object Name: PollServ
#* 
#*
#* String Quotes:
#* 1. Single single quotes will be used for small symbol-like strings.
#* 2. Double double quotes will be used for string that are used for interpolation or that are natural language messages.
#* 3. Triple double quotes are for docstrings and raw string literals. 
#*****

import threading

PROG_NAME_V = "Nimbus One Server v0.01"
PROG_NAME   = "Nimbus One Server"


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

##################################################################
#                    Polling Server Thread                       #
##################################################################
#*****
#* Purpose: This is the polling server thread that will recieve
#*           all of the discovery packets from the clients
#*****

class PollingServer(threading.Thread):
    """This Thread is the Main Polling Thread of the Server"""
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.portNumber = port

    def run(self):
        try:
            print("Hello, World!")
        except KeyboardInterrupt:
            print ("^C received, shutting down the polling server")

##################################################################
#                     MAIN Program Flow                          #
##################################################################
#*****
#* Purpose: This is the main thread that will manage all of
#*           the threads on the server

#Starting Polling Server
PollServ = PollingServer(80)
PollServ.start()

