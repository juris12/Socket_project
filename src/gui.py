import os
import json
from tabulate import tabulate
import keyboard
import time


class Ui():
    def __init__(self):
        self.register_or_login = 'Register'
        self.name = '-----------'
        self.pwd = '-----------'
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
        if self.register_or_login == 'Register':
            self.reg_screan('Register')
        else:
            self.reg_screan('  Login ')

        

    def all_profill(self,active,list,profil):
        os.system('cls')
        print('**************************************************************')
        print(f' Name: {profil[0]["name"]}     IP: {profil[0]["ip"]}')
        print('**************************************************************')
        headers = ['..................name..................','..................status..................']
        rows = [
            ([f"@                 {val['name']}",f"@                 {val['status']}"] if active == i 
            else [f".                 {val['name']}",f".                 {val['status']}"])
                for i,val in enumerate(list)]
        
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
        else:
            print(gui)

            
    def reg_screan(self,state):
            gui = f"**************************************************************\n{state}\n" 

            os.system('cls')
            print(gui)
            print("**************************************************************")
            input()
            self.name = input('NAME: ')
            time.sleep(0.5)
            print("**************************************************************")
            os.system('cls')
            print(gui)
            print("**************************************************************\n")
            self.pwd = input('PASSWORD: ')
            time.sleep(0.5)


