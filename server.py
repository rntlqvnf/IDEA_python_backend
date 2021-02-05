from socket import *
from select import *

HOST = 'localhost'
PORT = 6000
BUFSIZE = 1024
ADDR = (HOST, PORT)

# 소켓 생성
serverSocket = socket(AF_INET, SOCK_STREAM)

# 소켓 주소 정보 할당
serverSocket.bind(ADDR)
print('bind')

# 연결 수신 대기 상태
serverSocket.listen(100)
print('listen')

# 연결 수락
clientSocket, addr_info = serverSocket.accept()
print('accept')
print('--client information--')
print(clientSocket)

# 클라이언트로부터 메시지를 가져옴
while True:
    data = clientSocket.recv(65535)
    print('receive data : ',data.decode("utf-8"))
    msg = data.decode("utf-8")
    if msg == 'exit': # exit라는 메세지를 받으면 종료
        break;

# 소켓 종료
clientSocket.close()
serverSocket.close()
print('close')