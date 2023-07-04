from lib.py_express.routes import Routes
from lib.py_express.server import Response
from lib.py_express.server import Request


def home_route_get(res: Response, req: Request, next=None):
    res.status(200)
    res.headers(["Content-Type: text/html", "charset=utf-8"])
    res.mesage(f"Server is online")
    res.send()


def home_route(path):
    route = Routes(path)
    route.get(home_route_get)
    return route
