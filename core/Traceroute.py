
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
        print ("")
        website = str(input(b+"[+]"+w+" Domain/IP target: "))
        result = requests.get('https://api.hackertarget.com/mtr/?q=' + website).text
        print (y+result)
        print ("")
 except:
        input('[ ENTER ]')
        os.system('Kairav')
