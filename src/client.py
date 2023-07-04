import socket
from gui import *
import time
import os
from img_to_ascii import capture_image
import cv2

IP = "127.0.0.1"
PORT = 5000


class Client:
    def __init__(self) -> None:
        self.is_reciving_call = False
        ...

    def get_all(self):
        """
        get all user
        """
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((IP, PORT))
            client_socket.send("GET /profil HTTP/1.1\r\n".encode())
            response = b""
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                response += data
            response = response.decode()
            client_socket.shutdown(socket.SHUT_WR)
            if len(response.split("\r\n\r\n")) >= 2:
                return json.loads(response.split("\r\n\r\n")[1])
            else:
                return None
        except ConnectionRefusedError as err:
            print(err)

    def register(self, name, pwd):
        """
        register user
        """
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((IP, PORT))
            client_socket.send(
                f'POST /register HTTP/1.1\r\n\r\n{{"name":"{name}","pwd_hash":"{pwd}"}}'.encode()
            )
            response = b""
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                response += data
            response = response.decode()
            client_socket.shutdown(socket.SHUT_WR)
            if len(response.split("\r\n\r\n")) >= 2:
                return response.split("\r\n\r\n")[1]
            else:
                return None
        except ConnectionRefusedError as err:
            print(err)

    def login(self, name, pwd):
        """
        lets user sign in
        """
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((IP, PORT))
            client_socket.send(
                f'POST /login HTTP/1.1\r\n\r\n{{"name":"{name}","pwd_hash":"{pwd}"}}'.encode()
            )
            response = b""
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                response += data
            response = response.decode()
            client_socket.shutdown(socket.SHUT_WR)
            if len(response.split("\r\n\r\n")) >= 2:
                return response.split("\r\n\r\n")[1]
            else:
                return None
        except ConnectionRefusedError as err:
            print(err)

    def change_status(self, name):
        """
        changes user status
        """
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((IP, PORT))
            client_socket.send(f"POST /profil/{name} HTTP/1.1\r\n\r\n".encode("utf-8"))
            response = b""
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                response += data
            response = response.decode()
            client_socket.shutdown(socket.SHUT_WR)
            if response != '"mesage":"no user found"':
                return True
            else:
                return False
        except ConnectionRefusedError as err:
            print(err)

    def recive(self):
        """
        starts server
        """
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((IP, 3001))
        server.listen()
        client, _ = server.accept()
        flag = 0
        print("camera loading....")
        cap = cv2.VideoCapture(0)
        print("camera redy....")
        if not cap.isOpened():
            print("Failed to open the webcam")
        else:
            while flag < 200:
                mesage = client.recv(8192).decode("utf-8")
                client.send(capture_image(cap).encode("utf-8"))
                os.system("cls")
                print(mesage)
                flag += 1
        cap.release()
        client.close()
        server.close()

    def call(self, ip):
        """
        initiats calll
        """
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, 3001))
        flag = 0
        print("camera loading....")
        cap = cv2.VideoCapture(0)
        print("camera redy....")
        if not cap.isOpened():
            print("Failed to open the webcam")
        else:
            while flag < 200:
                client.send(capture_image(cap).encode("utf-8"))
                mesage = client.recv(8192).decode("utf-8")
                os.system("cls")
                print(mesage)
                flag += 1
        cap.release()
        client.close()


client = Client()

ui = Ui()
ui.get_regester_or_login()
ui.get_name_and_pwd()
if ui.register_or_login == "Register":
    print(client.register(ui.name, ui.pwd))
else:
    profil = client.login(ui.name, ui.pwd)
    if profil != '"message":"Name or pwd is incorect!"':
        profil = json.loads(profil)
        profil_list = client.get_all()
        activ_index = 0
        print(ui.all_profill(activ_index, profil_list, profil))

        while not client.is_reciving_call:
            profil_list = client.get_all()
            match input("comand: "):
                case "up":
                    if activ_index != 0:
                        activ_index -= 1
                    print(ui.all_profill(activ_index, profil_list, profil))
                    time.sleep(0.5)
                case "down":
                    if activ_index != len(profil_list) - 1:
                        activ_index += 1
                    print(ui.all_profill(activ_index, profil_list, profil))
                    time.sleep(0.5)
                case "c":
                    os.system("cls")
                    if not profil_list[activ_index + 1]["status"]:
                        print("Usser is offline")
                        time.sleep(1.5)
                        os.system("cls")
                        print(ui.all_profill(activ_index, profil_list, profil))
                    else:
                        print(profil_list[activ_index + 1])
                        print(f'caling {profil_list[activ_index+1]["name"]}........')
                        time.sleep(1.5)
                        client.call("127.0.0.1")

                    # client.recive()
                case "l":
                    print("User is logged out!")
                    break
                case "o":
                    os.system("cls")
                    client.is_reciving_call = True
                    if client.change_status(profil[0]["name"]):
                        print("Whaiting for incomming calls....... press q to quit")
                        client.recive()
                        input("end: ")
                        client.change_status(profil[0]["name"])
                    else:
                        print("error: wrong response")

    else:
        print(profil)
