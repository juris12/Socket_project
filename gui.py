import os
import json
from tabulate import tabulate
import keyboard


class Ui():
    def __init__(self):
        self.register_or_login = 'Register'
        self.name = None
        self.pwd = None
        self.ip = None
        self.port = None
    def get_regester_or_login(self):
        self.log_screan('Register')
        while True:
            match keyboard.read_key():
                case 'right':
                    self.log_screan('Login')
                    self.register_or_login = 'Login'
                case 'left':
                    self.log_screan('Register')
                    self.register_or_login = 'Register'
                case 'enter':
                    return self.register_or_login
    def get_name_and_pwd(self):
        self.log_screan('Register')
        
        while True:
            match keyboard.read_key():
                case 'right':
                    self.log_screan('Login')
                    self.register_or_login = 'Login'
                case 'left':
                    self.log_screan('Register')
                    self.register_or_login = 'Register'
                case 'enter':
                    return self.register_or_login

    def all_profill(active,list):
        headers = ['..................name..................','..................status..................']
        rows = [
            ([f".                 {val['name']}",f".                 {val['status']}"] if active == i 
            else [f".                 {val['name']}",f".                 {val['status']}"])
                for i,val in enumerate(list)]
        os.system('cls')
        print(tabulate(rows, headers, tablefmt='grid'))
    def log_screan(self,state):
        gui = f"""
            **************************************************************
            *                                                            *
            *                                                            *                                   
            *                Register            Login                   *  
            *                                    *****                   *
            *                                                            *
            **************************************************************
            """
        gui2 = f"""
            **************************************************************
            *                                                            *
            *                                                            *                                   
            *                Register            Login                   *  
            *                ********                                    *
            *                                                            *
            **************************************************************
            """
        os.system('cls')
        if state == 'Register':
            print(gui2)
            self.register_or_login = 'Login'
        else:
            print(gui)
            self.register_or_login = 'Register'
