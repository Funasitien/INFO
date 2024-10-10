#--------------------------------------------------#
# DreamLogger                        - By Dreamcloud
#--------------------------------------------------#
# Suport @ dsc.gg/drmcld
# Full creadits to @Funasitien
#
# github.com/funasitien
# 

class color:
    b = '\033[94m' # Blue
    c = '\033[96m' # Cyan
    g = '\033[92m' # green
    y = '\033[93m' # yellow
    r = '\033[91m' # red
    k = '\033[0m' #rest (or gray)


warn = "warn"
error = "error"
debu = False

def debug_mode(value=False):
    global debu
    if value == True:
        debu = True
    else:
        debu = False

def info(message):
    print("[" + color.b + "INFO" + color.k + "] " + message)

def warn(message):
    print("[" + color.y + "WARN" + color.k + "] " + message)


def error(message):
    print("[" + color.r + "ERROR" + "] " + message + color.k )


def debug(message, type="fine"):
    global debu
    if message == True:
        debu = True
    elif message == False:
        debu = False
    elif debu == False:
        return
    elif type == "error":
        print("[" + color.r + "DEBUG" + color.k + "] " + message)
        return
    elif type == "warn":
        print("[" + color.y + "DEBUG" + color.k + "] " + message)
        return
    else:
        print("[" + color.g + "DEBUG" + color.k + "] " + message)
