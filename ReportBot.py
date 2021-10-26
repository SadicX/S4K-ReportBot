# coding=utf-8
#!/usr/bin/env python3

from libs.check_modules import check_modules
from sys import exit
from os import _exit

check_modules()

from os import path

from libs.logo import print_logo
from libs.utils import print_success
from libs.utils import print_error
from libs.utils import ask_question
from libs.utils import print_status
from libs.utils import parse_proxy_file
from libs.proxy_harvester import find_proxies
from libs.attack import report_profile_attack
from libs.attack import report_video_attack

from multiprocessing import Process
from colorama import Fore, Back, Style

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def profile_attack_process(username, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_profile_attack(username, None)
        return

    for proxy in proxy_list:
        report_profile_attack(username, proxy)

def video_attack_process(video_url, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_video_attack(video_url, None)
        return

    for proxy in proxy_list:
        report_video_attack(video_url, proxy)

def video_attack(proxies):
    video_url = ask_question("Ingrese el enlace del video que desea reportar")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=video_attack_process, args=(video_url, [],))
            p.start()
            print_status(str(k + 1) + ". ¡Transacción abierta!")
            if (k == 5): print()
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("¡El ataque de reclamo por video está en marcha!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=video_attack_process, args=(video_url, proxy_list,))
        p.start()
        print_status(str(i) + ". ¡Transacción abierta!")
        if (k == 5): print()
        i = i + 1

def profile_attack(proxies):
    username = ask_question("Ingrese el nombre de usuario de la persona que desea reportar")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=profile_attack_process, args=(username, [],))
            p.start()
            print_status(str(k + 1) + ". ¡Transacción abierta!")
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("¡El ataque de queja de perfil está comenzando!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=profile_attack_process, args=(username, proxy_list,))
        p.start()
        print_status(str(i) + ". ¡Transacción abierta!")
        if (k == 5): print()
        i = i + 1

def main():
    print_success("Módulos cargados!\n")

    ret = ask_question("Le gustaría utilizar un proxy? [Y / N]")

    proxies = []

    if (ret == "Y" or ret == "y"):
        ret = ask_question("Le gustaría recopilar sus proxies de Internet? [Y / N]")

        if (ret == "Y" or ret == "y"):
            print_status("Recopilación de proxy de Internet! Esto puede tardar un rato.\n")
            proxies = find_proxies()
        elif (ret == "N" or ret == "n"):
            print_status("Tenga un máximo de 50 proxies en un archivo!")
            file_path = ask_question("Ingrese la ruta a su lista de proxy")
            proxies = parse_proxy_file(file_path)
        else:
            print_error("Respuesta no entendida, saliendo!")
            exit()

        print_success(str(len(proxies)) + " Número de proxy encontrado!\n")
    elif (ret == "N" or ret == "n"):
        pass
    else:
        print_error("Respuesta no entendida, saliendo!")
        exit()

    

    print("")
    print_status("1 - Reportar perfil")
    print_status("2 - Reportar un video")
    report_choice = ask_question("Seleccione el método de reporte")
    print("")

    if (report_choice.isdigit() == False):
        print_error("No se comprende la respuesta.")
        exit(0)
    
    if (int(report_choice) > 2 or int(report_choice) == 0):
        print_error("No se comprende la respuesta.")
        exit(0)

    if (int(report_choice) == 1):
        profile_attack(proxies)
    elif (int(report_choice) == 2):
        video_attack(proxies)

if __name__ == "__main__":
    print_logo()
    try:
        main()
        print(Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "[*] El programa se esta cargando")
        print(Style.RESET_ALL)
        _exit(0)