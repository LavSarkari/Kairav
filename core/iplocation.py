
import os,sys
import time
import requests
from colorama import Fore

u="\033[4m"
w="\033[00m"
r="\033[91;1m"
b="\033[34;1m"
y="\033[33;1m"
g="\033[32;1m"

def start():
 try:
        print ("")
        ip = str(input(b+"[+]"+w+" IP target: "))
        source = ipapi.location(ip=ip, key=None, field=None)
        print (Fore.GREEN+" [~]"+Fore.RED+" IP Lookup Information ")
        print
        print (Fore.GREEN+" [>]"+Fore.BLUE+" ip = "+w+ source["ip"])
        print (Fore.GREEN+" [>]"+Fore.BLUE+" city = " +w+ source["city"])
        print (Fore.GREEN+" [>]"+Fore.BLUE+" region = "+w+ source["region"])
        print (Fore.GREEN+" [>]"+Fore.BLUE+" id country = "+w+source["country"])
        print (Fore.GREEN+" [>]"+Fore.BLUE+" country = "+w+ source["country_name"])
        print (Fore.GREEN+" [>]"+Fore.BLUE+" Calling Code = "+w+source["country_calling_code"])
        print (Fore.GREEN+" [>]"+Fore.BLUE+" Languages = "+w+source["languages"])
        print (Fore.GREEN+" [>]"+Fore.BLUE+" org = "+w+ source["org"])
        text = str(input(w+"[ enter ]"))

        if text == " ":
                os.system(Kairav)
        else:
                sys.exit(0)
 except:
        print (r+'There Was an ERROR!!'+w)
        print
        input('[ ENTER ]')
        os.system('Kairav')
