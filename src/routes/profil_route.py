from lib.py_express.routes import Routes
from lib.py_express.server import Response
from lib.py_express.server import Request
from db import Profile
from db import Db
import json


def profil_route_get(res: Response,req: Request,next=None):
    db = Db()
    res.status(200)
    res.headers(['Content-Type: application/json'])
    res.json(db.get())
    res.send()




def profil_route(path):
    route = Routes(path)
    route.get(profil_route_get)
    return route