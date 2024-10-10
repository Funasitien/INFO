#--------------------------------------------------#
# DreamLogger                        - By Dreamcloud
#--------------------------------------------------#
# Suport @ discord.dreamcloud.tk
# Full creadits to @Funasitien
#
# github.com/funasitien


import os
import json
from datetime import date

debu = False

class color:
    b = '\033[94m' # Blue
    c = '\033[96m' # Cyan
    g = '\033[92m' # green
    y = '\033[93m' # yellow
    j = '\033[93m' # jaune
    r = '\033[91m' # red
    k = '\033[0m' #rest (or gray)

infotext = "[" + color.b + "INFO" + color.k + "]  "

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def debug_mode(value=False):
    global debu
    if value == True:
        debu = True
    else:
        debu = False

def info(message):
    print("[" + color.b + "INFO" + color.k + "]  ", message)

def warn(message):
    print("[" + color.y + "WARN" + color.k + "]  ", message)


def error(message):
    print("[" + color.r + "ERROR" + color.k + "] ", message)


def debug(message, type="fine"):
    if debu == False:
        return
    if type == "error":
        print(f"[{color.r}DEBUG{color.k}] {message}")
        return
    if type == "warn":
        print(f"[{color.y}DEBUG{color.k}] {message}")
        return
    else:
        print(f"[{color.g}DEBUG{color.k}] {message}")
        
        
        
        
        
        
        
        
        
        

    
def json_save(json_object):
    if date.today().weekday() == 3:
        eguality = False
        debug(json_object, type="warn")
        win = 0
        for i in json_object:
            if json_object[i] > win:
                winner = i
                win = json_object[i]
            elif json_object[i] == win:
                egual = i
                eguality = True
        debug(winner)
        if json_object["Norman"] < win - 1 or eguality == True:
            if eguality==False:
                json_object[winner] = json_object[winner] - 1
                json_object["Norman"] = json_object["Norman"] + 1
            else:
                json_object[egual] = json_object[egual] - 1
                json_object["Norman"] = json_object["Norman"] + 1
        
        debug(json_object, type="error")
        file = open('vote.json', 'w+')
        file.truncate(0)
        json.dump(json_object, file, indent=4)
        file.close()
            