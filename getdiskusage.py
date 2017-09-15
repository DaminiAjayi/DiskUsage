import os
from collections import OrderedDict
from pprint import pprint

def get_usage (mountpoint): 

    files = OrderedDict ()
    for root, directories, filenames in os.walk(mountpoint):
            for filename in filenames: 
                file = os.path.join(root,filename)
                size = os.path.getsize(file)
                files [file] = size

    return {"files":[ OrderedDict(sorted(files.items(), key=lambda item: item[1], reverse=True))]}


pprint (get_usage ("/Users/ajayi/Desktop"))
