# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
   _____   _  _     _  __    _____                       _     ____        _   
  / ____  | || |   | |/ /   |  __ \                     | |   |  _ \      | |  
 | (___   | || |_  | ' /    | |__) |___ _ __   ___  _ __| |_  | |_) | ___ | |_ 
  \___ \  |__   _| |  <     |  _  // _ \ '_ \ / _ \| '__| __| |  _ < / _ \| __|
  ____) |    | |   | . \    | | \ \  __/ |_) | (_) | |  | |_  | |_) | (_) | |_ 
 |_____/     |_|   |_|\_\   |_|  \_\___| .__/ \___/|_|   \__  |____/ \___/ \__|
                                       | |                                   
                                       |_|                                   """



def print_logo():
    print(Fore.BLUE + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.YELLOW + "      Visita mi Github!: https://github.com/SadicX/"+ Style.RESET_ALL + Style.BRIGHT)
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
