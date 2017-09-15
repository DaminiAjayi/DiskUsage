import os
from collections import OrderedDict
from pprint import pprint
import sys

def get_usage (mountpoint): 

    files = OrderedDict ()
    for root, directories, filenames in os.walk(mountpoint):
            for filename in filenames: 
                file = os.path.join(root,filename)
                size = os.path.getsize(file)
                files [file] = size

    return {"files":[ OrderedDict(sorted(files.items(), key=lambda item: item[1], reverse=True))]}

#This enables this script to be called by another script if needed
if __name__ == '__main__':
    #Validates that an argurment was given wen calling the function
    if len (sys.argv) != 2:
        print ("Usage: getdiskusage.py mountpoint")
        sys.exit(1)

    #Checks to see if the argument assigned exists
    if (os.path.isdir(mountpoint)):
        [print ("Directory does not exist. Please enter a valid directory")]
        sys.exit(1)

    mountpoint = sys.argv[1]
    pprint (get_usage (mountpoint))
