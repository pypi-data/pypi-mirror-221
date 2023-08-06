import os
import sys
def getProjRoot():
    thePath=os.getcwd()
    while True:
        if os.path.exists(thePath+'/.idea'):
            sys.path.append(thePath)
        if thePath=='/' or thePath=='\\':
            break;
        thePath = os.path.dirname(thePath)
