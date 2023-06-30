class Router_func:
    def __init__(self,req,res, next=None):
        self.req = req
        self.res = res
        self.next = next
class Routes:
    def __init__(self, path) -> None:
        self._path = path
        self._methods = {
            'GET': None,
            'PUT': None,
            'POST': None,
            'DELETE': None
        }
    def get(self, func):
        self._methods['GET'] = func
    def put(self, func):
        self._methods['PUT'] = func
    def post(self, func):
        self._methods['POST'] = func
    def delite(self, func):
        self._methods['DELETE'] = func

    
    