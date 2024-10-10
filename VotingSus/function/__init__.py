from dreamlogger import *
import time

debug_mode(True)

def is_candidate(voted):
    file = open("candidat.txt", 'r')
    for line in file.readlines():
        if voted == line.replace('\n', ''):
            debug("Vote + 1")
            return True
    return False   

debug("DEBUG MODE ENABLED")
debug("Functions loaded")