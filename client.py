import socket
import time

HOST = 'localhost'  
PORT = 6000       

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

print('Connecting...')

while True:
    time.sleep(1)
    data = client_socket.recv(1024)
    print('Received data : ', data.decode("utf-8"))  

client_socket.close()