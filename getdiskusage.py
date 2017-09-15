""""
getdiskusage.py is a command line application which
takes in a mount point and returns a list of all
the files in the mountpoint with a corresponding list
of all the file sizes in descending order
"""

import os
from collections import OrderedDict
from pprint import pprint
import sys

def get_usage (mountpoint): 

    """
    Return all files in mountpoint with corresponding
    filesizes as a dictionary 
    Args: 
        mountpoint (String): Mount point of the directory
    """

    files = OrderedDict ()
    for root, directory, filenames in os.walk(mountpoint):
            for filename in filenames: 
                file = os.path.join(root,filename)
                size = os.path.getsize(file)
                files [file] = size

    # reverse = True implies descending order
    return {"files":
            [ OrderedDict(sorted(files.items(),
                                key=lambda item: item[1],
                                reverse=True))]}

# This enables this script to be called by another script if needed
if __name__ == '__main__':
    # Validates that an argurment was given wen calling the function
    if len (sys.argv) != 2:
        print ("Usage: getdiskusage.py mountpoint")
        sys.exit(1)
    mountpoint = sys.argv[1]

    # Checks to see if the argument assigned exists
    if not (os.path.isdir(mountpoint)):
        print ("Directory does not exist. Please enter a valid directory")
        sys.exit(1)

    
    pprint (get_usage (mountpoint))
