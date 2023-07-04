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
    res.json([x for x in db.get() if x.status])
    res.send()
def profil_route_post(res: Response,req: Request,next=None):
    db = Db()
    res.status(200)
    res.headers(['Content-Type: application/json'])
    user = [x for x in db.get() if x.name == req.params]

    if len(user) == 1:
        db.change_status(user[0].name)
        res.mesage(f'"mesage":"Status cnaged for user {user[0].name} to {user[0].status}"')
    else:
        res.mesage('"mesage":"no user found"')
    res.send()




def profil_route(path):
    route = Routes(path)
    route.post(profil_route_post)
    route.get(profil_route_get)
    return route