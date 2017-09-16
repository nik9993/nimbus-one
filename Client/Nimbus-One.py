#!/usr/bin/python3
#*****
#* @(#)Nimbus-One.py
#*
#* Nimbus One Client Program
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
from libs.common import *
import socket

PROG_NAME_V = "Nimbus One Client v0.01"
PROG_NAME   = "Nimbus One Client"
size = 4096
host = '127.0.0.1'
port = 5050
 
##################################################################
#                         MAIN Thread                            #
##################################################################
#*****
#* Purpose: This is the main program flow of the client
#*
#*****

         
client_socket = socket.socket()
client_socket.connect((host,port))
         
message = input(" -> ")
         
try:
    client_socket.send(message.encode())
    data = client_socket.recv(size).decode()
             
    print ('Received from server: ' + data)

except Exception as err: 
    print("Client socket fail due to error: " + str(err))
client_socket.close()
