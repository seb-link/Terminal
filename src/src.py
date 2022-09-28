
#create a terminal
import hashlib
import ctypes
import os
from pathlib import Path
import sys
import time
import random
import subprocess
import getpass
import win32com.shell.shell as shell


def add_user(name,password,group) :
    try :
        os.mkdir("C:\Program Files\Seb-sh")
        os.mkdir("C:\Program Files\Seb-sh/User")
    except FileExistsError:
        pass
    try :
        os.mkdir("C:\Program Files\Seb-sh/User\{}".format(name))
    except FileExistsError:
        print("user already exists")
        return 1
    os.chdir("C:\Program Files\Seb-sh/User/{}".format(name))
    with open("shadow.pass","w") as shadow:
        shadow.write(password)
    with open("group.info","w") as g:
        g.write(group)
        g.close()
    # mettre group.info en read-only
    os.system('powershell("sp group.info IsReadOnly $true")')
version = "v1.2"
def get_name():
    user = input("Enter your username (entrer guest if you have no account): ")
    list = os.listdir("C:\Program Files\Seb-sh/User")
    if user == "guest":
        print("ok guest")
    else :
        if user not in list:
            exit("no account found")
        else :
            pas = getpass.getpass("Entrer {} password : ".format(user))
            pass_hash = hashlib.sha512(pas.encode()).hexdigest()
            del pas
            with open("C:\Program Files\Seb-sh/User/{}/shadow.pass".format(user), "r") as  v :
                inside = v.read()
                v.close()
            if pass_hash != inside :
                exit("Wrong password !")
            else :
                return user
                
def perm(name,group) :
    try :
        os.mkdir("C:\Program Files\Seb-sh/conf")
        os.mkdir("C:\Program Files\Seb-sh/conf/perm")
    except FileExistsError:
        pass
    try :
        f = open("C:\Program Files\Seb-sh/User/{}".format(name) , "r")
        f.close()
    except FileExistsError:
        exit("user don't exist lol")
    if "C:\Program Files\Seb-sh/conf/perm/admin".exists() :
        pass
    else :
        try :
            perm = open("C:\Program Files\Seb-sh/conf/perm/{}".format(group),"w")
        except FileExistsError:
            pass
        perm.write("{} \n".format(name))


def check_integrity() :
    try :
        os.mkdir("C:\Program Files\Seb-sh/conf")
        os.mkdir("C:\Program Files\Seb-sh/conf/perm")
        os.mkdir("C:\Program Files\Seb-sh/User")
        if os.path.exists("C:\Program Files\Seb-sh/conf/perm/admin") :
            pass
        else :
            print('no group name "admin"')
            return
    except FileExistsError:
        print("ok all good !")

def get_group(user) :
    try :
        f = open("C:\Program Files\Seb-sh/User\{}\group.info".format(user), "r")
        group = f.read()
    except FileNotFoundError :
        print("user do not exist")
    return group
def main() :
    os.system('title Terminal')
    print("""
    
    Séb-sh terminal {}
    =====================


    
    """.format(version))
    mode = 'normal'
    user = ''
    if ctypes.windll.shell32.IsUserAnAdmin() :
        user = 'admin'
    else :
        user = get_name()
    while True: 
        command = input("{}@terminal:~$ ".format(user))
        if command == "exit":
            print("Goodbye!")
            return 0
        elif command == "perm" :
            name = input("Enter the user name : ")
            group = input("Enter the group to move :")
            perm(name,group)
        elif command == "add_user" : 
            name = input("Enter the name of the user : ")
            password = getpass.getpass("Enter your password : ")
            # hash the password with SHA 512
            hashed_password = hashlib.sha512(password.encode()).hexdigest()
            del password
            group = input("Enter the user group : ")
            add_user(name, hashed_password, group)
        elif command.startswith("echo") :
            command.replace("echo ", "")
            print(command)
        elif command == "clear":
            os.system("cls")
        elif command == "debug":
            if mode == 'debug':
                mode = 'normal'
                print("Debug mode disabled")
            else:
                passwd = getpass.getpass("Enter password: ")
                if passwd == "seb-sh":
                    mode = 'debug'
                    print("Debug mode enabled")
                else:
                    print("Wrong password")
        elif command == "help":
            print("""
            list of custom commands:
                help - displays this help message
                exit - exits the program
                clear - clears the screen
                time - displays the current time
                name - sets your name
            for list of built-in commands type "super-help"
            """)
        elif command == "time":
            #print current time
            print(time.strftime("%H:%M:%S"))
        elif command == "super-help":
            subprocess.call("help", shell=True)
        elif command.startswith('name'):
            if command.replace('name', '') == '' or command.replace('name', '') == ' ':
                print(user)
            else :
                command = command.replace('name ', '')
                user = command
        elif command.startswith('cd'):
            if command.replace('cd', '') == '' or command.replace('cd', '') == ' ':
                print("You must enter a directory")
            else:
                command = command.replace('cd ', '')
                if command == "..": 
                    os.chdir("..")
                else:
                    try :
                        os.chdir(command)
                    except FileNotFoundError:
                        print("directory not found")
                    except :
                        print("error")
        elif command.startswith('random'):
            if command.replace('random', '') == '' or command.replace('random', '') == ' ':
                print("You must enter a number")
            else:
                command = command.replace('random ', '')
                print(random.randint(1, int(command)))
        elif command == "credits":
            print("""
            Séb-sh terminal {}
            ##############################################################
            open source terminal emulator
            ##############################################################
            do not use this terminal for illegal purposes
            ##############################################################
            this terminal is not safe for use in any other terminal
            ##############################################################
            there is some easter egg in this terminal
            ##############################################################
            thank you for using this terminal
            """.format(version))
        elif command.startswith("color"):
            if command.replace('color', '') == '' or command.replace('color', '') == ' ':
                print("You must enter a color")
            else:
                command = command.replace('color ', '')
                os.system("color {}".format(command))
        elif command == "hack":
            pwd = os.getcwd()
            os.chdir("C:/")
            start = time.time()
            if time.time() - start > 5:
                os.chdir(pwd)
                print("You have been hacked NASA ")
            else:
                os.system("dir /s")
        elif command == "pwd":
            print(os.getcwd())
        elif command == "ls":
            os.system("dir")
        elif command == "secret":
            if mode == "debug":
                print("""
                The key to the door is: 42
                """)
            else:
                print("there is nothing to see here...")
        elif command.startswith("rm"):
            if command.replace('rm', '') == '' or command.replace('rm', '') == ' ':
                print("You must enter a file name")
            else:
                command = command.replace('rm ', '')
                try:
                    os.remove(command)
                except FileNotFoundError:
                    print("file not found")
        elif command.startswith('sudo') :
            command = command.replace("sudo ", "")
            if get_group(user) != "admin" :
                print("access denied !")
        elif command == "version" or command == "ver" :
            print("Seb-sh terminal {}".format(version))
        elif command == "whoami" :
            if ctypes.windll.shell32.IsUserAnAdmin() :
                if mode == "debug" :
                    print("admin::debug")
                else :
                    print("admin")
            elif mode == "debug" :
                print(user + "::debug")
            else :
                print(user)
        else :
            print("command not found")
def inisialize():
    check_integrity()
    main()
inisialize()