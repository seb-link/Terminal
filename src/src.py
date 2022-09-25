
#create a terminal
import os
import time
import random
import subprocess
import getpass


def main() :
    os.system('title Terminal')
    print("""
    
    Séb-sh terminal v1.1
    =====================


    
    """)
    mode = 'normal'
    user = input("Enter your username: ")
    os.system("cls")
    while True: 
        command = input("{}@terminal:~$ ".format(user))
        if command == "exit":
            print("Goodbye!")
            return 0
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
                    except :
                        print("directory not found")
        elif command.startswith('random'):
            if command.replace('random', '') == '' or command.replace('random', '') == ' ':
                print("You must enter a number")
            else:
                command = command.replace('random ', '')
                print(random.randint(1, int(command)))
        elif command == "credits":
            print("""
            Séb-sh terminal v1.1
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
            """)
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
        else :
            try : 
                subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                subprocess.call(command, shell=True)
            except subprocess.CalledProcessError:
                print("Séb-sh probleme with command")
                continue
main()










