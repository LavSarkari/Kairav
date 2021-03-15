#!/usr/bin/env python3
import sys
import socket
import os
import time
from modules import menu
from core import apfinder,robots,findshareddns,dnslookup,Traceroute,httpheader,portscan,whois,cms,iplocation,reviplookup

try:
    from colorama import Fore
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install colorama\n
    pip3 install colorama
        """)

#---------------------------

try:
    import requests
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install requests\n
    pip3 install requests
        """)

#---------------------------


try:
    import ipapi
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install ipapi\n
    pip3 install ipapi
        """)

#---------------------------


try:
    import builtwith
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install builtwith\n
    pip3 install builtwith
        """)
#---------------------------

os.system('clear')

while True:


    try:
        menu.banner()
        menu.mainList()
        number = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Kairav"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+" ").lower()
    except:
        print("\n Oops! :-\ [ERROR] ")
        sys.exit()
    if number == '4':

        print
        sys.exit()

        #####################
    elif number == 'update' or number == '3':
       os.system('bash /data/data/com.termux/files/usr/share/Kairav/update.sh')
    elif number == "2":
       menu.banner()
       menu.List()
       no =  input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Kairav"+Fore.BLUE+"~"+Fore.WHITE+"@MORE"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+" ").lower()
       if no == '1':
          os.system('xdg-open https://lavsarkari.github.io/Kairav')
       elif no == '2':
          os.system('xdg-open https://github.com/LavSarkari/Kairav')
       elif no == '3':
          os.system('xdg-open https://instagram.com/_.geniusman._')
       elif no == '4':
          os.system('xdg-open https://lavsarkari.github.io/')
        #-------------------#
    elif number == 'help' or number == '?':
         menu.helpList
    elif number == '1':
        try:
            menu.banner()
            menu.infoList()
            infor = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Kairav"+Fore.BLUE+"~"+Fore.WHITE+"@Home/Infoga"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"+").lower()

                #####################


            if infor == "9":
                menu.banner()
                cms.start()

                #####################


            elif infor == "4":
                menu.banner()
                Traceroute.start()

                #####################


            elif infor == "2":
                menu.banner()
                reverseip.start()

                #####################

            elif infor == "3":
                menu.banner()
                portscan.start()

                #####################

            elif infor == "5":
                menu.banner()
                iplocation.start()

                #####################

            elif infor == "6":
                menu.banner()
                httpheader.start()

                #####################

            elif infor == "7":
                menu.banner()
                findshareddns.start()

                #####################

            elif infor == "1":
                menu.banner()
                whois.start()

                #####################

            elif infor == "8":
                menu.banner()
                dnslookup.start()
                #####################

            elif infor == "10":
                menu.banner()
                robots.start()
                #####################

            elif infor == "11":
                menu.banner()
                finder.start()

                #####################

            elif infor == "12":
                input(Fore.RED+" [!]"+Fore.GREEN+" Back To Menu (Press Enter...) ")

                #####################
            elif infor == "13" or infor == "exit":
                sys.exit()

                #####################
            elif infor == "":
                input(Fore.RED+" [!]"+Fore.GREEN+" Please Enter Number (Press Enter...) ")
        except KeyboardInterrupt:
            print("")
            sys.exit()
