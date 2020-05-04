import platform
import os
import datetime
import sys
from log import log, notify

## Work on mac only

LIVING_DAYS = 21
today = datetime.datetime.utcnow()
destination = os.path.join('../Downloads')

def readFiles():
    dir = os.path.dirname(__file__)
    files = os.listdir(destination)
    return files

def modification_date(path_to_file):
    ## Work on mac only
    stat = os.stat(path_to_file)
    lastModified = datetime.datetime.utcfromtimestamp(stat.st_mtime)
    return lastModified

def delete_file(file):
    try:
        log(file + ' will be deleted')
        os.remove(destination + '/' + file)
        pass
    except:
        log(str(sys.exc_info()[0]))
        pass

def delete_old_files():
    files = readFiles()
    log(str(files))
    for file in files:
        lastModified = modification_date(destination + '/' + file)
        difference =  today - lastModified
        if difference.days > LIVING_DAYS:
            delete_file(file)
    log("script finished")
    notify("Download Cleanup", "Script finished")

if __name__ == "__main__":
    log("Script started")
    notify("Download Cleanup", "Script started")
    delete_old_files()