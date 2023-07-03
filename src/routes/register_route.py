from lib.py_express.routes import Routes
from lib.py_express.server import Response
from lib.py_express.server import Request
from db import Profile
from db import Db
import bcrypt
import json

def is_name_uesd(name):
    db = Db()
    prof_list = db.get()
    for i in prof_list:
        if i.name == name:
            return True
    return False
def register_route_post(res: Response,req: Request,next=None):
    try:
        if is_name_uesd(req.body["name"]):
            res.status(400)
            res.headers(['Content-Type: application/json'])
            res.mesage(f'Name {req.body["name"]} alredy exist!')
        else:
            db = Db()
            hashed_password = bcrypt.hashpw(req.body['pwd_hash'].encode("utf-8"), bcrypt.gensalt())
            db.add_profil(
                Profile(req.body['name'],hashed_password,'127.0.0.1')
            )
            res.status(200)
            res.headers(['Content-Type: application/json'])
            res.mesage(f'profil with name: {req.body["name"]} is created!')
    except KeyError:
        res.status(400)
        res.headers(['Content-Type: application/json'])
        res.mesage(f'No name or pwd!')       
    res.send()



def register_route(path):
    route = Routes(path)
    route.post(register_route_post)
    return route