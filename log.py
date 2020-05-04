from datetime import datetime
import os
import __main__

def log(text):
    with open('out.txt', 'a') as f:
        print >> f, '[' + str(datetime.utcnow()) + '] ' + __main__.__file__ + ': ' + text

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))