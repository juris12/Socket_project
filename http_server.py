import socket
from routes import Routes
PORT = 5000
IP = '127.0.0.1'
class Server():
    def __init__(self, host, port, queue) -> None:
        """Initializes class instance
        Parameters:
        
        host: str
            ip address
        port: int
            port you are using 
        queue: int
            number of alowed clients in queue befor cutting of new clients

        """
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._host = host 
        self._port = port
        self._router_list = []
        self._queue = queue
        self._is_running = False
        self._server_socket.bind(self._host,self._port)
    def start_server(self):
        """Starts server
        """
        if self._is_running:
            print('Server is alredy running')
        else:
            self._is_running = True
            self._server_socket.listen(self._queue)
            self._client_conection()

    def _client_conection(self):
        """waits for conections
        """
        while self._is_running:
            client_socket, address = self._server_socket.accept()
            try:
                request = client_socket.recv(1024).decode('utf-8')
                self._get_response(request, client_socket)
            except Exception as exc:
                print('Error: ')
                print(exc)
            
    def _get_response(self, request, client_socket):
        """
        Creates
        """
        method, path = request.split('\n')[0].split(' ')[:2]
        for router in self._router_list:
            if router._path == path:
                client_socket.sendall(router._methods[method]().encode())
                client_socket.shutdown(socket.SHUT_WR)
                break  
        client_socket.sendall('HTTP/1.1 404\r\n'.encode())
        client_socket.shutdown(socket.SHUT_WR)

    def add_router(self, route):
        self._router_list.append(Routes(route))

    def stop_server(self):
        if self._is_running:
            self._is_running = False
        

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
