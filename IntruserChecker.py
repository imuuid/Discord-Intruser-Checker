import requests, colorama, time, random, os, subprocess, threading
from colorama import Fore, init, Style
os.system("title IntruserChecker")
request_url = "https://canary.discordapp.com/api/v9/users/@me"
os.system('cls')

def write_good_tokens(Token):
    with open("worked_tokens.txt", "a") as file:
        file.write(f"{Token}\n")

def write_bad_tokens(Token):
    with open("bad_tokens.txt", "a") as file:
        file.write(f"{Token}\n")
        
print(f"""{Fore.LIGHTRED_EX}                          
╦┌┐┌┌┬┐┬─┐┬ ┬┌─┐┌─┐┬─┐╔═╗┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐
║│││ │ ├┬┘│ │└─┐├┤ ├┬┘║  ├─┤├┤ │  ├┴┐├┤ ├┬┘
╩┘└┘ ┴ ┴└─└─┘└─┘└─┘┴└─╚═╝┴ ┴└─┘└─┘┴ ┴└─┘┴└─ """)

print("")
print("")
print("")
print("")
print(f"""{Fore.LIGHTRED_EX}
                                       ╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗	
                                       ║                                                                                                                    ║
                                       ║                                                                                                                    ║
                                       ║                                                                                                                    ║
                                       ║                                            1: Check The Tokens in tokens.txt                                       ║
                                       ║                                            2: Leave The Checker                                                    ║
                                       ║                                                                                                                    ║
                                       ║                                                                                                                    ║
                                       ║                                                                                                                    ║
                                       ╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝
""")
option = input("Your choice : ")

if option == '1': os.system('cls')

print(f"""{Fore.LIGHTGREEN_EX}                         
 ██▓ ███▄    █ ▄▄▄█████▓ ██▀███   █    ██   ██████ ▓█████  ██▀███      ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓██ ▒ ██▒ ██  ▓██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒   ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄   ▒███   ▓██ ░▄█ ▒   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄     ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░██░▒██░   ▓██░  ▒██▒ ░ ░██▓ ▒██▒▒▒█████▓ ▒██████▒▒░▒████▒░██▓ ▒██▒   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░ ░░   ░ ▒░    ░      ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░     ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ▒ ░   ░   ░ ░   ░        ░░   ░  ░░░ ░ ░ ░  ░  ░     ░     ░░   ░    ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
 ░           ░             ░        ░           ░     ░  ░   ░        ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                                                                      ░                       ░                                """)
print("")
print("")
print("")
with open("tokens.txt") as f:
    for line in f:
        token = line.strip("\n")
        headers = {'Content-Type': 'application/json', 'authorization': token}
        url = "https://discordapp.com/api/v9/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code in range(200, 299):
            write_good_tokens(token)
            print(token + " : Tokens Worked .".format(line.strip("\n")))
            print("")
            
        else:
            write_bad_tokens(token)
            print(token + " : Tokens Phone Locked Or Not Works")
            print("")
          
print("")
print("")
input("Ty for using IntruserChecker, our server: https://discord.gg/PC3T6HapUZ Checker by NothingTime#0001: ")   


