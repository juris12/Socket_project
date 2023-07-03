import socket
import re
import json
PORT = 5002
import json
IP = '127.0.0.1'
class Response():
    """Creates response objekt
    """
    def __init__(self,client_socket):
        self._headers=[]
        self._status_code = 500
        self._mesage = ''
        self._client_socket = client_socket
    def headers(self,headers):
        self._headers=headers
    def status(self,headers):
        self._status_code=headers
    def json(self,db):
        self._mesage = json.dumps([{
            'name':x.name,
            'pwd_hash':x.pwd_hash,
            'status':x.status,
            'ip':x.ip
        } for x in db])
    def mesage(self,mesage):
        self._mesage=mesage
    def html(self,path):
        with open(path) as f:
            self._mesage = f.read() 
    def send(self):
        data = f'HTTP/1.1 {self._status_code}\r\n'
        data += f'{"; ".join(self._headers)}\r\n'
        data += '\r\n'
        data += self._mesage
        self._client_socket.sendall(data.encode())
    def send_html(self,path):
        try:
            with open(path) as f:
                self._mesage = f.read()
                self.send()
        except FileNotFoundError:
            data = f'HTTP/1.1 404\r\n'
            data += '\r\n'
            data += f'file: {path} not found!'
            self._client_socket.sendall(data.encode())
    def send_img(self,path):
        try:
            
            with open('files/favicon.png', 'rb') as f:
                img = f.read()
                
                # response = (
                # "HTTP/1.1 200 OK\r\n"
                # "Content-Type: image/png\r\n"
                # f"Content-Length: {format(len(img))}\r\n\r\n"
                # f'{str(img)}'
                # )
                data = f'HTTP/1.1 200\r\n'
                data += '\r\n'
                data += f'img: {path} send!'
                self._client_socket.sendall(data.encode())
        except FileNotFoundError:
            data = f'HTTP/1.1 404\r\n'
            data += '\r\n'
            data += f'img: {path} not found!'
            self._client_socket.sendall(data.encode())
class Request():
    def __init__(self,msg,params):
        bodyparse = ''
        body = msg.split('\r\n\r\n')
        if len(body) >= 2:
            for i in body[1].split('\n'):
                bodyparse+=i.replace('\r','')
            bodyparse = json.loads(bodyparse)
        else:
            bodyparse = None
        absolute_path = re.search(r"^(/[\w,/]*)(?:/([\w,\.]*))?$",msg.split('\n')[0].split(' ')[1])
        self._path = absolute_path.group(1)
        self._params = None
        if params:
            self._params = absolute_path.group(2)
        self._body = body
        self._mathod = msg.split('\n')[0].split(' ')[0]
    @property
    def params(self):
        return self._params
    @property
    def body(self):
        return self._body
    @property
    def method(self):
        return self._mathod
    @property
    def path(self):
        return self._path
    
class Server():
    """Initializes class instance
    """
    def __init__(self) -> None:
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._host = None
        self._port = None
        self._router_list = []
        self._queue = None
        self._is_running = False


    def listen(self,ip,port,queue=5):
        """Starts server
            
            Parameters:
        
            ip: str
                ip address
            port: int
                port you are using 
            queue: int
                number of alowed clients in queue befor cutting of new clients
        """
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
        """Adds route to server
        """
        self._router_list.append(func(path))
    
    def _running_client(self):
        for _ in range(10):
        # while True:
            try:
                client_socket, address = self._server_socket.accept()
                msg = client_socket.recv(1024).decode('utf-8')
                print(msg)
                for r in self._router_list:
                    absolute_path = re.search(r"^(/[\w,/]*)(?:/:(\w*))?$",r._path)
                    params = absolute_path.group(2)
                    path = absolute_path.group(1)
                    req = Request(msg,params)
                    if req.path == path: 
                        print('----------------------------------------')
                        print(req._mathod,req._path,req._params,req._body)
                        print('----------------------------------------')
                        if r._methods[req.method] != None:
                            res = Response(client_socket)
                            r._methods[req.method](res,req)
                        else:
                            print(f'Method {req.method} is not defined for route {req.path}')
                client_socket.shutdown(socket.SHUT_WR)
            except KeyboardInterrupt:
                print('keybord interupt...')
            except Exception as exc:
                print('Error: ')
                print(exc)
                client_socket.shutdown(socket.SHUT_WR)

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
