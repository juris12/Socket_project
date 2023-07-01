import socket
PORT = 5002
import json
IP = '127.0.0.1'
class Response():
    def __init__(self):
        self._headers=[]
        self._status_code = 500
        self._mesage = ''
    def headers(self,headers):
        self._headers=headers
    def status(self,headers):
        self._status_code=headers
    def mesage(self,mesage):
        self._mesage=mesage
    def data(self) -> str:
        data = f'HTTP/1.1 {self._status_code}\r\n'
        data += f'{"; ".join(self._headers)}\r\n'
        data += '\r\n'
        data += self._mesage
        return data.encode()
class Server():
    def __init__(self) -> None:
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._host = None
        self._port = None
        self._router_list = []
        self._queue = None
        self._is_running = False


    def listen(self,ip,port,queue=5):
        if self._is_running:
            print('Server is alredy running')
        else:
            self._is_running = True
            self._host = ip
            self._port = port
            self._queue = queue
            self._server_socket.bind((self._host,self._port))
            self._server_socket.listen(self._queue)
            print(f'Server running on PORT: {port}')
            self._running_client()
            
        

    def route(self, path: str, func):
        self._router_list.append(func(path))
    
    def _running_client(self):
        for _ in range(5):
        # while True:
            try:
                client_socket, address = self._server_socket.accept()
                msg = client_socket.recv(1024).decode('utf-8')
                print('----------------------------------------')
                body = ''
                for i in msg.split('\n')[10:]:
                    body+=i.replace('\r','')
                body = json.loads(body)
                req={
                    'body': body,
                    'method':msg.split('\n')[0].split(' ')[0],
                    'path':msg.split('\n')[0].split(' ')[1]
                }
                print(req)
                print('----------------------------------------')
                for r in self._router_list:
                    if req['path'] == r._path: 
                        if r._methods[req['method']] != None:
                             r._methods[req['method']](client_socket,req)
                        else:
                            print(f'Method {req["method"]} is not defined for route {req["path"]}')
                client_socket.shutdown(socket.SHUT_WR)
            except KeyboardInterrupt:
                print('keybord interupt...')
            except Exception as exc:
                print('Error: ')
                print(exc)

    def stop_server(self):
        print('Server closed')
        if self._is_running:
            self._is_running = False
            self._server_socket.close()
            
        

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((IP,PORT))
# server.listen(5)
# for _ in range(5):
#     while True:
#         try:
#             client_socket, address = server.accept()
#             msg = client_socket.recv(1024).decode('utf-8')
#             pieces = msg.split('\n')
#             print('----------------------------------------')
#             req = msg.split('\n')[0].split(' ')[:2]
#             print(req)
#             print('----------------------------------------')
#             data = 'HTTP/1.1 200 OK\r\n'
#             data += 'Content-Type: text/html; charset=utf-8\r\n'
#             data += '\r\n'
#             data += '<html><body><h1>Hello World!!!!</h1></body></html>'
#             client_socket.sendall(data.encode())
#             client_socket.shutdown(socket.SHUT_WR)
#         except KeyboardInterrupt:
#             print('keybord interupt...')
#         except Exception as exc:
#             print('Error: ')
#             print(exc)
        
#         break
# server.close()
