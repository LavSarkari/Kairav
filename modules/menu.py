import os
from colorama import Fore
import time
import sys

#################### fonts colors ####################
w="\033[00m"
r="\033[31;1m"
g="\033[32;1m"
y="\033[33m"
d="\033[2;31m"
b="\033[34;1m"
p="\033[35;1m"
c="\033[36;1m"
W="\033[47m"
R="\033[41m"
B="\033[30m"
G="\033[90m"
BG="\033[100m"
####################    Banner    ####################

def banner():
 print (Fore.WHITE+'''


                                                          .%&         &
                                                 %%%     %% .%     %%%(
                                          %%%   %% *%%  %% %  %% %%( %%   %%%
                                          %%%%%%%% .  %%%     %%%  # ,%%%%%%%(           ,
                              %%%        %%%  .%%%  %% &%% %% %% ,%% %%%%  %%%%       %%%(
                              %%%%%%   %%%%      %% /%% %%%%%%% %%% %%%      %%%   %%%%%%%
                             /%.   %%%%%%/ &      %%/%% %%%.%%%% % %%         %%%%%%/   %%      #
                       %%    &%     &%%%(  %.      (%%%%%*   ,%%%%%%       %%  %%%%     %%     %%
                       %%%%  %% %%  %%%%  %%%%      %%%&   %   *%%%%     %%%%   %%%   %%(%   %%%%
                       %%%%%%%% %%%(%%%  %%%%%%  %%%%%    .%&    (%%%%  %%%%%%  %%%% %%%(%%%%%%%%
                       %%  %%%% %%%%%%%  %%%%% %%%%%      %%%&     #%%%%  %%%%  %%%% %%(%%%%  %%
                       %%*   &%(%%%%%%%  &%% %%%%%      %%% %%%      %%%%% %%%  %%%% %% %%    %%
               %%&/     %%    %% %% %%%   % %%%%%      %%%   %%%,      %%%% &%  %%%%(% %%.   %%*     %%%%
               %%%%%%%%%.%%    %%  %%%%    %%%%%     #%%   *   %%%      %%%%    %%% % %%# % (%%%%%%%%%%%
     &          %%%*   *%%%% %% %%   %%%*  %%%%     %%%   ,%%    %%*    #%%%   %%%   %% %% %%%%%    %%%#         *
      %%%%%%%%%%%%%%       %%% %%.%%   %%% %%%#    %%     % %%    #%%    %%%&%%%%  %%&&%% %%       %%%%%%%%%%%%%%
        %%%%    (%%%%#   %%   %% %% %%*  %%%%%   ,%%     %   %(     %%   %%%%%   %%,%%% %   *%    %%%%%     %%%#
          %%%%  %%%*%%%    %%%%& %  %& %%%%%%%(  %%     %& %  %     %%   %%%#%%%/ %% %%  %%%%   %%% %%%%  %%%%
            %%%%# .%%% %%%   (%%%%%&%%     &%%%  %%    ,% .%  %%    %%  %%%%     %%& %%%%%   ,%% %%%%  %%%%&
               %%%%%%     %%%(    %%%& %%%%%, %%. %%   %% /%# %%   %%  %%  &%%%% %%%%     %%%     *%%%%%%
                  /%%%%%%%%%%%%%%%%%&          %%%% %   %  %* %%  %(*%%#           &%%%%%%%%%%%%%%%%
                           ,**,     %%%%%&,    .,   *%%% % % %%%%%(         .%%%%%%,
                                 %%%    ,           &%%    %    %%%%.               %%/
                               %%%%%%%%%%%%%%%    /%%%%&.#%#%% /%%%%&   .%%%%%%%%%%%%%%%%
                                          %%%%&%%%%%%%%%%     #%%%%%%%%%&(#%%%

 '''+Fore.LIGHTRED_EX+'''
                                ||=====================================================||
                                ||Tool Name      : '''+Fore.WHITE+'''Kairav'''+Fore.LIGHTRED_EX+'''                              ||
                                ||Author         : '''+Fore.WHITE+'''Lav Sarkari'''+Fore.LIGHTRED_EX+'''                         ||
                                ||Tool Website   : '''+Fore.WHITE+'''https://lavsarkari.github.io/Kairav'''+Fore.LIGHTRED_EX+''' ||
                                ||Version        : '''+Fore.WHITE+'''1.0.0 (BETA)'''+Fore.LIGHTRED_EX+'''                        ||
                                ||Author Website : '''+Fore.WHITE+'''https://lavsarkari.github.io'''+Fore.LIGHTRED_EX+'''        ||
                                ||=====================================================||


''')

