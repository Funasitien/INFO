#--------------------------------------------------#
# DreamLogger                        - By Dreamcloud
#--------------------------------------------------#
# Suport @ discord.dreamcloud.tk
# Full creadits to @Funasitien
#
# github.com/funasitien
#   

import os

class color:
    b = '\033[94m' # Blue
    c = '\033[96m' # Cyan
    g = '\033[92m' # green
    y = '\033[93m' # yellow
    j = '\033[93m' # jaune
    r = '\033[91m' # red
    k = '\033[0m' #rest (or gray)

infotext = "[" + color.b + "INFO" + color.k + "]  "
warn = "warn"
error = "error"

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
        print("[" + color.r + "DEBUG" + color.k, "] ", message)
        return
    if type == "warn":
        print("[" + color.y + "DEBUG" + color.k, "] ", message)
        return
    else:
        print("[" + color.g + "DEBUG" + color.k + "] ", message)