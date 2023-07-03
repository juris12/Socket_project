from lib.py_express.routes import Routes
from lib.py_express.server import Response
from lib.py_express.server import Request


def files_route_get(res: Response,req: Request,next=None):
    res.status(200)
    res.headers(['Content-Type: text/html','charset=utf-8'])
    res.send_img('files/' + req.params)


def files_route(path):
    route = Routes(path)
    route.get(files_route_get)
    return route