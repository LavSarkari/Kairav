
import os,sys
import time
import requests


u="\033[4m"
w="\033[00m"
r="\033[91;1m"
b="\033[34;1m"
y="\033[33;1m"
g="\033[32;1m"

def start():
 try:
        proxy = ['66.42.39.36:8080']
        print ("")
        print (g+"\n [+] Whois Lookup ! ! !")
        website = input(b+" [+]"+w+" Domain/IP target: ")
        result = os.system('whois '+ website)
        print (b)
        print (result)
        print ("")
        text = str(input(w+"[ Enter ]"))
        if text == " ":
                pass
        else:
                sys.exit(0)
 except:
        input(' [ ENTER ] ')
        os.system('Kairav')
        
