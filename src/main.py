PORT = 5000
IP = "127.0.0.1"
import sys
import os
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(parent_dir, ".."))
from lib.py_express.server import Server
from routes.home_route import home_route
from routes.register_route import register_route
from routes.profil_route import profil_route
from routes.login_route import login_route

#create server instance

server = Server()


# add routes to server
server.route("/", home_route)
server.route("/register", register_route)
server.route("/login", login_route)
server.route("/profil/:id", profil_route)

# start server
server.listen(IP, PORT, 5)
