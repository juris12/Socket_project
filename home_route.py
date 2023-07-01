from lib.py_express.routes import Routes
from lib.py_express.server import Response


def home_route_get(res,req,next=None):
    response = Response()
    response.status(200)
    response.headers(['Content-Type: text/html','charset=utf-8'])
    response.mesage('Hggggggggggello World!!!!')
    res.sendall(response.data())
def home_route_post(res,req,next=None):
    data = 'HTTP/1.1 200\r\n'
    data += 'Content-Type: text/html; charset=utf-8\r\n'
    data += '\r\n'
    data += f'<html><body><h1>{req["body"]}</h1></body></html>'
    res.sendall(data.encode())




def home_route(path):
    route = Routes(path)
    route.post(home_route_post)
    route.get(home_route_get)
    return route