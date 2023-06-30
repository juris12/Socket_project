from lib.py_express import Routes



def home_route_get(res,req,next=None):
    data = 'HTTP/1.1 200 OK\r\n'
    data += 'Content-Type: text/html; charset=utf-8\r\n'
    data += '\r\n'
    data += '<html><body><h1>Hggggggggggello World!!!!</h1></body></html>'
    res.sendall(data.encode())
def home_route_post(res,req,next=None):
    data = 'HTTP/1.1 200 OK\r\n'
    data += 'Content-Type: text/html; charset=utf-8\r\n'
    data += '\r\n'
    data += f'<html><body><h1>{req["body"]}</h1></body></html>'
    res.sendall(data.encode())




def home_route(path):
    route = Routes(path)
    route.post(home_route_post)
    route.get(home_route_get)
    return route