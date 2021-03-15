
import os,sys
import time
import requests, builtwith


u="\033[4m"
w="\033[00m"
r="\033[91;1m"
b="\033[34;1m"
y="\033[33;1m"
g="\033[32;1m"

def start():
 try:
        print ("")
        print (g+"\n [+] CMS Scanner ! ! !")
        target = str(input(b+"[+]"+w+" Domain: "))
        if not 'https://' in target or not 'http://' in target:
            target = 'http://'+target
        info = builtwith.parse(target)
        for name in info:
            value = ''
        for val in info[str(name)]:
            name = name.replace('-',' ')
            name = name.title()
            value += str(val)
        print(b+"\n"+name+': '+value)
        print ("")
        text = str(input(w+"[ enter ]"))
        if text == " ":
                os.system(Kairav)
        else:
                sys.exit(0)
 except:
        input('[ ENTER ]')
        os.system('Kairav')
