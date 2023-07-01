PORT = 5001
IP = '127.0.0.1'
from lib.py_express.server import Server
from home_route import home_route

server = Server()

server.route('/',home_route)

server.listen(IP,PORT,5)
