# Socket programming - Client side program 
import socket 
import sys 
  
  
def Main(): 
    # setting host to local host and defining a port number
    host = '127.0.0.1'
    port = 22796
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connecting server to host
    sock.connect((host,port)) 
    print('\n Type quit to exit')
  
    while True: 
        # request message from client 
        print('\n Print message')
        message = input()
        if (message == 'quit'):
            sock.close()
            sys.exit()
  
        # the message is sent to the server 
        sock.send(message.encode('ascii')) 
  
        # server must receive the message 
        data = sock.recv(1024) 
  
        # print the reversed string received message  
        print('Message as received from the server :',str(data.decode('ascii'))) 

    # close the connection 
    sock.close() 
  
if __name__ == '__main__': 
    Main() 
