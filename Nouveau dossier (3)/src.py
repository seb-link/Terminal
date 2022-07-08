
#create a terminal
import os
import sys
import time
import random
import subprocess




def main() :
    print("""
    
    Séb-sh terminal v1.0
    bye.
    
    """)
    user = input("Enter your username: ")
    os.system("cls")
    while True: 
        command = input("{}@terminal:~$ ".format(user))
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "clear":
            os.system("cls")
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
                    os.chdir(command)
        elif command.startswith('random'):
            if command.replace('random', '') == '' or command.replace('random', '') == ' ':
                print("You must enter a number")
            else:
                command = command.replace('random ', '')
                print(random.randint(1, int(command)))
        elif command == "credits":
            print("""
            Séb-sh terminal v1.0
            ##############################################################
            open source terminal emulator
            ##############################################################
            do not use this terminal for illegal purposes
            ##############################################################
            this terminal is not safe for use in any other terminal
            ##############################################################
            thank you for using this terminal
            """)
        else :
            try : 
                subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                subprocess.call(command, shell=True)
            except subprocess.CalledProcessError:
                print("Séb-sh probleme with command")
                continue
main()











