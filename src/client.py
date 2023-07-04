import socket
from gui import *
import time
import os
import threading

IP = '127.0.0.1'
PORT = 5000

class Client():
    def __init__(self) -> None:
        self.is_reciving_call = False
        ...
    def get_all(self):
        try:
            client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_socket.connect((IP,PORT))
            client_socket.send("GET /profil HTTP/1.1\r\n".encode())
            response = b""
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                response += data
            response = response.decode()
            client_socket.shutdown(socket.SHUT_WR)
            if len(response.split('\r\n\r\n')) >= 2:
                return json.loads(response.split('\r\n\r\n')[1])
            else:
                return None
        except ConnectionRefusedError as err:
            print(err)
    def register(self,name,pwd):
        try:
            client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_socket.connect((IP,PORT))
            client_socket.send(f'POST /register HTTP/1.1\r\n\r\n{{"name":"{name}","pwd_hash":"{pwd}"}}'.encode())
            response = b""
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                response += data
            response = response.decode()
            client_socket.shutdown(socket.SHUT_WR)
            if len(response.split('\r\n\r\n')) >= 2:
                return response.split('\r\n\r\n')[1]
            else:
                return None
        except ConnectionRefusedError as err:
            print(err)
    def login(self,name,pwd):
        try:
            client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client_socket.connect((IP,PORT))
            client_socket.send(f'POST /login HTTP/1.1\r\n\r\n{{"name":"{name}","pwd_hash":"{pwd}"}}'.encode())
            response = b""
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                response += data
            response = response.decode()
            client_socket.shutdown(socket.SHUT_WR)
            if len(response.split('\r\n\r\n')) >= 2:
                return response.split('\r\n\r\n')[1]
            else:
                return None
        except ConnectionRefusedError as err:
            print(err)
    def recive(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((IP,3000))
        server.listen()
        client, _ = server.accept()
        flag = True
        while flag:
            mesage = client.recv(2048).decode('utf-8')
            if mesage == 'done': flag = False
            else:print(mesage)
        client.close()
        server.close()
    def call(self,ip):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((ip,3000))
        flag = True
        while flag:
            client.send(input('Mesage: ').encode('utf-8'))
            mesage = client.recv(2048).decode('utf-8')
            if mesage == 'done': flag = False
            else:print(mesage)
        client.close()
 

client = Client()

ui = Ui()
ui.get_regester_or_login()
ui.get_name_and_pwd()
if ui.register_or_login == 'Register':
    print(client.register(ui.name,ui.pwd))
else:
    profil = client.login(ui.name,ui.pwd)
    if profil != '"message":"Name or pwd is incorect!"':
        profil = json.loads(profil)
        profil_list = client.get_all()
        activ_index = 0
        print(ui.all_profill(activ_index,profil_list,profil))
       
        while not client.is_reciving_call:
            profil_list = client.get_all()
            match keyboard.read_key():
                case 'up':
                    if activ_index != 0:
                        activ_index -= 1
                    print(ui.all_profill(activ_index,profil_list,profil))
                    time.sleep(0.5)
                case 'down':
                    if activ_index != len(profil_list)-1:
                        activ_index += 1
                    print(ui.all_profill(activ_index,profil_list,profil))
                    time.sleep(0.5)
                case 'c':
                    os.system('cls')
                    if not profil_list[activ_index]['status']:
                        print('Usser is offline')
                        time.sleep(1.5)
                        os.system('cls')
                        print(ui.all_profill(activ_index,profil_list,profil))
                    else:
                        print(profil_list[activ_index])
                    
                    # client.recive()
                case 'l':
                    print('User is logged out!')
                    break
                case 'o':
                    os.system('cls')
                    client.is_reciving_call = True
                    print('Whaiting for incomming calls....... press q to quit')
                    client.recive()
                    
    else:
        print(profil)



