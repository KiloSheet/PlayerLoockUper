import os
import requests
from colorama import init, Fore, Style

init()

def playerlookup():
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print(Fore.YELLOW + "This is the player lookup.")
    print("Example of Nick - IceRush.")
    print()
    
    playerlookup_input = input("Enter the Nick: ")
    print()
    
    response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{playerlookup_input}")
    player_data = response.json()
    
    print(Fore.CYAN + str(player_data))
    print()

    print(Fore.LIGHTCYAN_EX + "Har copy bardari az in source be manzure Yatim budane shakhs hast va ba Madar e vey barkhorde jeddi khahad shod!")
    
    print("1. Lookup another player")
    print("2. Go back to the main menu")
    print()
    
    backtomm4 = input(Fore.GREEN + "root$-[~]:")
    
    if backtomm4 == "1":
        playerlookup()
    elif backtomm4 == "2":
        mainmenu()
    else:
        print(Fore.RED + "Invalid input!")

def mainmenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print()

    print(Fore.LIGHTCYAN_EX + "Har copy bardari az in source be manzure Yatim budane shakhs hast va ba Madar e vey barkhorde jeddi khahad shod!")

    print(Fore.YELLOW + "Main Menu")
    print("1. Player Lookup")
    print("2. Exit")
    print()
    
    choice = input(Fore.GREEN + "root$-[~]:")
    
    if choice == "1":
        playerlookup()
    elif choice == "2":
        exit()
    else:
        print(Fore.RED + "Invalid input!")
        mainmenu()

mainmenu()