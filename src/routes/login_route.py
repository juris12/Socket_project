from lib.py_express.routes import Routes
from lib.py_express.server import Response
from lib.py_express.server import Request
from db import Profile
from db import Db
import bcrypt
import json

def is_not_pwd_valid(profil,pwd):
    if profil == None:
        return True
    if bcrypt.checkpw(pwd.encode('utf-8'), profil.pwd_hash):
        return False
    return True
def login_route_post(res: Response,req: Request,next=None):
    try:
        db = Db()
        profil: Profile = db.get(req.body["name"])
        if is_not_pwd_valid(profil,req.body['pwd_hash']):
            res.status(400)
            res.headers(['Content-Type: application/json'])
            res.mesage(f'"message":"Name or pwd is incorect!"')
        else:
            res.status(200)
            res.headers(['Content-Type: application/json'])
            res.json([profil])
    except KeyError:
        res.status(400)
        res.headers(['Content-Type: application/json'])
        res.mesage(f'No name or pwd!')       
    res.send()



def login_route(path):
    route = Routes(path)
    route.post(login_route_post)
    return route