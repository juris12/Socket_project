import pickle

class Profile():
    def __init__(self,name,pwd_hash,ip):
        self.name = name
        self.pwd_hash = pwd_hash
        self.ip = ip
        self.status = False

class Db():
    def __init__(self):
        self._profil_list = []
        try:
            data = self._read_to_db()      
        except:
            data = []
            self._write_to_db(data)
        self._profil_list: list = data

    def _read_to_db(self):
        with open('data.pickle', 'rb') as file:
            return pickle.load(file) 
            
    def _write_to_db(self,data):
        with open('data.pickle', 'wb') as file:
            pickle.dump(data, file)

    def add_profil(self, profile: Profile):
        self._profil_list.append(profile)
        self._write_to_db(self._profil_list)
    def change_status(self, i: Profile):
        for z in self._profil_list:
            try:
                if z.name == i: z.status = not z.status
            except KeyError:
                pass
        self._write_to_db(self._profil_list)

    def get(self,i=None):
        if i:
            for z in self._profil_list:
                try:
                    if z.name == i: return z
                except KeyError:
                    pass
            return None
        return self._profil_list
