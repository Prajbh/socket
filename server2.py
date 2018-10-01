# Socket programming - server side
import socket
import sys 
  
# import thread module 
from _thread import *
import threading
  
print_lock = threading.Lock()

clientList = {}

#define a thread
def threaded(a): 
    while True: 
  
        # server receives the data from client 
        data = a.recv(1024) 
        if not data: 
            print("Client " + str(clientList[a]) + " left" )
            break
  
        # reverse the given string from client 
        print("\nMessage recieved from client " + str(clientList[a]) + " - " + data.decode("utf-8"))
        data = data[::-1]
 
        # send the manipulated data to the client
        a.send(data) 
  
    # connection closed 
    a.close() 
  
  
def Main(): 
    host = "" 
    count = 1

   #Enter the port number to bind
    port = 22796
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    sock.bind((host, port)) 
    print("socket has binded to the port", port) 
  
    # socket listen upto 5 requests 
    sock.listen(5) 
    print("socket is listening") 


    while True: 
  
        # establishing connection with client 
        a, addr = sock.accept() 

        clientList[a] = count
        count = count + 1

        print('\nConnected to :', addr[0], ':', addr[1]) 
  
        # To start a new thread 
        start_new_thread(threaded, (a,)) 
    sock.close() 
  
  
if __name__ == '__main__': 
    Main()
 