####################   Lits   ####################
def mainList():

    time.sleep(0.1)
    print(Fore.RED+"["+Fore.WHITE+"+"+Fore.RED+"]"+Fore.CYAN+" Choose one of the options below \n")

    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX+" [1] Information Gathering\n")

    time.sleep(0.1)
    print(Fore.YELLOW+" [2] More \n")

    time.sleep(0.1)
    print(Fore.YELLOW+" [3] Update\n")

    time.sleep(0.1)
    print(Fore.WHITE+" [4] Exit\n")


def infoList():
    time.sleep(0.1)
    print(Fore.GREEN+"  [01]"+Fore.BLUE+" - Whois")
    time.sleep(0.2)

    print(Fore.GREEN+"  [02]"+Fore.BLUE+" - Reverse IP")
    time.sleep(0.1)

    print(Fore.GREEN+"  [03]"+Fore.BLUE+" - NMAP Port Scan")
    time.sleep(0.1)

    print(Fore.GREEN+"  [04]"+Fore.BLUE+" - Trace Toute")
    time.sleep(0.1)

    print(Fore.GREEN+"  [05]"+Fore.BLUE+" - IP location Finder")
    time.sleep(0.1)

    print(Fore.GREEN+"  [06]"+Fore.BLUE+" - Show HTTP Header")
    time.sleep(0.1)

    print(Fore.GREEN+"  [07]"+Fore.BLUE+" - Find Shared DNS")
    time.sleep(0.1)

    print(Fore.GREEN+"  [08]"+Fore.BLUE+" - DNS Lookup")
    time.sleep(0.1)

    print(Fore.GREEN+"  [09]"+Fore.BLUE+" - Cms Detect")
    time.sleep(0.1)

    print(Fore.GREEN+"  [10]"+Fore.BLUE+" - Robots Scanner")
    time.sleep(0.1)

    print(Fore.GREEN+"  [11]"+Fore.BLUE+"- Admin Page Finder")
    time.sleep(0.1)

    print(Fore.GREEN+"  [12]"+Fore.BLUE+" - Back To Menu")
    time.sleep(0.1)

    print(Fore.GREEN+"  [13]"+Fore.WHITE+" - Exit \n")

def List():
    time.sleep(0.1)
    print(Fore.GREEN+"  [01]"+Fore.BLUE+"- Open Tool's Website")
    time.sleep(0.1)
    print(Fore.GREEN+"  [02]"+Fore.BLUE+"- Open Tool's GitHub Repo")
    time.sleep(0.1)
    print(Fore.GREEN+"  [03]"+Fore.BLUE+"- Open Author's Insta Page")
    time.sleep(0.1)
    print(Fore.GREEN+"  [04]"+Fore.BLUE+"- Open Author's Website")
    print('')
def helpList():
    print (w)
    print (w+"{"+B+W+" HELP MENU "+w+"}")
    print (w)
    print (g+" LIST COMMANDS                DESCRIPTIONS"+w)
    print ("-----------------------------------------------------")
    print (w+" help                         show help menu")
    print (w+" update                       check available update")
    print (w+" report                       report about this tool")
    print (w+" clear                        clear windows")
    print (w+" exit                         exit in this tool")
    print ("-----------------------------------------------------")
    print (w)
