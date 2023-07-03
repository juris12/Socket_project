from lib.py_express.routes import Routes
from lib.py_express.server import Response
from lib.py_express.server import Request
from db import Profile
from db import Db
import json


def home_route_get(res: Response,req: Request,next=None):
    db = Db()
    res.status(200)
    res.headers(['Content-Type: text/html','charset=utf-8'])
    # res.headers(['Content-Type: application/json'])
    db.add_profil(
        Profile('Jhon','fasfasf','127.0.0.1')
    )
    db.add_profil(
        Profile('dddn','fasfasf','127.0.0.1')
    )
    db.add_profil(
        Profile('ffffJhon','fasfasf','127.0.0.1')
    )
    db.add_profil(
        Profile('dgggddn','fasfasf','127.0.0.1')
    )
    db.add_profil(
        Profile('Jhohhhhn','fasfasf','127.0.0.1')
    )
    db.add_profil(
        Profile('dddn','fasfasf','127.0.0.1')
    )
    res.json(db.get())
    res.send()
def home_route_post(res: Response,req: Request,next=None):
    res.status(200)
    res.headers(['Content-Type: text/html','charset=utf-8'])
    res.mesage(f'<html><body><h1>{req.body}</h1></body></html>')
    res.send()




def home_route(path):
    route = Routes(path)
    route.post(home_route_post)
    route.get(home_route_get)
    return route