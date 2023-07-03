PORT = 5000
IP = '127.0.0.1'
from lib.py_express.server import Server
from home_route import home_route
from files_route import files_route

server = Server()

server.route('/',home_route)
server.route('/files/:dfasf',files_route)

server.listen(IP,PORT,5)
