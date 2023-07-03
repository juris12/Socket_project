import socket
from gui import *


IP = '127.0.0.1'
PORT = 5000

class Client():
    def __init__(self) -> None:
        ...
    def get_all(self):
        try:
            client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_socket.connect((IP,PORT))
            client_socket.send("GET / HTTP/1.1\r\n".encode())
            response = b""
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                response += data
            response = response.decode()
            client_socket.shutdown(socket.SHUT_WR)
            if len(response.split('\r\n\r\n')) >= 2:
                return json.loads(response.split('\r\n\r\n')[1])
            else:
                return None
        except ConnectionRefusedError as err:
            print(err)
# client = Client()



ui = Ui()

print(ui.get_regester_or_login())



