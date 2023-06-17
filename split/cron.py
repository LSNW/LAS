import os, time

def clearTempZips ():
    path = os.path.join('media', 'tempzips')
    now = time.time()

    for file in os.listdir(path):
        fullPath = os.path.join(path, file)
        if (now - os.stat(fullPath).st_mtime) > 1800:
            if os.path.isfile(f):
                os.remove(fullPath)
