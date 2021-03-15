
import os,sys
import time
import requests
import json

u="\033[4m"
w="\033[00m"
r="\033[91;1m"
b="\033[34;1m"
y="\033[33;1m"
g="\033[32;1m"

def start():
 try:
        print ("")
        website = str(input(b+"[+]"+w+" Domain/IP target: "))
        mysite = {"remoteAddress":website}

        link = requests.post("https://domains.yougetsignal.com/domains.php" , mysite)

        source = json.loads(link.content)

        print(source)


        for data in source["domainArray"]:
                print(" "+data[0]+"\n")
        print ("")
        text = str(input(w+"[ enter ]"))
        if text == " ":
                os.system(Kairav)
        else:
                sys.exit(0)
 except:
        input('[ ENTER ]')
        os.system('Kairav')
