import socket
import json
from collections import OrderedDict

host = 'localhost' # 호스트 ip를 적어주세요
port = 6000            # 포트번호를 임의로 설정해주세요

server_sock = socket.socket(socket.AF_INET)
server_sock.bind((host, port))
server_sock.listen(1)

print("기다리는 중")
client_sock, addr = server_sock.accept()

print('Connected by', addr)
data = client_sock.recv(1024)
print(data, len(data))

#print(data2.encode())
data2 = OrderedDict()
data2["result"] = True
client_sock.send(json.dumps(data2).encode('UTF-8'))

client_sock.close()
server_sock.close()